from pyrebase import pyrebase
import time

config = {
	"apiKey": "wPemlJJRGL0uscrLvZU4iVqaVxjzIKcr5cuLL5AC",
	"authDomain": "iotnodemcu.firebaseapp.com",
	"databaseURL": "https://iotnodemcu.firebaseio.com",
	"storageBucket": "iotnodemcu.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_handler(message):
     print(message["path"])
     print(message["data"]) 

db.stream(stream_handler)

while 1:
	time.sleep(1)
	print("firebase run")

