# Types matters
#Python knows what types everythings is 

A = "Writing programs (or programming) is a very creative and rewarding activity"
B = [1,2,3,4,5]
C = 87
D = 58.5
E = b'hola'
EE = memoryview(E)
EEE = bytes
EEEE = bytearray(b'hello world')
F = {"key": 15, "key1":"value"}
G = (5,15, "hello world")
H = True
I = None
J = 15
K = {"Hello", "world"}

print('A', type(A), A) 
print('B', type(B), B)
print('C', type(C), C)
print('D', type(D), D)
print('E', type(E), E)
print('EE', type(EE), EE)
print('EEE', type(EEE), EEE)
print('EEEE', type(EEEE), EEE)
print('F', type(F), F)
print('G', type(G), G)
print('H', type(H), H)
print('I', type(I), I)
print('J', type(J), J)
print('K', type(K), K)
