n=int(input("saisir la position: "))
a=int(input("saisir l'element pour l'ajoute dand le tuple: "))
r=int(input("saisir la nombre des nombres : "))
x=()
y=[]
c=int(input("saisr une valeur: "))
for i in range(0,r+2) :
    if i==n :
       y.insert(n,a)
    y.append(c)
    x=tuple(y)
    c=int(input("saisr une valeur: "))
print(x)