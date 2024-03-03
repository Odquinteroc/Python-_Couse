import xml.etree.ElementTree as ET
import urllib.parse, urllib.error
from urllib.request import urlopen

url = 'https://py4e-data.dr-chuck.net/comments_42.xml'
u = 'https://py4e-data.dr-chuck.net/comments_1965935.xml'
response = urllib.request.urlopen(u) #type class http.client.HTTPResponse'>
#print('response',type(response))
xml_data = response.read() #type bytes
#print('xml_data',type(xml_data))

stuff = ET.fromstring(xml_data) # class 'xml.etree.ElementTree.Element
#print('stuff',type(stuff))
lst = stuff.findall('comments/comment') #list of bytes
#print(lst)
suma = 0
lista =[]
for i in lst:
    a = i.find('count').text #this fount the tag count and convertit from bytes to strings
    print(a)
    lista.append(int(a))
c = sum(lista)

print(c)
    
# for item in lst:
#      a = item.find('count').text
#      b = int(a)
#      suma += b
# print(suma)



