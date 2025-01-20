print("if you need to stop write 0")
a=int(input("saisir un nombre: "))
s=a
i=0
while a!=0 :
    somme=a+s
    i=i+1
    moyenne=somme/i
    a=int(input("saisir un nombre: "))
print("la somme est: ",somme)
print("la moyenne est: ",moyenne)