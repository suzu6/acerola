# -*- coding: utf-8

from firebase import firebase
import RPi.GPIO as GPIO
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

GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM)  # GPIOへアクセスする番号をBCMの番号で指定することを宣言します。
GPIO.setup(14, GPIO.IN)  # BCMの15番ピン、物理的には10番ピンを出力に設定します。


try:
    while True:
        time.sleep(5)

        now = datetime.now() + timedelta(hours=9)
        key = now.strftime('%Y-%m-%d %H:%M:%S')
        value = GPIO.input(14)

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
