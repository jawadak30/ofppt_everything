
thislist=[]
multiple=[]
somme=0
for i in range(0,6) :
    a=int(input("saisir un nombre: "))
    thislist.append(a)
    print(thislist[i],"sont index est: ",i+1)
    somme=somme+thislist[i]
print(thislist)
print("la somme est: ",somme)
print("la plus grand nombre est: ",max(thislist))
print("la valeur plud petite est: ",min(thislist))
s=0
r=0
for i in range(0,6) :
    t=thislist[i]*3
    multiple.append(t)
    if thislist[i]%2==0 :
        s=s+1
    else :
        r=r+1
print("le nombre des nombres pair dans la liste est: ",s)
print("le nombre des nombres impair dans la liste est: ",r)
print("la multiple est: ",multiple)