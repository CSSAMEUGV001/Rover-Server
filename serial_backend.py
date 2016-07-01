#!/usr/bin/env python3
from __future__ import print_function
import socket
import sys
import serial
import os


class PyCar:
    SERIAL_PATH_1 = '/dev/ttyACM0'
    SERIAL_PATH_2 = '/dev/ttyACM1'

    def __init__(self):
        if os.path.exists(self.SERIAL_PATH_1):
            self.ser = serial.Serial(self.SERIAL_PATH_1)
        else:
            self.ser = serial.Serial(self.SERIAL_PATH_2)

    def control(self, steering, throttle):
        message = '{} {}\n'.format(steering, throttle)
        print(message, end='')
        written = self.ser.write(message)
        if written != len(message):
                print("message truncated")
                self.ser.flush()

if __name__ == '__main__':
    car = PyCar()
    car.control(90, 90)

