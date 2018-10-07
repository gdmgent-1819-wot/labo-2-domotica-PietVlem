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
    r1s = db.reference('/room1/socket').get()
    r2l = db.reference('/room2/light').get()
    r2s = db.reference('/room2/socket').get()
    kil = db.reference('/kitchen/light').get()
    kis = db.reference('/kitchen/socket').get()
    kid = db.reference('/kichen/door').get()
    lrl = db.reference('/livingroom/light').get()
    lrs = db.reference('/livingroom/socket').get()
    lrd = db.reference('/livingroom/door').get()

    #color lights
    #room 1
    if r1l == true:
        sense.set_pixel(0, 2, 255, 255, 0)
    if r1s == true:
        sense.set_pixel(3, 0, 0, 0, 255)
    #room 2
    if r2l == true:
        sense.set_pixel(0, 6, 255, 255, 0)
    if r2s == true:
        sense.set_pixel(3, 7, 0, 0, 255)
    #kitchen
    if kil == true:
        sense.set_pixel(4, 2, 255, 255, 0)
    if kis == true:
        sense.set_pixel(7, 3, 0, 0, 255)
    if kid == true:
        sense.set_pixel(5, 0, 0, 255, 0)
        sense.set_pixel(6, 0, 0, 255, 0)
        sense.set_pixel(7, 0, 0, 255, 0)
    #living room
    if lrl == true:
        sense.set_pixel(4, 2, 255, 255, 0)
    if lrs == true:
        sense.set_pixel(7, 4, 0, 0, 255)
    if lrd == true:
        sense.set_pixel(5, 7, 255, 0, 0)
        sense.set_pixel(6, 7, 255, 0, 0)
        sense.set_pixel(7, 7, 255, 0, 0)

    #check every 3 seconds
    sleep(3)







