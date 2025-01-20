def double(n):
    for val in thislist:
        l=[]
        if val not in l:
            l.append(val)
        return(l)
thislist=[]
for i in range(0,5):
    n=int(input("saisir un nombre: "))
    thislist.append(n)
print("les valeurs sont",double(n))