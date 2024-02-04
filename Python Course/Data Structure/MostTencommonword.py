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
        print(counts, word)
lst = list()

for k, v in counts.items(): # become dictionary in a list of tuples
    newtup = (v, k) # change the order between key and value
    lst.append(newtup) # add each tuple to the list

lst = sorted(lst, reverse=True) # sort the list of tuple in descending order
for val, key in lst[:10]: # looop throught the first 10 tuples
    print(key, val) # print the first 10 tuples
