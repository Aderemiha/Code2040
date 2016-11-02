import urllib2
import urllib
import sys


url = 'http://challenge.code2040.org/api/reverse' 
keys = urllib.urlencode({        #post the url and keys to the api
  'token': '19ced7d67c5290c1f46ee277fae43616',
  'github': 'https://github.com/Aderemiha/Code2040.git'
})
response = urllib2.urlopen(url, keys).read() #read the response
print(response)
reverse = "".join(reversed(response)) #reverse the response
print(reverse)
urlReverse = 'http://challenge.code2040.org/api/reverse/validate'
params = urllib.urlencode({
    'token': '19ced7d67c5290c1f46ee277fae43616',
    'string': reverse
    })
answer = urllib2.urlopen(urlReverse, params).read() #read the response
print(answer)
