import RPi.GPIO as GPIO
from time import sleep 
from pyrebase import pyrebase
import time
import Adafruit_DHT
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#init DHT22
sensor = Adafruit_DHT.DHT22
pin = 4

#init MCP3008
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#init GPIO
GPIO.setmode(GPIO.BOARD)
sw_heater=16
sw_motor=18
GPIO.setup(sw_heater, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw_motor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#init Firebase Database
config = {
	"apiKey": "wPemlJJRGL0uscrLvZU4iVqaVxjzIKcr5cuLL5AC",
	"authDomain": "iotnodemcu.firebaseapp.com",
	"databaseURL": "https://iotnodemcu.firebaseio.com",
	"storageBucket": "iotnodemcu.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def stream_handler(message):
    onChange(message["path"], message["data"]) 

def onChange(key, value):
    if(key == "/HeaterStatus"):
    	print("heater status : " + value)
    elif(key == "/HeaterTimer"):
		print("heater timer : " + value)
    elif(key == "/Humidity"):
    	print("humidity : ", value)
    elif(key == "/Temperature"):
		print("temperature : ", value)
    elif(key == "/MotorMode"):
        print("motor mode : " + value)
    elif(key == "/MotorMode"):
		print("motor mode : " + value)
    elif(key == "/MotorDegree"):
		print("motor degree : " + value)   
	 	
db.stream(stream_handler)

def event_sw_heater(arg):
    if(GPIO.input(sw_heater)==0):
		db.child("/HeaterStatus").set("ON")
    else:
		db.child("/HeaterStatus").set("OFF")

def event_sw_motor(arg):
    if(GPIO.input(sw_motor)==0):
		db.child("/MotorMode").set("ON")
    else:
		db.child("/MotorMode").set("OFF")

GPIO.add_event_detect(sw_heater, GPIO.BOTH, event_sw_heater, bouncetime=50)
GPIO.add_event_detect(sw_motor, GPIO.BOTH, event_sw_motor, bouncetime=50)

while 1:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		db.child("/Temperature").set(float(format(temperature, ".2f")))
		db.child("/Humidity").set(float(format(humidity, ".2f")))
	else:
		print 'Failed to get reading. Try again!'
		
	sleep(1)

