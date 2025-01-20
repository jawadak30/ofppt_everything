class Film:
    def __init__(self,titre,réalisateur):
        self.titre=titre
        self.réalisateur=réalisateur
    def afficher(self):
        print("titre",self.titre,"réalisateur",self.réalisateur)
    def __str__(self):
        return("titre"+self.titre+"réalisateur"+self.réalisateur)
class Acteur:
    def __init__(self,id,nom):
        self.id=id
        self.nom=nom
        self.lsfilm=[]
    def afficher(self):
        print("id ",self.id,"nom",self.nom)
        for ls in self.lsfilm:
            
            ls.afficher()
    def ajouter(self):
        nbr=int(input("donner le nombre de film: "))
        for i in range(nbr):
            titre=input("titre de film: ")
            réalisateur=input("realisateur de film: ")
            f=Film(titre,réalisateur)
            self.lsfilm.append(f)
act1=Acteur(1,"nom")
act1.afficher()