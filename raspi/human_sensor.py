#!/usr/bin/python
# -*- coding: utf-8

from firebase import firebase
from datetime import datetime, timedelta
import RPi.GPIO as GPIO  # importing the RPi.GPIO module
import time  # importing the time module

GPIO.cleanup()  # to clean up at the end of your script
motion_pin = 18  # select the pin for the motion sensor
led_pin = 11

# Initialize the app with a service account, granting admin privileges
firebase = firebase.FirebaseApplication(
    'https://acerola-4cf84.firebaseio.com',
    None
)

# 'fan' or 'light'
target = 'light'
url = '/measure/' + target

# initilarize
firebase.delete('/measure', target)
firebase.put('', '/measure', target)


GPIO.setmode(GPIO.BCM)  # to specify which pin numbering system
GPIO.setwarnings(False)  
GPIO.setup(motion_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
print "-----------------------------------------------------------------------"

# FIFO
que = []
stock_num = 10

while True:
    value = GPIO.input(motion_pin)
    now = datetime.now() + timedelta(hours=9)
    key = now.strftime('%Y-%m-%d %H:%M:%S')
    # only temp
    data = {'t': key, 'y': value}

    if value != 0:
        GPIO.output(led_pin, True)
    else:
        GPIO.output(led_pin, False)

    print 'post ', data
    result = firebase.post(url, data)
    que.append(result['name'])

    if len(que) > stock_num:
        # stock数以下のデータを削除
        key = que.pop(0)
        result = firebase.delete(url, key)
        print 'delete ', result

    sampling_interval = firebase.get(
        '/devices/'+target+'/sampling_interval', None)
    print 'sampling_interval', sampling_interval
    time.sleep(sampling_interval)

GPIO.cleanup()
