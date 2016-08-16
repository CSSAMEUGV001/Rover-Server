from __future__ import print_function
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import json
import pisocket

app = Flask(__name__)
socketio = SocketIO(app)
piserver = None

TEMPLATE_VALUES = {
        'framerate': 15,
        'throttle_scale': 0.1,
        'steering_scale': 0.1,
        'neu_throttle': 90,
        'neu_steering': 90,
        }

@app.route('/')
def index():
    return render_template('index.html', **TEMPLATE_VALUES)

@socketio.on('value changed')
def value_changed(message):
    if piserver != None:
        steering = int(message.get('steering', 90))
        throttle = int(message.get('throttle', 90))
        try:
            piserver.send_nul(json.dumps({'steering': steering, 'throttle': throttle}).encode())
        except:
            pass
        # print(str(steering) + " " + str(throttle))

if __name__ == '__main__':
    print('Waiting for RaspberryPi')
    piserver = pisocket.SocketCommunicator.server()
    piip = piserver.sock.getpeername()[0]
    TEMPLATE_VALUES['piip'] = piip
    socketio.run(app, host='0.0.0.0')

