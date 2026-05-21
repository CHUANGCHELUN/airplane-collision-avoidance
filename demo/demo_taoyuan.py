"""
demo_taoyuan.py
──────────────────────────────────────────────────
桃園國際機場實測場景（13 架飛機）
需要 HBase 正在執行，請先設定 .env（參考 .env.example）
──────────────────────────────────────────────────
"""
from dotenv import load_dotenv
load_dotenv()
import math
import time
from datetime import datetime
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
def write_aircraft_to_hbase(a11,a12,a13,t):
    connection = happybase.Connection(os.getenv('HBASE_HOST', 'localhost'))  # 請替換成HBase伺服器的IP地址
    table = connection.table('ground')  # 請替換成您的HBase表名稱
   

    
    table = connection.table('ground')
    if(a11.ah>0):
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


    

    print("t=",t)
    
        
 
        
       
        
        

     

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
        #桃機
        current_id2 = [25.084690,121.233431]
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000080#306km
        angle_degrees = 80
        ah = 0
        a11 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'CCA-195')
        current_id2 = [25.079282,121.224026]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000433#306km
        angle_degrees = 52
        ah = 100
        a12 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'CAL-5882')
        current_id2 = [25.082788, 121.242461]#GPS座標35.50886
        span = 0.000648 #翼展
        length = 0.000739 #機身長
        speed = 0.000080#306km
        angle_degrees = 137
        ah = 0
        a13 = Airplant(current_id2,span,length,speed,angle_degrees,ah,'EVA-708')
        T = 0
    
        while T<140:
            angle_radians3 = math.radians(a11.degrees)
            direction4 = angle_radians3
            a11.gps[0] = a11.gps[0] + a11.speed * 1 * math.cos(direction4)
            a11.gps[1] = a11.gps[1] + a11.speed * 1 * math.sin(direction4)

            if(8>T>3):
                a11.degrees=(a11.degrees-4)%360
            elif(T==18):
                a11.degrees=52
            elif(20>T>18):
                a11.speed=a11.speed+0.00004
            elif(42>T>36):
                a11.speed=a11.speed-0.00001
            elif(T==45):
                a11.speed=0
            elif(95>T>90):
                a11.speed=a11.speed+0.00001
            elif(114>T>104):
                a11.speed=0.00003
                a11.degrees=(a11.degrees+5)%360
            elif(T==125):
                    a11.degrees=135
                    a11.speed=0.0001033
            elif(T==129):
                a11.speed=0.0001

            angle_radians3 = math.radians(a12.degrees)
            direction4 = angle_radians3
            a12.gps[0] = a12.gps[0] + a12.speed * 1 * math.cos(direction4)
            a12.gps[1] = a12.gps[1] + a12.speed * 1 * math.sin(direction4)
            
            if(27>T>23):
                if(a12.ah>0):
                    a12.ah=a12.ah-50
                if(a12.speed>0.0002):
                    a12.speed=a12.speed-0.00015
            if(32>T>29):
                a12.degrees=a12.degrees+10
                a12.speed=0.00008
            if(54>T>52):
                a12.degrees=a12.degrees+9
            
            elif(93>T>82):
                a12.degrees=a12.degrees-3
            elif(T==91):
                a12.speed=0.000103
            elif(118>T>109):
                if(a12.speed<0.000040):
                    a12.speed=a12.speed-0.00002
                a12.degrees=(a12.degrees+10)%360
            elif(T==128):
                a12.speed=0    
            
            angle_radians3 = math.radians(a13.degrees)
            direction4 = angle_radians3
            a13.gps[0] = a13.gps[0] + a13.speed * 1 * math.cos(direction4)
            a13.gps[1] = a13.gps[1] + a13.speed * 1 * math.sin(direction4)
            if(73>T>61):
                a13.speed=0.00003
                a13.degrees=(a13.degrees+5)%360
            elif(T==82):
                a13.degrees=231
            elif(100>T>83):
                a13.speed=a13.speed+0.00005
            elif(110>T>100):
                a13.ah=a13.ah+100
                a13.speed=a13.speed+0.0001

                
           
        
            tt = datetime.now().strftime("%S")
            write_aircraft_to_hbase(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,tt)
            T+=1
            time.sleep(1)


