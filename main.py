import serial
import time
from main_camera import DesktopApp

ser=serial.Serial('COM3',9600,timeout=0.5)

while True:
 s=ser.readline()
 s=s.decode('utf-8')
 if s.startswith('#'):
  print('Face Recognition Calling')
  print('Place your Face Properly facing to Camera')
  time.sleep(4)
  print('Face Recognition Process Started')
  DesktopApp().run() 
