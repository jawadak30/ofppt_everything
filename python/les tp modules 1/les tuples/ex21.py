thislist=[(10, 20, 100),(40, 50, 100),(70, 80, 100)]
l=[]
x=list(thislist[0])
y=list(thislist[1])
z=list(thislist[2])
for i in range(1,2) :
    x.insert(3,100)
    del x[2]
    y.insert(3,100)
    del y[2]
    z.insert(3,100)
    del z[2]
a=tuple(x)
b=tuple(y)
c=tuple(z)
l.append(a)
l.append(b)
l.append(c)
print(l)