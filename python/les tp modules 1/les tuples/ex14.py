thislist=[]
y=()
a=int(input("saisir le nombre pour trouver l'indice: "))
for i in range(0,6) :
    a=int(input("saisir un nombre : "))
    thislist.append(a)
    c=0
    if a==thislist[i] :
        s=c+i
        print("lindice de nombre est: ",s)
    else :
        print("ce nombre n'existe pas")
y=tuple(thislist)
print(y)