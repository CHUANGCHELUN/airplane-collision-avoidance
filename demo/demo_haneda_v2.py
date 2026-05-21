"""
demo_haneda_v2.py
──────────────────────────────────────────────────
重現 2023/06/10 羽田事件（完整版，19 架飛機）
需要 HBase 正在執行，請先設定 .env（參考 .env.example）
──────────────────────────────────────────────────
"""
from dotenv import load_dotenv
load_dotenv()
import math
import time
import os
import sys
from datetime import datetime
  

import happybase


class Airplant:
  def __init__(self,gps,span,length,s,deg,ah,fname):
    self.gps = gps
    self.span = span
    self.length = length
    self.id = []
    self.speed = s
    self.degrees = deg
    self.polygon = []
    self.wc= False
    self.wcoler= ' '
    self.wcname = ' '
    self.name = fname
    self.ah = ah
        
def clear_hbase_table(table):
    for key, _ in table.scan():
        table.delete(key)
def write_aircraft_to_hbase(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,t):
    connection = happybase.Connection(os.getenv('HBASE_HOST', 'localhost'))  # 請替換成HBase伺服器的IP地址
    table = connection.table('ground')  # 請替換成您的HBase表名稱
   

    batch = table.batch()

        
    ident = a1.name
    lat_str = a1.gps[0]
    lon_str = a1.gps[1]
    gs = a1.speed*360000
    track = a1.degrees
    flight = a1.name
    altitude_str = a1.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()
    batch = table.batch()

        
    ident = a2.name
    lat_str = a2.gps[0]
    lon_str = a2.gps[1]
    gs = a2.speed*360000
    track = a2.degrees
    flight = a2.name
    altitude_str = a2.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()

    batch = table.batch()

        
    ident = a5.name
    lat_str = a5.gps[0]
    lon_str = a5.gps[1]
    gs = a5.speed*360000
    track = a5.degrees
    flight = a5.name
    altitude_str = a5.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()
    batch = table.batch()

        
    ident = a6.name
    lat_str = a6.gps[0]
    lon_str = a6.gps[1]
    gs = a6.speed*360000
    track = a6.degrees
    flight = a6.name
    altitude_str = a6.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()
    batch = table.batch()

        
    ident = a8.name
    lat_str = a8.gps[0]
    lon_str = a8.gps[1]
    gs = a8.speed*360000
    track = a8.degrees
    flight = a8.name
    altitude_str = a8.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()
    batch = table.batch()

        
    ident = a9.name
    lat_str = a9.gps[0]
    lon_str = a9.gps[1]
    gs = a9.speed*360000
    track = a9.degrees
    flight = a9.name
    altitude_str = a9.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()
    batch = table.batch()

        
    ident = a10.name
    lat_str = a10.gps[0]
    lon_str = a10.gps[1]
    gs = a10.speed*360000
    track = a10.degrees
    flight = a10.name
    altitude_str = a10.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()


    table = connection.table('ground')
    if(a3.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a3.name
    lat_str = a3.gps[0]
    lon_str = a3.gps[1]
    gs = a3.speed*360000
    track = a3.degrees
    flight = a3.name
    altitude_str = a3.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()
    
    table = connection.table('ground')
    if(a4.ah>0):
        table = connection.table('air')

        
    batch = table.batch()

        
    ident = a4.name
    lat_str = a4.gps[0]
    lon_str = a4.gps[1]
    gs = a4.speed*360000
    track = a4.degrees
    flight = a4.name
    altitude_str = a4.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()
    table = connection.table('ground')
    if(a7.ah>0):
        table = connection.table('air')

        
    batch = table.batch()

        
    ident = a7.name
    lat_str = a7.gps[0]
    lon_str = a7.gps[1]
    gs = a7.speed*360000
    track = a7.degrees
    flight = a7.name
    altitude_str = a7.ah


        # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

    # 寫入HBase表
    batch.send()
    table = connection.table('ground')
    if(a11.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a11.name
    lat_str = a11.gps[0]
    lon_str = a11.gps[1]
    gs = a11.speed*360000
    track = a11.degrees
    flight = a11.name
    altitude_str = a11.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()
    table = connection.table('ground')
    if(a12.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a12.name
    lat_str = a12.gps[0]
    lon_str = a12.gps[1]
    gs = a12.speed*360000
    track = a12.degrees
    flight = a12.name
    altitude_str = a12.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()
    table = connection.table('ground')
    if(a13.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a13.name
    lat_str = a13.gps[0]
    lon_str = a13.gps[1]
    gs = a13.speed*360000
    track = a13.degrees
    flight = a13.name
    altitude_str = a13.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()
    table = connection.table('ground')
    if(a14.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a14.name
    lat_str = a14.gps[0]
    lon_str = a14.gps[1]
    gs = a14.speed*360000
    track = a14.degrees
    flight = a14.name
    altitude_str = a14.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()
    table = connection.table('ground')
    if(a15.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a15.name
    lat_str = a15.gps[0]
    lon_str = a15.gps[1]
    gs = a15.speed*360000
    track = a15.degrees
    flight = a15.name
    altitude_str = a15.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()

    table = connection.table('ground')
    if(a16.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a16.name
    lat_str = a16.gps[0]
    lon_str = a16.gps[1]
    gs = a16.speed*360000
    track = a16.degrees
    flight = a16.name
    altitude_str = a16.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()

    table = connection.table('ground')
    if(a17.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a17.name
    lat_str = a17.gps[0]
    lon_str = a17.gps[1]
    gs = a17.speed*360000
    track = a17.degrees
    flight = a17.name
    altitude_str = a17.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()

    table = connection.table('ground')
    if(a18.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a18.name
    lat_str = a18.gps[0]
    lon_str = a18.gps[1]
    gs = a18.speed*360000
    track = a18.degrees
    flight = a18.name
    altitude_str = a18.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()

    table = connection.table('ground')
    if(a19.ah>0):
        table = connection.table('air')
    
        
    batch = table.batch()
    
    ident = a19.name
    lat_str = a19.gps[0]
    lon_str = a19.gps[1]
    gs = a19.speed*360000
    track = a19.degrees
    flight = a19.name
    altitude_str = a19.ah


            # 將資訊加入 batch
    if all(field != 'N/A' for field in [lat_str, lon_str, gs]):
        batch.put(str(ident).encode(), {
            b'info:lat': str(lat_str).encode(),
            b'info:lon': str(lon_str).encode(),
            b'info:gs': str(gs).encode(),
            b'info:track': str(track).encode(),
            b'info:flight': str(flight).encode(),
            b'info:altitude': str(altitude_str).encode(),
            b'info:ver': str(t).encode()
        })

        # 寫入HBase表
    batch.send()

    print("t=",t)
    table = connection.table('ground')
   
    for key, data in table.scan():
        # 转换字节数组为字符串并移除'b'前缀
        clean_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}
        name = clean_data.get('info:flight', '')
        ver = clean_data.get('info:ver', '0')
        if(abs(int(t)-int(ver))>2):
            print(ver)
            table.delete(row=name)

    table = connection.table('air')
    for key, data in table.scan():
        # 转换字节数组为字符串并移除'b'前缀
        clean_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}
        name = clean_data.get('info:flight', '')
        ver = clean_data.get('info:ver', '0')
        if(abs(int(t)-int(ver))>2):
            table.delete(row=name)
 

    connection.close()
if __name__ == "__main__":
    while True:
        #羽田 35.5540972948419,139.77068652455744 deg 325   35.552057606251715,139.77213472988404
        #35.55470322217961, 139.7703532766479 deg 356
        #第一台飛機24.26928217538842,120.62040502246616 24.275000, 120.620030
        current_id = [35.552057606251715,139.77213472988404]#GPS座標
        span = 0.0000648 #翼展
        length = 0.0000739 #機身長
        speed = 0.000133
        angle_degrees = 325
        ah = 0
        a1 = Airplant(current_id,span,length,speed,angle_degrees,ah,'TG-683')

        #第二台飛機
        current_id2 = [35.55434549791139,139.7705127308972]#GPS座標
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000133
        angle_degrees = 325
        ah = 0
        a2 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'BR-189')

        current_id2 = [35.55843, 139.79183]#GPS座標
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000188
        angle_degrees = 325
        ah = 100
        a3 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'UA-881')

        current_id2 = [35.53566, 139.78631]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000833#306km
        angle_degrees = 325
        ah = 200
        a4 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'JL-12')
        
        current_id2 = [35.54521, 139.78451]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 320
        ah = 0
        a5 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'JL-556')#556
        current_id2 = [35.547718, 139.78341]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 45
        ah = 0
        a6 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-477')
        current_id2 = [35.53012, 139.80520]#GPS座標
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000123#306km
        angle_degrees = 145
        ah = 0
        a7 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'HD-44')
        current_id2 = [35.547018, 139.76956732766479]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 100
        ah = 0
        a8 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-478')
        current_id2 = [35.549018, 139.76786732766479]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 100
        ah = 0
        a9 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-500')
        current_id2 = [35.548518, 139.76556732766479]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 150
        ah = 0
        a10 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'JL-120')
        current_id2 = [35.555018, 139.78636732766479]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000000#306km
        angle_degrees = 150
        ah = 0
        a11 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-438')
        current_id2 = [35.545018, 139.77106732766479]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 245
        ah = 0
        a12 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-428')
        current_id2 = [35.544018, 139.77156732766479]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.00000#306km
        angle_degrees = 235
        ah = 0
        a13 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'EVA-708')
        current_id2 = [35.555208, 139.78706732766479]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000000#306km
        angle_degrees = 150
        ah = 0
        a14 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-440')
        current_id2 = [35.555688, 139.78806732766479]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000000#306km
        angle_degrees = 150
        ah = 0
        a15 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-450')
        current_id2 = [35.552818, 139.78856732766479]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000000#306km
        angle_degrees = 260
        ah = 0
        a16 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-460')
        current_id2 = [35.551018, 139.79006732766479]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000000#306km
        angle_degrees = 60
        ah = 0
        a17 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-462')
        current_id2 = [35.551818, 139.789256732766479]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000000#306km
        angle_degrees = 260
        ah = 0
        a18 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-468')
        current_id2 = [35.564740, 139.78493]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000000#306km
        angle_degrees = 10
        ah = 0
        a19 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-380')
        T = 0
        
        while T<50:
            angle_radians = math.radians(a1.degrees)
            direction1 = angle_radians 
            a1.gps[0] = a1.gps[0] + a1.speed * 1 * math.cos(direction1)
            a1.gps[1] = a1.gps[1] + a1.speed * 1 * math.sin(direction1)
            if(T==20):
               a1.speed=0
            elif(T>25):
                a1.speed=0.000133
                if(T>45):
                    a1.degrees=(a1.degrees+15)%360
            
            angle_radians = math.radians(a2.degrees)
            direction1 = angle_radians 
            a2.gps[0] = a2.gps[0] + a2.speed * 1 * math.cos(direction1)
            a2.gps[1] = a2.gps[1] + a2.speed * 1 * math.sin(direction1)
            if(T>3):
                a2.speed=0
            else:
                a2.degrees=(a2.degrees+15)%360
            if(29>T>21):
                a2.speed=0.000143
                a2.degrees=(a2.degrees+13)%360
            elif(T>29):
                a2.speed=0.000133
                if(35>T>32):
                    a2.degrees=(a2.degrees+5)%360
                elif(T>46):
                    a2.degrees=(a2.degrees+5)%360
                
            

            angle_radians1 = math.radians(a3.degrees)
            direction2 = angle_radians1 
            a3.gps[0] = a3.gps[0] + a3.speed * 1 * math.cos(direction2)
            a3.gps[1] = a3.gps[1] + a3.speed * 1 * math.sin(direction2)
            if(a3.ah>0):
                a3.ah = a3.ah - 10
            if(50>T>43):
                a3.degrees = (a3.degrees-14)%360

            angle_radians2 = math.radians(a4.degrees)
            direction3 = angle_radians2 
            a4.gps[0] = a4.gps[0] + a4.speed * 1 * math.cos(direction3)
            a4.gps[1] = a4.gps[1] + a4.speed * 1 * math.sin(direction3)
            if a4.speed>0.000133:
                a4.speed = a4.speed-0.00002
                
            if(a4.ah!=0):
                a4.ah = a4.ah - 10
            if(T==10):
                a4.degrees=a4.degrees-1
            angle_radians3 = math.radians(a7.degrees)
            direction4 = angle_radians3
            a7.gps[0] = a7.gps[0] + a7.speed * 1 * math.cos(direction4)
            a7.gps[1] = a7.gps[1] + a7.speed * 1 * math.sin(direction4)
            if(13>T>10):
                a7.degrees=a7.degrees -10
            elif(31>T>23):
                a7.degrees=(a7.degrees -11)%360
            elif(38>T>35):     
                a7.speed=a7.speed+0.0005    
            if(T>40):
                a7.ah=a7.ah+100

            

            tt = datetime.now().strftime("%S")
            write_aircraft_to_hbase(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,tt)
            T+=1
            time.sleep(0.2)


