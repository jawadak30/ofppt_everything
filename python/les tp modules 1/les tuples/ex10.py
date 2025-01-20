thislist=[]
y=()
for i in range(0,6) :
    b=int(input("saisir une valeur: "))
    thislist.append(b)
a=int(input("saisir l'element pour afficher s'il,existe dans un tuple"))
if a in thislist :
    print("existe")
else :
    print("n'existe pas ")
y=tuple(thislist)
print(y)
