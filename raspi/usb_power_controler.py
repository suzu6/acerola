# -*- coding: utf-8

from firebase import firebase
import subprocess
import time

device = 'A1'

# Initialize the app with a service account, granting admin privileges
firebase = firebase.FirebaseApplication(
    'https://acerola-4cf84.firebaseio.com',
    None
)

target = firebase.get('/setting/'+device, None)


try:
    while True:
        turnon = firebase.get('/devices/'+target+'/power', None)
        print target, turnon

        if turnon:
            subprocess.call(["sh", "/home/pi/acerola/raspi/usb_turn_on.sh"])
        else:
            subprocess.call(["sh", "/home/pi/acerola/raspi/usb_turn_off.sh"])
        # interval
        sleep = firebase.get('/devices/'+target+'/catch_interval', None)
        time.sleep(sleep)

except:
    print 'has error'

subprocess.call(["sh", "/home/pi/acerola/raspi/run_usb.sh"])