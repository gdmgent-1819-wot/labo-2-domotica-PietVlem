from time import sleep
from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#firebase init
cred = credentials.Certificate("smarthome-7fe68-firebase-adminsdk-v7wa9-6208f8722d.json.json")
firebase = firebase_admin.initialize_app(cred,{'databaseURL':'https://smarthome-7fe68.firebaseio.com'})

#init sensehat
sense = SenseHat()

while True:
    #clear lights
    sense.clear()

    #import firebase vars
    r1l = db.reference('/room1/light').get()

    #color lights
    if r1l == true:
        sense.set_pixel(0, 2, 255, 255, 0)

    #check every 3 seconds
    sleep(3)







