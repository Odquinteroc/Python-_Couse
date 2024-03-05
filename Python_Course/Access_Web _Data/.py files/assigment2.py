from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #https://py4e-data.dr-chuck.net/comments_42.html , https://py4e-data.dr-chuck.net/comments_1965933.html
html = urlopen(url, context=ctx).read() # <class 'bytes'>
#print('html: ', type(html))
soup = BeautifulSoup(html, "html.parser") # <class 'bs4.BeautifulSoup'>
#print('soup: ', type(soup)) # <class 'bs4.BeautifulSoup'>

# Retrieve all of the anchor tags
tags = soup('span') # <class 'bs4.element.ResultSet'>
#print('tags: ', type(tags))
suma = 0
for tag in tags:
    #print(type(tag))#<class 'bs4.element.Tag'>
    #print(tag.contents) # <class 'list'>
    suma += int(tag.contents[0])
    print('Contents:', tag.contents[0])
print(suma)

