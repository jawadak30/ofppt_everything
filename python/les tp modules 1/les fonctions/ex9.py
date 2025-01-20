def fonction(a):
    print(thislist)
    s=0
    r=0
    for val in thislist:
            print(val,"lindice est",i)
            if val%2==0:
                s=s+1
            else:
                 r=r+1
    l=[]
    for val in thislist:
        c=val*3
        l.append(c)
    print(l)
    print("la grande valeur est: ",max(thislist))
    print("la valeur minimale",min(thislist))
    print("le nombre des nombes pair est: ",s)
    print("le nombre des nombres impair est : ",r)
thislist=[]
for i in range(0,6):
    a=int(input("saisir un nombre: "))
    thislist.append(a)
fonction(a)