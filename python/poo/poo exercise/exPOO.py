class Adrese:
    def __init__(self,rue,ville):
        self.rue=rue
        self.ville=ville
    def afficher(self):
        print("rue",self.rue,"ville",self.ville)
    def __str__(self):
        return("rue"+self.rue+"ville"+self.ville)
class Personne:
    def __init__(self,code,nom,adresse):
        self.code=code
        self.nom=nom
        self.adresse=adresse
    def afficher(self):
        print("code",self.code,"nom",self.nom,)
        self.adresse.afficher
    def __str__(self):
        ad=self.adresse.__str__()
        return "code"+self.code+" ,nom: "+self.nom+" ,adresse:"+ad
a=Adrese("c1","V1")
p=Personne("1","n1",a)
p.afficher()
print(p)
thislsit=[]
c=int(input("saisir un nombre: "))
for i in range(c):
    code=input("donner la code: ")
    nom=input("donner le nom: ")
    prenom=input("donner le prenom: ")
    p=Personne(code,nom,prenom)
    thislsit.append(p)
for p in thislsit:
    print(p)