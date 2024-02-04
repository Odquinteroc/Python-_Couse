import re #import regular expression library

hand = open('text1.txt')
for line in hand:
    line.rstrip()
    if re.search('For example', line): # Search "for example"
        print(line)

for line in hand:
    line.rstrip()
    if re.search('^Before', line): #Search "Before" at begin of the line
        print(line)

# "^X.*:" start the line with "X", folow by any character ".",  folow by "*" many times, follow by a ":"
# "^X-\S+:" start the line with "X-", match any non-whitespaces character "\S",  folow by one or more times "+", follow by a ":"
        
#re.search returns a True/False
#re.findall returns a list of the posible matches

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x) # [0-9]+ one or more digits  output ['2', '19', '42']
print(y)
y = re.findall('[AEIOU]+', x) # [AEIOU]+ one or more uppercase vowel characters

    
s = 'From: using the : character'
d = re.findall('^F.+:', s) # ouput ['From: using the :'] becasue it still searching for the last ":"
print(d)

sq = 'From: using the : character'
dq = re.findall('^F.+?:', sq) # ^F.+?: the "?2 means no be greedy ouput ['From:']
print(dq)

qw= 'From oscar@gmail.com sat jan 5 09:14:16 2008'
qe = re.findall('^From (\S+@\S+)', qw) # the extract part is inside of the parenthesis
print (qe)
#Without regular expression the double split patterns 

QWE = qw.split()
email = QWE[1]
pieces = email.split('@') # Output gmail.com, Takes the lines and splits then takes the second index and split again using "@" as parameter 
print (pieces[1]) #

# The regex version
l = re.findall('@([^ ]*)', qw)
ll = re.findall('^From .*@([^ ]*)', qw) ## find "@" follow by some number no blank characters
print(l) # Output ['gmail.com']
print(ll)

#Escape character
er = 'we just recived $10.00 for cookies.'
df = re.findall('\$[0-9.]+', er)
print(df)