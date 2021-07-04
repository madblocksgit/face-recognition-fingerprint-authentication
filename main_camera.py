from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import *
import time
from face import face_reg

ACCESS_ID = "AKIAU3FKDER5U6ZAKOFA" 
ACCESS_KEY = "2vWiY74A6tq4e00x17BI8rqnRG9j4HvsLP5Q5qmQ" 
REGION = "ap-south-1" #ap-south-1

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')

class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("demo.jpg")
        print("Captured")
        if(face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='1.jpeg',target='demo.jpg')):
        	print('Customer1 Found')
        elif(face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='2.jpg',target='demo.jpg')):
        	print('Customer2 Found')
        elif(face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='3.jpeg',target='demo.jpg')):
        	print('Customer3 Found')
        elif(face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='4.jpeg',target='demo.jpg')):
        	print('Customer4 Found')
        elif(face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='mad.jpg',target='demo.jpg')):
        	print('Customer5 Found')
        else:
        	print('No Customer Matched')

class DesktopApp(App):
    def build(self):
        return (CameraClick())

