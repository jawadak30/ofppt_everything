print("pour stoperr la saisie des nombres tape r 0")
a=int(input("saisir un nombre: "))
s=a
i=0
while a!=0 :
    a=int(input("saisir un nombre: "))
    s=s+a
    i=i+1
print(i)    
m=s//i
print("la somme est: ",s)
print("la moyenne est: ",m)