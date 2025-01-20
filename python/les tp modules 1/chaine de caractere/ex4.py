a=input("write something: ")
def fonction(a):
    s=0
    for val in a:
        if val in ["a","e","i","o","y","u"]:
           s=s+1
    return(s)
print(fonction(a))