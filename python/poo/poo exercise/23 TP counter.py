from collections import Counter
c = Counter() # compteur vide
print(c) # affiche: Counter()
c = Counter('programmation') #compteur avec un iterable
print(c) #affiche Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
c = Counter({'red': 4, 'blue': 2 }) # un compteur avec un mapping
print(c) #affcihe: Counter({'red': 4, 'blue': 2})
c = Counter(cats=4, dogs=8) #un compteur avec key=valeur
print(c) #affcihe: Counter({'dogs': 8, 'cats': 4})

c= Counter(['red','blue'])
print(c['green'])
c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements())) #affiche ['a', 'a', 'a', 'a', 'b', 'b']
c = Counter(a=4, b=2, e=10, c=0, d=-2)
print(c.most_common(2))
print(Counter('abracadabra').most_common(3)) #affiche [('a', 5), ('b', 2), ('r', 2)]

