name = input('Enter file: ')
try:
    handle = open(name, 'r')
except FileNotFoundError:
    print('File not found')
    exit()
counts = dict()
for line in handle: # read each line in the file
    words = line.split() # split each line in list of each words
    for word in words: # go through each word in the list
        counts[word] = counts.get(word, 0) + 1 # count each word and add it to the dictionary 
        #print(counts, word)
lst = list()

print(sorted([(v, k) for k, v in counts.items()], reverse=True))