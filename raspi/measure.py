#!/usr/bin/python
# -*- coding: utf-8

from firebase import firebase
from bme280_sample import readData
from datetime import datetime, timedelta
import time

counter = 0
turnon = True

# Initialize the app with a service account, granting admin privileges
firebase = firebase.FirebaseApplication(
    'https://acerola-4cf84.firebaseio.com',
    None
)

# 'fan' or 'light'
target = 'fan'
url = '/measure/' + target

# initilarize
firebase.delete('/measure', target)
firebase.put('', '/measure', target)


# FIFO
que = []
stock_num = 10

while True:
    now = datetime.now() + timedelta(hours=9)
    key = now.strftime('%Y-%m-%d %H:%M:%S')
    # only temp
    value = readData()[0]['value']
    data = {'t': key, 'y': value}

    result = firebase.post(url, data)
    print 'post ', result

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
