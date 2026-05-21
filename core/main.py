import os
import math
import time
import json
import threading
import requests
import numpy as np
import happybase
from numpy import sin, cos, arccos, pi, round
from shapely.geometry import Polygon as ShapelyPolygon
from dotenv import load_dotenv

load_dotenv()

HBASE_HOST    = os.getenv('HBASE_HOST', 'localhost')
LINE_TOKEN    = os.getenv('LINE_TOKEN', '')
JSON_OUTPUT   = os.getenv('JSON_OUTPUT_PATH', './output.json')

has_yellow_warning = {}
has_red_warning = {}
has_intersect_yellow_warning = {}
has_intersect_red_warning = {}
appInfo  = {}
appstate = {}


class Airplant:
    def __init__(self, gps, span, length, s, deg, ah, fname):
        self.gps      = gps
        self.span     = span
        self.length   = length
        self.id       = []
        self.speed    = s
        self.degrees  = deg
        self.polygon  = []
        self.wc       = False
        self.wcoler   = ''
        self.wcname   = ''
        self.name     = fname
        self.ah       = ah
        self.time     = 0
        self.distance = 0


# ──────────────────────────────────────────────
# LINE 通知
# ──────────────────────────────────────────────
def line_notify(msg):
    if not LINE_TOKEN:
        print(f'[LINE NOTIFY skipped] {msg}')
        return
    headers = {
        'Authorization': 'Bearer ' + LINE_TOKEN,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    requests.post('https://notify-api.line.me/api/notify',
                  headers=headers, params={'message': msg})


# ──────────────────────────────────────────────
# 距離 / 幾何 工具
# ──────────────────────────────────────────────
def rad2deg(r): return r * 180 / pi
def deg2rad(d): return d * pi / 180

def haversine_meters(a1, a2):
    """兩個 Airplant 之間的距離（公尺）"""
    theta = a1.gps[1] - a2.gps[1]
    dist  = 60 * 1.1515 * rad2deg(
        arccos(
            sin(deg2rad(a1.gps[0])) * sin(deg2rad(a2.gps[0])) +
            cos(deg2rad(a1.gps[0])) * cos(deg2rad(a2.gps[0])) * cos(deg2rad(theta))
        )
    )
    return round(dist * 1.609344 * 1000, 2)


def aircraft_corners(ac):
    """計算飛機四個角的 GPS 座標（用於 SAT 多邊形）"""
    rad = math.radians(ac.degrees)
    cx  = ac.gps[0] + ac.length / 2 * math.cos(rad)
    cy  = ac.gps[1] + ac.length / 2 * math.sin(rad)
    corners = []
    for sx, sy in [(−1, 1), (1, −1)]:
        corners.append((cx + sx * ac.span / 2 * math.sin(rad),
                         cy + sy * ac.span / 2 * math.cos(rad)))
    cx2 = ac.gps[0] − ac.length / 2 * math.cos(rad)
    cy2 = ac.gps[1] − ac.length / 2 * math.sin(rad)
    for sx, sy in [(1, −1), (−1, 1)]:
        corners.append((cx2 + sx * ac.span / 2 * math.sin(rad),
                          cy2 + sy * ac.span / 2 * math.cos(rad)))
    return corners


def predict_corners(ac, seconds=30):
    """預測 seconds 秒後的四個角位置（保留機尾兩個角不動）"""
    rad     = math.radians(ac.degrees)
    future  = []
    for pt in ac.id:
        future.append((
            pt[0] + ac.speed / 360000 * seconds * math.cos(rad),
            pt[1] + ac.speed / 360000 * seconds * math.sin(rad),
        ))
    future[2] = ac.id[2]
    future[3] = ac.id[3]
    return future


def polygons_intersect(p1, p2):
    return ShapelyPolygon(p1).intersects(ShapelyPolygon(p2))


# ──────────────────────────────────────────────
# JSON / HBase I/O
# ──────────────────────────────────────────────
def to_dict(ac):
    return {
        'lat':      ac.gps[0],
        'lng':      ac.gps[1],
        'name':     ac.name,
        'speed':    ac.speed * 1000 / 3600,
        'wc':       ac.wc,
        'wcoler':   ac.wcoler,
        'wcname':   ac.wcname,
        'degrees':  ac.degrees,
        'ah':       ac.ah,
        'distance': ac.distance,
        'time':     ac.time,
    }


def clear_hbase_table(table):
    for key, _ in table.scan():
        table.delete(key)


def save_to_hbase_and_json():
    global appInfo, appstate
    appstate = appInfo.copy()

    conn  = happybase.Connection(HBASE_HOST)
    table = conn.table('warning')
    clear_hbase_table(table)
    batch = table.batch()
    for name, info in appInfo.items():
        batch.put(str(name).encode(), {
            b'Info:wc':       str(info['wc']),
            b'Info:wcoler':   info['wcoler'],
            b'Info:wcname':   info['wcname'],
            b'Info:name':     info['name'],
            b'Info:time':     str(info['time']),
            b'Info:distance': str(info['distance']),
        })
    batch.send()
    conn.close()

    with open(JSON_OUTPUT, 'w') as f:
        json.dump(appInfo, f, indent=2)
    appInfo.clear()


def fetch_ground_aircraft():
    """從 HBase ground table 讀取地面滑行飛機"""
    conn  = happybase.Connection(HBASE_HOST)
    table = conn.table('ground')
    result = {}
    for key, data in table.scan():
        d     = {k.decode(): v.decode() for k, v in data.items()}
        fname = d.get('info:flight', '')
        ac    = Airplant(
            gps    = [float(d.get('info:lat', 0)), float(d.get('info:lon', 0))],
            span   = 0.000648,
            length = 0.000739,
            s      = float(d.get('info:gs', 0)),
            deg    = float(d.get('info:track', 0)),
            ah     = d.get('info:altitude', '0'),
            fname  = fname,
        )
        result[key.decode()] = ac
    conn.close()
    return result


# ──────────────────────────────────────────────
# 碰撞偵測核心（SAT + TTC + 三圈警戒）
# ──────────────────────────────────────────────
GREEN_R  = 834   # 公尺
YELLOW_R = 500
RED_R    = 276

def detect_collision(a1, a2):
    global appInfo

    a1.id      = aircraft_corners(a1)
    a2.id      = aircraft_corners(a2)
    a1.polygon = predict_corners(a1)
    a2.polygon = predict_corners(a2)

    intersect = polygons_intersect(a1.polygon, a2.polygon)
    dist      = haversine_meters(a1, a2)
    ttc       = 0
    if abs(a1.speed − a2.speed) > 0:
        ttc = round(dist / abs(a1.speed * 1000 / 3600 − a2.speed * 1000 / 3600), 3)

    def clear_warning(ac, other_name):
        if ac.wcname == other_name:
            ac.wc, ac.wcname, ac.wcoler = False, '', ''
            for d in [has_yellow_warning, has_intersect_yellow_warning,
                      has_red_warning,    has_intersect_red_warning]:
                d.pop(ac.name, None)

    if dist > YELLOW_R:
        clear_warning(a1, a2.name)
        clear_warning(a2, a1.name)

    elif YELLOW_R >= dist > RED_R:
        for ac, other in [(a1, a2), (a2, a1)]:
            if not ac.wc and ac.wcoler != 'R':
                ac.wcoler, ac.wcname = 'Y', other.name
                ac.distance, ac.time = dist, ttc
        if intersect:
            a1.wc = a2.wc = True

        if a1.name not in has_yellow_warning or a2.name not in has_yellow_warning:
            line_notify(f'Yellow Warning: {a1.name} & {a2.name} distance {dist}m')
            has_yellow_warning[a1.name] = has_yellow_warning[a2.name] = True
        if intersect and (a1.name not in has_intersect_yellow_warning):
            line_notify(f'Yellow Warning: {a1.name} & {a2.name} 即將碰撞，距離 {dist}m')
            has_intersect_yellow_warning[a1.name] = has_intersect_yellow_warning[a2.name] = True

    else:  # dist <= RED_R
        for ac, other in [(a1, a2), (a2, a1)]:
            ac.wcoler, ac.wcname = 'R', other.name
            ac.distance, ac.time = dist, ttc
            ac.wc = intersect

        if a1.name not in has_red_warning or a2.name not in has_red_warning:
            line_notify(f'Red Warning: {a1.name} & {a2.name} distance {dist}m')
            has_red_warning[a1.name] = has_red_warning[a2.name] = True
        if intersect and (a1.name not in has_intersect_red_warning):
            line_notify(f'Red Warning: {a1.name} & {a2.name} 即將碰撞，距離 {dist}m')
            has_intersect_red_warning[a1.name] = has_intersect_red_warning[a2.name] = True

    appInfo.update({a1.name: to_dict(a1), a2.name: to_dict(a2)})


# ──────────────────────────────────────────────
# 主迴圈
# ──────────────────────────────────────────────
if __name__ == '__main__':
    print(f'Connecting to HBase at {HBASE_HOST} …')
    while True:
        aircraft = list(fetch_ground_aircraft().values())

        for ac in aircraft:
            if ac.name in appstate:
                prev = appstate[ac.name]
                ac.wc, ac.wcoler, ac.wcname = prev['wc'], prev['wcoler'], prev['wcname']

        for i in range(len(aircraft)):
            for j in range(i + 1, len(aircraft)):
                a1, a2 = aircraft[i], aircraft[j]
                if a1.speed > 0 or a2.speed > 0:
                    detect_collision(a1, a2)

        if len(aircraft) == 1:
            ac = aircraft[0]
            appInfo[ac.name] = to_dict(ac)

        save_to_hbase_and_json()
        time.sleep(1)
