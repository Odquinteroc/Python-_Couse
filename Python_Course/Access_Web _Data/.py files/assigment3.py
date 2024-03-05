import urllib.parse, urllib.error
from bs4 import BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ') # https://py4e-data.dr-chuck.net/known_by_Fikret.html , https://py4e-data.dr-chuck.net/known_by_J.html
a = int(input('Enter count: '))
Line = int(input('Enter position: '))

print('retriving:', url)

cn= 0
while cn < a:
    cn +=1
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    all_a_tags = soup.find_all('a')
    third_a_tag = all_a_tags[Line - 1]
    print('retriving:', str(third_a_tag.get('href', None)))
    url = str(third_a_tag.get('href', None))





# for i in range(0, a):
#     html = urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, "html.parser")
#     tags = soup('a')
#     count = 0

#     for tag in tags:
#         count+=1
#         if count == Line:
#             print('retriving:', str(tag.get('href', None)))
#             url = str(tag.get('href', None))
#             count = 0
#             break

    

