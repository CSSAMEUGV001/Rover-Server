from __future__ import print_function
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import json
import pisocket

app = Flask(__name__)
socketio = SocketIO(app)

class Socketor:
    def reconnect(self):
        print('Waiting for RaspberryPi')
        self.piserver = pisocket.SocketCommunicator.server()

sock = Socketor()


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
    steering = int(message.get('steering', 90))
    throttle = int(message.get('throttle', 90))
    try:
        sock.piserver.send_nul(json.dumps({'steering': steering, 'throttle': throttle}).encode())
    except:
        sock.reconnect()
    # print(str(steering) + " " + str(throttle))

if __name__ == '__main__':
    sock.reconnect()
    piip = sock.piserver.sock.getpeername()[0]
    TEMPLATE_VALUES['piip'] = piip
    socketio.run(app, host='0.0.0.0')

