import json
import urllib
import requests
import sys
import re
import numpy as np

payload = {'token':'19ced7d67c5290c1f46ee277fae43616', 'github': 'https://github.com/Aderemiha/Code2040.git'}
r = requests.post('http://challenge.code2040.org/api/prefix', data = payload)   ##post the payload to the API
print(r.text)
response = json.loads(r.text)
prefix = response["prefix"] ##get the prefix
array  = response["array"]  ##get the array
print("prefix:")
print(prefix)
print("array:")
print(array)

finalArray = []                             ##get rid of the words with the prefix
for n in range(0, len(array)):
    if(not array[n].startswith(prefix)):
        finalArray.append(array[n])

print("final array:")
print(finalArray)


payload = {'token':'19ced7d67c5290c1f46ee277fae43616', 'array': finalArray}


result = requests.post('http://challenge.code2040.org/api/prefix/validate', json = payload) ##post the final array to the API

print(result.text)
