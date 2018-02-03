import copy

a = [11, 22, 33]
b = [44, 55, 66]

c = [a, b]

e = copy.deepcopy(c)
f = copy.copy(c)

a.append(77)

print(c)
print(e)
print(f)






