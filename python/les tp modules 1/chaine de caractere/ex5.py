
def number(a):
    thislist=[]
    for val in a:
        if val.isnumeric():
            thislist.append(val)
    return(thislist)
print(number("python 3 sortie en 2008 "))