from collections import OrderedDict
d=OrderedDict()
d['a']='1' #remplir d
d['b']='2'
d['c']='3'
d['d']='4'
print(d)
d.move_to_end('b')
print(d) #affiche OrderedDict([('a', '1'), ('c', '3'), ('d', '4'), ('b', '2')])
d.move_to_end('b',last=False)
print(d) #affiche OrderedDict([('b', '2'), ('a', '1'), ('c', '3'), ('d', '4')])
print(d.popitem(True)) #affiche ('d', '4')
print(d) #affiche OrderedDict([('b', '2'), ('a', '1'), ('c', '3')])
