from __future__ import print_function
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from serial_backend import PyCar

car = PyCar()

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/image')
# def index():
#     #TODO return the image
#     return render_template('index.html')

@socketio.on('value changed')
def value_changed(message):
    steering = int(message.get('steering', 90))
    throttle = int(message.get('throttle', 90))
    car.control(steering, throttle)
    # print(steering + " " + throttle)

# @socketio.on('connected')
# def client_connected(message):
# 	print("Connection from: " + message.get(''))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
