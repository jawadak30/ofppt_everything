def Conversion(n):
    s=0
    while n/10!=0 :
        s=s+(n%10)
    return(s)
n=int(input("saisir un nombre: "))
Conversion(n)
print(Conversion,"la conversion est: ",s)