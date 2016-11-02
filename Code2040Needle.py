import urllib2
import urllib
import sys
import re

##get needle and haystack from API
url = 'http://challenge.code2040.org/api/haystack'
keys = urllib.urlencode({
  'token': '19ced7d67c5290c1f46ee277fae43616',
  'github': 'https://github.com/Aderemiha/Code2040.git'
})
response = urllib2.urlopen(url, keys).read()

## find needle in haystack
needleSplit = response.split(',"haystack":')[0]
haystackSplit = response.split(',"haystack":')[1]

print(response)
needle = needleSplit.split(':')[1]

haystackReg = "\"[a-z]+\""

haystack = re.findall(haystackReg, haystackSplit)

for n in range(0,len(haystack)):
    if(haystack[n] == needle):
        index = n
        
##return Index
urlNeedle = 'http://challenge.code2040.org/api/haystack/validate'
params = urllib.urlencode({
    'token': '19ced7d67c5290c1f46ee277fae43616',
    'needle': index
   })
answer = urllib2.urlopen(urlNeedle, params).read()
print(answer)
