from time import sleep 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=16
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def event_sw_heater(arg):
    if(GPIO.input(button1)==0):
	print("On")
    else:
	print("Off")
	
GPIO.add_event_detect(button1, GPIO.BOTH, event_sw_heater, bouncetime=50)

while 1:
	sleep(1)
	print("start")
	
