from abc import ABC, abstractmethod
class vehicule(ABC):
    def __init__(self, immatriculation, date_achat, etat, prix_achat):
        self.immatriculation = immatriculation
        self.date_achat = date_achat
        self.etat = etat
        self.prix_achat=prix_achat
    @abstractmethod
    def __str__(self):
        pass
class voiture(vehicule):
    def __init__(self,matricule,date_dachat,prix,etat,marque,modele,couleur):
        super().__init__(matricule,date_dachat,prix,etat)
        self.marque=marque
        self.modele=modele
        self.couleur=couleur
    def __str__(self):
        return "le matricule est: "+self.immatriculation+" la date d'achat est: "+str(self.date_achat)+" le prix est: "+str(self.prix)+" l'etat estg: "+self.etat+" la marque est: "+self.marque+" le modele est; "+self.modele+" le, couleurb estg "+self.couleur
class camion(vehicule):
    def __init__(self,matricule,date_dachat,prix,etat,capacite,dimension):
        super().__init__(matricule,date_dachat,prix,etat)
        self.capacite=capacite
        self.dimension=dimension
    def __str__(self):
        return "le matricule est: "+self.immatriculation+" la date d'achat est: "+str(self.date_achat)+" le prix est: "+str(self.prix)+" l'etat estg: "+self.etat+" la capicite est: "+self.capacite+" les dimensions de camion: "+self.dimension
class moto(vehicule):
    def __init__(self,matricule,date_dachat,prix,etat,cylindre,type):
        super().__init__(matricule,date_dachat,prix,etat)
        self.cylindre=cylindre
        self.type=type
    def __str__(self):
        return "le matricule est: "+self.immatriculation+" la date d'achat est: "+str(self.date_achat)+" le prix est: "+str(self.prix)+" l'etat estg: "+self.etat+" combien des cylindres: "+self.cylindre+" le type: "+self.type
class agence:
    def __init__(self,code,adresse):
        self.code=code
        self.adresse=adresse
        self.lsvehicule=[]
    def __str__(self):
        return "le code de l'agnece est: "+str(self.code)+" l'adresse de l'agnece est : "+self.adresse+" le nomber des vehicules: "+str(len(self.lsvehicule))
    def ajoutervehicule(self,vehicule):
        if vehicule not in self.lsvehicule:
            self.lsvehicule.append(vehicule)
    def rechercheVehicule(self,matricule):
        for vehicule in self.lsvehicule:
            if matricule==vehicule.matricule:
                return vehicule
            else:
                return"n'a pas de vehicule"
    def inventaire(self):
        print(self.lsvehicule)
    def suprimmevehicule(self):
        mat=int(input("saisir le amtricule pour suprimme: "))
        for vehicule in self.lsvehicule:
            if mat==vehicule.matricule:
                self.lsvehicule.remove(vehicule)
                return(self.lsvehicule)
            else:
                return("cette vehicule n'existe pas pour la suprimmée")
class entrepriseoflocation:
    def __init__(self,nom):
        self.nom=nom
        self.lsagnece=[]
    def __str__(self):
        return ("le nom est: "+self.nom+" le nombre des vehiclue est: "+str(len(self.lsagnece)))
    def ajouter_agence(self,agence):
        if agence not in self.lsagnece:
            self.lsagnece.append(agence)
        else:
            return("cette déja existée")
    def rechercheVehiculeGlobal(self,agence):
        for agence in self.lsagnece:
            if agence.rechercheVehicule()==True:
                return agence.rechercheVehicule()
            else:
                return("ce vecule n'existe pas dans les agences")
    def localisation(self,matricule):
        for val in self.lsagnece:
            for valeur in val.lsvehicule:
                if matricule==valeur.matricule:
                    print("cette vehicule est existe ")
                    return valeur.etat
                else:
                    return("cette vehicule n'existe pas")
agence1 = agence("A001","123 Rue de la Pompe")
voiture1 = voiture("ABC123","01/01/2023","disponible",20000,"Toyota","Corolla","Bleu")
agence1.ajoutervehicule(voiture1)
agence2 = agence("A002", "456 Avenue des Champs-Élysées")
camion1 = camion("XYZ789","02/01/2023", "en maintenance",30000, 5000,"6m x 2m x 2m")
agence2.ajoutervehicule(camion1)
entreprise_location =entrepriseoflocation("LocationCars")
entreprise_location.ajouter_agence(agence1)
entreprise_location.ajouter_agence(agence2)
print(entreprise_location)