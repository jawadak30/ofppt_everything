b=()
c=()
x=()
y=[]
for i in range(0,10) :
    a=int(input("saisir un valeur"))
    if i<3 :
        y.append(a)
        x=tuple(y)
    print(x)
    if i<6 and i>=3 :
        y.append(a)
        b=tuple(y)
    print(b)
    if i>=6 :
        y.append(a)
        c=tuple(y)
    print(c)
    