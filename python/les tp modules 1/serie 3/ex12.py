a=int(input("saisir un nombre: "))
s=0
for i in range(1,a):
    if a%i==0 :
       s=s+i
if a==s :
    print(a,"est un nombre parfait")
else :
    print(a,"non pas un nombre parfait")
