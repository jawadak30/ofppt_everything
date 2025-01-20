x=()
y=[]
n=int(input("saisir le nombre des nombres: "))
for i in range(0,n) :
    a=int(input("saisir une valeur: "))
    y.append(a)
    x=tuple(y)
    print(x)
    if i>=0 and i<=3 :
       print(x)
    if i>=n-4 and i<n :
       print(x)