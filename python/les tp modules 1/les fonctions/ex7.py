def dupliqe(thislist):
    l=[]
    for i in thislist:
        if i in thislist:
            l.append(i)
    return(l)
thislist = []
for i in range(0,6):
    a=int(input("saiisr un nombre: "))
    thislist.append(a)
print("les nombres dupliqués sont: ",dupliqe(thislist))