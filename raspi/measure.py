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

sampling_interval = firebase.get('/devices/'+target+'/sampling_interval', None)
print 'sampling_interval', sampling_interval


# FIFO
que = []
stock_num = 10

try:
    while True:
        time.sleep(5)

        now = datetime.now() + timedelta(hours=9)
        key = now.strftime('%Y-%m-%d %H:%M:%S')
        value = readData()

        result = firebase.post(url, {key: value})
        print 'post ', result

        que.append(result['name'])
        if len(que) > stock_num:
            # stock数以下のデータを削除
            key = que.pop(0)
            result = firebase.delete(url, key)
            print 'delete ', result

except KeyboardInterrupt:
    GPIO.cleanup()
