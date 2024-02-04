
stuff = 'hello \n world'
print(stuff)

# \n New line it is a character, it count in len() function

xfile = open('Text.txt', 'r')
count = 0
words = 0

for line in xfile:
    count = count + 1
    print(count)
    print(line)
    words = words + len(line.split())
    print(words)
    list.append(line)
    print(list) 

R= xfile.read()
print(len(R))

# we can get a list of keys and values or item (both) from a dictionary
# dictionary methods .keys() and.values() , items(), 
# two iteration variables for key,valuer in dictionary.items()

name = input('Enter file: ')
try:
    handle = open(name, 'r')
except FileNotFoundError:
    print('File not found')
    exit()
counts = dict()
# loop for read each line 
for line in handle:
    words = line.split() #split() returns a list of strings, becomes each line in a list of each word
    #print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        print(counts, word)

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

#Spaces and \n count in len() function '''

