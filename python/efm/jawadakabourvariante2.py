import re
import json
import datetime
class livre:
    def __init__(self,ISBN,titre,auteur,genre):
        if self.set_ISBN(ISBN):
           self.ISBN=ISBN
        self.titre=titre
        self.auteur=auteur
        self.genre=genre
    def __str__(self):
        return "le ISBN est: "+self.ISBN+"le titre de livre est: "+self.titre+"l'auteur est :"+self.auteur+"le genre est :"+self.genre
    def set_Genre(self,genre):
        if genre=="roman" or genre=="biographie" or genre=="science fiction":
            self.genre=genre
    def set_ISBN(self,ISBN):
        return bool(re.match("^[1-9]".format(6)+" "+"[A-Z]"+" "+ "[1-9]".format(2),ISBN))
class membre:
    def __init__(self,telephone,mail,cin,nom,prenom,nii):
        self.telephone=telephone
        self.mail=mail
        self.cin=cin
        self.nom=nom
        self.prenom=prenom
        self.nii=nii
    def __str__(self):
        return "le telephone est: "+str(self.telephone)+"l'adresse mail est: "+self.mail+"le cin est: "+self.cin+"le nom est: "+self.nom+"le prenom est: "+self.prenom+"le nii est: "+self.nii
    def set_mail(self,mail):
        return bool(re.match("^[a-z].+@[a-z].+.ccc$"),mail)
class membreparticulier(membre):
    def __init__(self,telephone,mail,cin,nom,prenom,nii):
        super().__init__(telephone,mail,cin,nom,prenom,nii)
    def __str__(self):
        return super().__str__()
class membreinstitution(membre):
    def __init__(self,telephone,mail,cin,nom,prenom,nii):
        super().__init__(telephone,mail,cin,nom,prenom,nii)
    def __str__(self):
        return super().__str__()
class emprunt:
    num_emprunt=0
    def __init__(self,membre,livre,datededebut,datedefin,prix):
        emprunt.num_emprunt+=1
        self.nombre=emprunt.num_emprunt
        self.membre=membre
        self.livre=livre
        self.datededebut=datededebut
        self.datedefin=datedefin
        self.prix=prix
    def __str__(self):
        return "le numero d'emprunt: "+str(self.nombre)+"le membre est: "+self.membre+"le livre est: "+self.livre+"la date de debut est: "+self.datededebut+"la date de fin est: "+self.datedefin+"le prix est: "+str(self.prix)
    def prix_emp(self,prix):
        total_prix=self.nombre*prix
        return total_prix
class ensembleemprunts:
    def __init__(self):
       self.ls_emprunt=[]
    def ajouter_emprunt(self,empr):
        if empr not in self.ls_emprunt:
            self.ls_emprunt.append(empr)
    #def info_emprunt(self,telephone):
    def savegarde(self,membre):
        data={}
        data=json.dumps(membre)
        print(data)