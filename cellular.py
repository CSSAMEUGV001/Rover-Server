import serial
import time

class cellular:
	
	def __init__(self, serialpath, baud = 9600)
		self.serial_path = serialpath
		self.baud_rate = baud
		
		
		
		
	def connect(self)
		self.ser = serial.Serial(self.serial_path, self.baud_rate)
		if self.ser.isOpen():
			print "Connected to Fona\n"
		else:
			print "Not connected to Fona\n"
		
		self.connection = True
		
	def setGps(self, offon)
		if self.gps_status:
			self.ser.write("AT+CGPS?")
			msg = self.ser.readline()
		else:
		
	def reset_module(self)
		self.ser.write("AT+CRESET")
		msg = self.ser.readline()
		if msg == "OK":
			print("Reseting")
		else:
			print("Error reseting")
	
	def turn_off_module(self)
		self.ser.write("AT+CPOF")
		msg = self.ser.readline()
		if msg.find(msg) == -1:
			print("Powering Down\n")
		else:
			print("Error Powering Down\n")

	def parse_reply(self, message, separator)
		msgList = message.split(separator)
		
		return msgList
			
		