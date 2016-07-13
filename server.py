from __future__ import print_function
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
from i2c_backend import PyCar
from camera import Camera

car = PyCar()

app = Flask(__name__)
socketio = SocketIO(app)

TEMPLATE_VALUES = {
        'max_throttle': 105,
        'min_throttle': 75,
        'neu_throttle': 90,
        'max_steering': 140,
        'min_steering': 53,
        'neu_steering': 90,
        }

@app.route('/')
def index():
    return render_template('index.html', **TEMPLATE_VALUES)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
           mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('value changed')
def value_changed(message):
    steering = int(message.get('steering', 90))
    throttle = int(message.get('throttle', 90))
    car.control(steering, throttle)
    # print(str(steering) + " " + str(throttle))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
