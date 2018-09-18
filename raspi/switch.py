#!/usr/bin/python
# -*- coding: utf-8

from firebase import firebase
import subprocess
import time
import RPi.GPIO as GPIO  # importing the RPi.GPIO module

device = 'A1'

GPIO.cleanup()  # to clean up at the end of your script
motion_pin = 15
led_pin = 14

GPIO.setmode(GPIO.BCM)  # to specify which pin numbering system
GPIO.setwarnings(False)
GPIO.setup(motion_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)


# Initialize the app with a service account, granting admin privileges
firebase = firebase.FirebaseApplication(
    'https://acerola-4cf84.firebaseio.com',
    None
)

target = firebase.get('/setting/'+device, None)

# 押下時にTrue、押されていない時はFalse
done = False

# try:
while True:
    # スイッチを押した時、状態をトグルする
    # interval
    time.sleep(1)

    value = GPIO.input(motion_pin)
    print target, value, GPIO.HIGH

    if value == GPIO.HIGH and not done:
        # switch on and not toggle power yet
        turnon = firebase.get('/devices/'+target+'/power', None)
        # 反転
        turnon = not turnon
        GPIO.output(led_pin, turnon)
        turnon = firebase.put('', '/devices/'+target+'/power', turnon)
        done = True
        print target + ' is turn ' + 'on' if turnon else 'off'
    else:
        # switch off or done toggle power
        done = False

# except:
#     print 'has error'

# subprocess.call(["sh", "/home/pi/acerola/raspi/run_usb.sh"])
