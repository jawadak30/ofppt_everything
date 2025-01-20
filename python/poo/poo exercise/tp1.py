class voiture:
    def __init__(self,matricule,marque,anné):
        self.matricule = matricule
        self.marque = marque
        self.anné = anné
    def afficher(self):
        print("matricule: ",self.matricule,"marque: ",self.marque,"anné: ",self.anné)
    def __str__(self):
        return("matricule "+self.matricule+"marque "+self.marque+"anné "+self.anné)
class conducteur:
    def __init__(self,ID,nom,voitures):
        self.ID=ID
        self.nom=nom
        self.voitures=voitures
        self.thislist=[]
    def affichage(self):
        print("le id de la voiture est : ",self.ID,
              "le nom de la voitures est: ",self.nom,
              "la voiturs est: ",self.voitures)
        for val in self.thislist:
            val.affichage()
    def __str__(self):
        return("le id de la voiture est : "+str(self.ID)+
               "le nom de la voitures est: "+self.nom+
               "la voiturs est: "+self.voitures)
    def ajouter(self):
        nombre=int(input("saisir le nombre des voitures: "))
        for i in range(nombre):
            a=int(input("saisir le matricule de la voiture: "))
            b=input("saisir la marque: ")
            c=int(input("saisir lanné; "))
            mercedeces=voiture(a,b,c)
            self.thislist.append(mercedeces)
    def chercher(self):
        d=str(input("saisir titre du film que tu chreche: "))
        if d in self.thislist:
            print("le film est dans la liste")
        else:
            print("le film n'est  pas dans la lite")