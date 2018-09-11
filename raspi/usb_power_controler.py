# -*- coding: utf-8

from firebase import firebase
import subprocess
import time

counter = 0
turnon = True

# Initialize the app with a service account, granting admin privileges
firebase = firebase.FirebaseApplication(
    'https://acerola-4cf84.firebaseio.com',
    None
)

target = firebase.get('/setting/A1', None)


while True:
    turnon = firebase.get('/devices/light/power', None)
    print turnon

    if turnon:
        subprocess.call(["sh", "/home/pi/acerola/raspi/usb_turn_on.sh"])
    else:
        subprocess.call(["sh", "/home/pi/acerola/raspi/usb_turn_off.sh"])
    # interval
    sleep = firebase.get('/devices/light/catch_interval', None)
    time.sleep(sleep)
