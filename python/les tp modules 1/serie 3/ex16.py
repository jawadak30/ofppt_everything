print("poiur stoper la saisie des nombres taper 0")
a=int(input("saisir un nompbre: "))
grand=a
min=a
s=a
i=0
while a>0 :
    a=int(input("saisir un nombre: "))
    i=i+1
    somme=s+a
    moyenneAri=somme/i
    if a>grand:
      grand=a
    if a<min :
      min=a
    moyenneMauvise=(grand+min)/2
    print("la moyenne arithmitique est: ",moyenneAri)
    print("la moyenne mauvise est: ",moyenneMauvise)
    if moyenneMauvise>moyenneAri :
        print("la maileur moyenne est: ",moyenneMauvise)
    else :
        print("la maileur moyenne est: ",moyenneAri)