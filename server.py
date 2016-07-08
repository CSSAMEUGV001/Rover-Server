from __future__ import print_function
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from i2c_backend import PyCar

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

# @app.route('/image')
# def index():
#     #TODO return the image
#     return render_template('index.html')

@socketio.on('value changed')
def value_changed(message):
    steering = int(message.get('steering', 90))
    throttle = int(message.get('throttle', 90))
    car.control(steering, throttle)
    # print(str(steering) + " " + str(throttle))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
