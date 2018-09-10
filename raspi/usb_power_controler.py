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

while counter < 10:
    
    turnon = firebase.get('/devices/light/power', None)
    print turnon

    if turnon:
        subprocess.call(["sh", "./usb_turn_on.sh"])
    else:
        subprocess.call(["sh", "./usb_turn_off.sh"])
    time.sleep(5)
    counter += 1
