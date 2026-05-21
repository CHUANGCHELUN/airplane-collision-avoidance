import os
import requests
from flask import Flask, jsonify
from flask_cors import CORS
import happybase
from dotenv import load_dotenv

load_dotenv()

HBASE_HOST         = os.getenv('HBASE_HOST', 'localhost')
FLIGHTAWARE_API_KEY = os.getenv('FLIGHTAWARE_API_KEY', '')
FLASK_HOST         = os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT         = int(os.getenv('FLASK_PORT', 8081))

app = Flask(__name__)
CORS(app)


def scan_table(conn, table_name):
    """掃描 HBase 表，回傳 {column: value} 字典列表"""
    table = conn.table(table_name)
    rows  = []
    for key, data in table.scan():
        rows.append({k.decode(): v.decode() for k, v in data.items()})
    return rows


@app.route('/get_hbase_data', methods=['GET'])
def get_data():
    conn   = happybase.Connection(HBASE_HOST)
    output = {}

    # 地面飛機
    for d in scan_table(conn, 'ground'):
        fname = d.get('info:flight', '')
        output[fname] = {
            'icao':     d.get('info:icao', ''),
            'lat':      float(d.get('info:lat', 0)),
            'lng':      float(d.get('info:lon', 0)),
            'name':     fname,
            'speed':    float(d.get('info:gs', 0)),
            'degrees':  float(d.get('info:track', 0)),
            'ah':       d.get('info:altitude', ''),
            'ver':      d.get('info:ver', ''),
            'wc': False, 'wcoler': '', 'wcname': '', 'time': '', 'distance': '',
        }

    # 警告狀態
    for d in scan_table(conn, 'warning'):
        name = d.get('Info:name', '')
        if name in output:
            output[name].update({
                'wc':       d.get('Info:wc', ''),
                'wcoler':   d.get('Info:wcoler', ''),
                'wcname':   d.get('Info:wcname', ''),
                'time':     d.get('Info:time', ''),
                'distance': d.get('Info:distance', ''),
            })

    # 飛行中飛機
    for d in scan_table(conn, 'air'):
        fname = d.get('info:flight', '')
        output[fname] = {
            'icao':    d.get('info:icao', ''),
            'lat':     float(d.get('info:lat', 0)),
            'lng':     float(d.get('info:lon', 0)),
            'name':    fname,
            'speed':   float(d.get('info:gs', 0)),
            'degrees': float(d.get('info:track', 0)),
            'ah':      d.get('info:altitude', ''),
            'ver':     d.get('info:ver', ''),
            'wc': False, 'wcoler': '', 'wcname': '', 'time': '', 'distance': '',
        }

    conn.close()
    return output


@app.route('/get_api_data/<flightname>', methods=['GET'])
def flight_info(flightname):
    if not FLIGHTAWARE_API_KEY:
        return {'error': 'FLIGHTAWARE_API_KEY not set'}, 500
    url      = f'https://aeroapi.flightaware.com/aeroapi/flights/{flightname}'
    response = requests.get(url, headers={'x-apikey': FLIGHTAWARE_API_KEY})
    return response.json()


if __name__ == '__main__':
    print(f'Server starting on {FLASK_HOST}:{FLASK_PORT}')
    app.run(host=FLASK_HOST, port=FLASK_PORT)
