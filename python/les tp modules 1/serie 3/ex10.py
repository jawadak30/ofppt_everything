print("pour steper la saisie des nombre taper un nomnre <=0 ")
a=int(input("saisir un nombre: "))
s=0
grand=a
min=a
i=0
while a>0 :
    if a>grand:
        grand=a
    if a<min :
        min=a
    s=s+a
    i=i+1
    a=int(input("saisir un nombre: "))
m=s/i
print(min,"est la plus petite valeur")
print(grand,"est la blue grand nombre")
print("la somme est: ",s)
print("la moyenne est: ",m)

