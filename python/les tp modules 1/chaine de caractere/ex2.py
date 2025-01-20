a=input("write something: ")
def fonctio(a):
    thislist=[]
    for s in a:
        for i in s:
            s=i+"*"
            thislist.append(s)
    return(thislist)
print(fonctio(a))