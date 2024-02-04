looking = None
print('before', looking)
for i in [12,23,33,4,15,6,97,86,9,10]:
    if looking == None:
        looking = i
    elif i < looking :
        looking = i
    print(looking, i)
print('after', looking)



# Ctrl + Shift + L (Change the name of all variables)