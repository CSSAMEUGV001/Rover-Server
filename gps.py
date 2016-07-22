import serial
import time

class gps:
    DEFAULT_SERIAL_PATH = '/dev/ttyUSB0'

    def __init__(self, serial_port = DEFAULT_SERIAL_PATH, baud = 9600):
        self.port = serial_port
        self.baud = baud

        self.gpsOn = False
		
		self.connect()

#        if msg == "OK":
#            print "Connected"
#            self.connected = True
#        else:
#            print "OK Not returned"
#            self.connected = False

    def connect(self):
        self.ser = serial.Serial(serial_path, baud)
        while msg != "OK":
            self.ser.write("at\n")
            msg = self.ser.readline()
        print "Connected to module, OK received"

	#Gets raw gps data returned from gps module
    def getGPS(self):
		msg = "ERROR"
        if self.connected and self.gpsOn:
			while True:
				self.ser.write("At+CGPSINFO")
				time.sleep(1)
				msg = self.ser.readline()
				if msg.find("+CGPSINFO:") != -1:
					break
        return msg	
			
	#Turns the gps module on
    def startGPS(self):
        if self.connected == True:
            while self.gpsOn == False:
                self.ser.write("AT+CGPS=1")
                msg = self.ser.readline()
                if msg == "OK"
                    self.gpsOn = True

	#Turns the gps module off
    def stopGPS(self):
        if self.connected:
            self.ser.write("AT+CGPS=0")
            self.gpsOn = False

    # TODO, add parsing to just get lat and long
    def getLongLat(self):
		#Makes sure there is a serial connection, if not will connect
		while !self.connected:
			self.connect()
			time.sleep(2)
			
		#Makes sure gps is on, if not turns on
		while !self.gpsOn:
			self.startGPS()
			time.sleep(2)
		
        return getGPS()
	
	# Universal parser to parse AT command responses
	def parse_reply(self, message, seperator):
		msgList = message.split(seperator)
		
		return msgList
		
	
	
	
	
	
	
