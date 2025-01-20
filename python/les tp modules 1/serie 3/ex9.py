a=int(input("saisir un nombre: "))
if a%2==0 :
     print(a,"n'est pas nombre premier")
elif a%1==0 :
   if a%a==0 :
       print(a,"est un nombre premier")