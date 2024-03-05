

#Good Code
# This first line is provided for you
hrs = input("Enter Hours:")
rate = input("Enter rate:")
Pay = int(hrs)*float(rate)
print("Pay:" , Pay)

# otro programita= condicional doble
hrs = input("Enter Hours:")
h = float(hrs)
tarifa = input("Enter rate")
t = float(tarifa)
if h <= 40:
   y = h*t
   print (y)
else: y = 40*t + (h-40)*t*1.5
print(y)

#otro programita: condicional multiple
score = input("Enter Score: ")
try:
    e = float(score)
except:
    print ("no es un numero")
if e > 1:
    print ("value out of range")
elif e >= 0.9 :
    print ("A")
elif e >= 0.8 :
    print ("B")
elif e >= 0.7 :
    print ("C")
elif e >= 0.6 :
    print ("D")
elif e < 0.6 :
    print ("F")

#funcion :
def computepay(h,r):
    m = (h-40)*0.5*r
    if h <=40:
        m =0
    j = h*r
    w = m + j
    return w

hrs = input("Enter Hours:")
tarifa = input("Enter rate")
h = float(hrs)
r = float(tarifa)
p = computepay(h,r)
print("Pay",p)

#comando semana 7
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        si = int(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = si
        
    elif si < smallest:
        smallest = si
        
    if largest is None:
        largest = si
            
    elif si > largest:
        largest = si

print("Maximum is", largest)
print("Minimum is", smallest)

#semana 1 curso 2
text = "X-DSPAM-Confidence:    0.8475"
data = text.find(":")
dataa = text.find("5")
dataaa = text[data + 1	:dataa + 1]
si= dataaa.strip() 
no =float(si)
print(no)

#semana 3
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fhh = fh.read()
fhhh =fhh.strip()
fhhhh = fhhh.upper()
    
print(fhhhh)
    
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    linee = line.rstrip ()
    print(linee.upper())

#semana 3 ejercicio 2
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
       line = float(line[21:])
       total = line + total    
average = total/ count
print("Average spam confidence:",average)
        
#semana 4 1
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    thing = line.split()
    for element in thing:
        if element in lst:
            continue
        else:
            lst.append(element)
    
lst.sort()
print(lst)


#semana 4 2

fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From"): continue
    if line.startswith("From:"): continue
    else:
        words = line.split()
        print (words[1])
    count = count + 1
	
print ("There were", count, "lines in the file with From as the first word")

fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    
    if line.startswith("From:"): continue
        
    elif  line.startswith("From"): 
    
        words = line.split()
        print (words[1])
    count = count + 1
	
print ("There were", count, "lines in the file with From as the first word")


#semana 5
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
lista = list()
for line in handle:
    line = line.rstrip()
    if line.startswith("From:"): continue
    elif line.startswith("From"):
        word = line.split()
        lista.append(word[1])
        #print (lista)        
for wordss in lista:
    dic[wordss] = dic.get(wordss,0) + 1
    
#print(dic)
bigcount = None
bigword = None
for key,value in dic.items(): 
    
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key

print (bigword,bigcount)

#semana 6
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1
        #print (line[0:2])

lst=list()        
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)