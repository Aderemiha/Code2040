import json
import urllib
import requests
import sys
import re
import dateutil.parser
import datetime
import time
from datetime import timedelta

payload = {'token':'19ced7d67c5290c1f46ee277fae43616', 'github': 'https://github.com/Aderemiha/Code2040.git'}
r = requests.post('http://challenge.code2040.org/api/dating', data = payload)   ##post the payload to the API
print(r.text)


response = json.loads(r.text) 
 
dateString = response["datestamp"] #get date
secString = response["interval"] #get the seconds interval

secondsToAdd = timedelta(seconds = secString) #convert secString to seconds
theDate = dateutil.parser.parse(dateString) #convert dateString to date
finalTime = theDate + secondsToAdd #add the date and seconds to get the new date

finalTime = finalTime.replace(tzinfo=None) #remove the timezone
 
finalTime = finalTime.isoformat() + 'Z' #format it back into ISO time

print(finalTime)

payload = {'token':'19ced7d67c5290c1f46ee277fae43616', 'datestamp': finalTime}  #post the new
result = requests.post('http://challenge.code2040.org/api/dating/validate', data = payload)
print(result.text)
