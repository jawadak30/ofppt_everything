l=[(4,1),(2,5),(2,'test'),(3,6),(1,'bonjour')]
nl=[]
for i,n in l:
    nl.extend((n,)*i)
print(nl)