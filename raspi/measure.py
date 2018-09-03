# -*- coding: utf-8

from firebase import firebase
from datetime import datetime, timedelta
import time

counter = 0
turnon = True

# Initialize the app with a service account, granting admin privileges
firebase = firebase.FirebaseApplication(
    'https://acerola-4cf84.firebaseio.com',
    None
)

url = '/measure/fan'

firebase.delete('/measure', 'fan')
firebase.put('', '/measure', 'fan')

arr = []

while counter < 20:
	time.sleep(5)
	value = counter * 3
	now = datetime.now() + timedelta(hours=9)
	
	key = now.strftime('%Y-%m-%d %H:%M:%S')
	result = firebase.post(url, {key: value})
	print 'post ', result

	arr.append(result['name'])
	if len(arr) > 10:
		print arr
		key = arr.pop(0)
		result = firebase.delete(url, key)
		print 'delete ', result
	counter += 1
