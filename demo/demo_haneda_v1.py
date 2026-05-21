"""
demo_haneda_v1.py
─────────────────────────────────────────────────────────────
重現 2023/06/10 日本羽田機場碰撞事件（簡化版，10 架飛機）
涉及航班：TG-683（泰航）、BR-189（長榮）等
需要 HBase 正在執行，請先設定 .env（參考 .env.example）
─────────────────────────────────────────────────────────────
"""
from dotenv import load_dotenv
load_dotenv()
import math
import time
import os
import sys

  

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
def write_aircraft_to_hbase(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,t):
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

    print("t=",t)
    table = connection.table('ground')
    for key, data in table.scan():
        # 转换字节数组为字符串并移除'b'前缀
        clean_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}
        name = clean_data.get('info:flight', '')
        ver = clean_data.get('info:ver', '')
        if(str(ver)!=str(t)):
            print(ver)
            table.delete(row=name)

    table = connection.table('air')
    for key, data in table.scan():
        # 转换字节数组为字符串并移除'b'前缀
        clean_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}
        name = clean_data.get('info:flight', '')
        ver = clean_data.get('info:ver', '')
        if(str(ver)!=str(t)):
            table.delete(row=name)
        
 
        
       
        
        

     

    connection.close()
if __name__ == "__main__":
    while True:
        #羽田 35.5540972948419,139.77068652455744 deg 325   35.552057606251715,139.77213472988404
        #35.55470322217961, 139.7703532766479 deg 356
        #第一台飛機24.26928217538842,120.62040502246616 24.275000, 120.620030
        current_id = [35.552057606251715,139.77213472988404]#GPS座標
        span = 0.000648 #翼展
        length = 0.000739 #機身長
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
        
        current_id2 = [35.54421, 139.78451]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 45
        ah = 0
        a5 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'JL-556')#556
        current_id2 = [35.547818, 139.78341]#GPS座標35.50886
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
        angle_degrees = 130
        ah = 0
        a8 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-478')
        current_id2 = [35.549018, 139.76786732766479]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 330
        ah = 0
        a9 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'NH-500')
        current_id2 = [35.548518, 139.76556732766479]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.0000#306km
        angle_degrees = 150
        ah = 0
        a10 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'JL-120')
        
        T = 0
        
        while T<30:
            angle_radians = math.radians(a1.degrees)
            direction1 = angle_radians 
            a1.gps[0] = a1.gps[0] + a1.speed * 1 * math.cos(direction1)
            a1.gps[1] = a1.gps[1] + a1.speed * 1 * math.sin(direction1)
            if(T==23):
               a1.speed=0
            
            angle_radians = math.radians(a2.degrees)
            direction1 = angle_radians 
            a2.gps[0] = a2.gps[0] + a2.speed * 1 * math.cos(direction1)
            a2.gps[1] = a2.gps[1] + a2.speed * 1 * math.sin(direction1)
            
            if(T>2):
                a2.speed=0
            else:
                a2.degrees=(a2.degrees+15)%360

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
                a4.speed = a4.speed-0.00005
                
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

            write_aircraft_to_hbase(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,T)
            T+=1
            time.sleep(1)


