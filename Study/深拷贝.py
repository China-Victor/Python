import copy

a = [11, 22, 33]

b = copy.deepcopy(a)

print(id(a))
print(id(b))

a.append(44)

print(a)
print(b)

c = (11, 22, 33)

e = copy.deepcopy(c)
print(id(c))
print(id(e))








