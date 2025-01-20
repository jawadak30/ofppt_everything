thislist=[]
dernier=[]
n=int(input("saisir le nombre des employés: "))
for i in range(0,n) :
    a=str(input("saisir un nombre: "))
    thislist.append(a)
    if  i>n-6 and i<n :
        dernier.append(a)
print(thislist)
print(dernier)