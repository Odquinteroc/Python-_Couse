name = input('Enter file: ')
try:
    handle = open(name, 'r')
except:
    print('File not found')
    exit()

for line in handle:
    words = line.split()
    print(words)
   # print(line)