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
		if self.gps_status == True:
			self.ser.write("AT+CGPS?")
			msg = self.ser.readline()
		else:
			
		