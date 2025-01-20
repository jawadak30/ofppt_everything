from collections import ChainMap
x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}
z = {'a':3, 'c':10}
c = ChainMap(y, x,z)
print(c)
for k, v in c.items(): #parcourir les éléments de c
    print(k, v)
