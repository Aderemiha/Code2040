import urllib
import urllib2

url = 'http://challenge.code2040.org/api/register'
keys = urllib.urlencode({                               #post the url and keys to the api
  'token': '19ced7d67c5290c1f46ee277fae43616',
  'github': 'https://github.com/Aderemiha/Code2040.git'
})
response = urllib2.urlopen(url, keys).read()    #read the response
print(response)
