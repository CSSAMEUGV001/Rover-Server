import serial

class gps:
    DEFAULT_SERIAL_PATH = 'dev/ttyUSB0'

    def __init__(self, serial_port = DEFAULT_SERIAL_PATH, baud = 9600):
        self.port = serial_port
        self.baud = baud

        self.gpsOn = False

        if msg == "OK"
            print "Connected"
            self.connected = True
        else
            print "OK Not returned"
            self.connected = False

    def connect(self):
        self.ser = serial.Serial(serial_path, baud)
        while msg != "OK"
            self.ser.write("at\n")
            msg = self.ser.readline()
        print "Connected to module, OK received"

    def getGPS(self):
        if(self.connected == True and self.gpsOn == True)
            self.ser.write("At+CGPSINFO")
            msg = self.ser.readline()
            return msg

    def startGPS(self):
        if self.connected == True:
            while self.gpsOn == False:
                self.ser.write("AT+CGPS=1")
                msg = self.ser.readline()
                if msg == "OK"
                    self.gpsOn = True

    def stopGPS(self):
        if self.connected:
            self.ser.write("AT+CGPS=0")
            self.gpsOn = False

    # TODO, add parsing to just get lat and long
    def getLongLat(self):
        if(self.connected and self.gpsOn)
            getGPS
