import re
x = open('text2.txt')
h =[]
for line in x:
    line.rstrip()
    y = re.findall('[0-9]+', line)
    if len(y) < 1 :continue
    for i in y:
        h.append(int(i))
m = sum(h)
print(m)


#  print( sum( [ for line in x: line.rstrip() ('[0-9]+',**************************.read()) ] ) )