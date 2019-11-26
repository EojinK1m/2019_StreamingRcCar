from importlib import import_module #import 라는 모듈의 import_module이라는 함수 사용
from flask import Flask, render_template, Response#Flask
import os#OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

if os.environ.get('CAMERA'): #카메라 모듈의 환경 변수나, 디렉터리, 파일 등의 정보를 받아온다
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera#임포트하고 싶은 모듈을 변수명으로 사용하는 코드
else:
    from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

def gen(camera):
   while True:
       frame = camera.get_frame()
       yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
   return Response(gen(Camera()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
   app.run( debug=True, threaded=True)