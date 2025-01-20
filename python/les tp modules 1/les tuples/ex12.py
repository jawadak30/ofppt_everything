thislist=[]
y=()
b=int(input("saisir la position pour supprime l'element de la liste: "))
for i in range(0,6) :
    a=int(input("saisir un nombre: "))
    thislist.append(a)
    print(thislist)
    if i==b :
        del thislist[i]
y=tuple(thislist)
print(y)