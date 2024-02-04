# tuples are like list but they are unmutable and can't be changed and insted of braces the use parenthesis., it behave like a string in tha case.
#tuples can assign tuples values on left hand side of an assigment statement
# (x, y) = (1, 'fred') or (a, b) = (2, 2)
# we can get a tuple from a dictionary using the method .items() it returns a list of tuples

d = {'a': 1, 'c': 10, 'b': 7}

for key, value in sorted(d.items()): # this code will print the key and the value of the dictionary ordered by the keys
    print(key, value)

# How do we sort by values 
tmp = list()
for k, v in d.items():
    #print(v, k)
    tmp.append((v, k))
    print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)