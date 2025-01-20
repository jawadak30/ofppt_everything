a=int(input("saisir un nombre: "))
m=a
inverse=0
while a!=0 :
    inverse=(inverse*10)+(a%10)
    a=a/10
if m==inverse :
    print(m,"est un nombre palindrome ")
else : 
    print(m,"n'est pas un nombre palindrome")