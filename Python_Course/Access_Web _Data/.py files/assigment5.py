import json
import urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = input('enter:') # https://py4e-data.dr-chuck.net/comments_42.json ,  https://py4e-data.dr-chuck.net/comments_1965936.json

uh = urllib.request.urlopen(data, context=ctx)
#print('uh' , type(uh)) # <class 'http.client.HTTPResponse'>
url = uh.read().decode()
#print('url' , type(url)) # url <class 'str'>

info = json.loads(url) #info <class 'dict'>
#print('info', type(info)) # info <class 'dict'>

c=0
#print("info['comments']" , type(info['comments'])) # info['comments'] <class 'list'>
# for i in info['comments']:
#     c += i['count']

inf = info['comments'] #list of dictionaries
print(inf)
for i in inf:
    c += i['count']

print(c)
    