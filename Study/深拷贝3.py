from copy import *

a = [11, 22]
b = [33, 44]

c = (a, b)

e = deepcopy(c)
f = copy(c)

print(id(c))
print(id(e))
print(id(f))

b.append(55)

print(e)
print(f)



