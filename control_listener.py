import pisocket
import json
from i2c_backend import PyCar


car = PyCar()
client = pisocket.SocketCommunicator.client()

while True:
    message = client.read_to_nul()
    controls = json.loads(message.decode())
    steering = int(controls.get('steering', 90))
    throttle = int(controls.get('throttle', 90))
    car.control(steering, throttle)

