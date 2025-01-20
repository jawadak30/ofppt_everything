from abc import ABC, abstractmethod
class Equipement(ABC):
    def __init__(self,code,date,etat,prix):
        super().__init__()
        self._code=code
        self._date=date
        self._etat=etat
        self._prix=prix
    @abstractmethod
    def set_etat(self,etat):
        pass
    def __str__(self):
        return("le code est: "+str(self._code)+
               "la date est: "+str( self._date)+
               "etat est: "+self._etat+
               "le prix est: "+str(self._prix))
class ordinateur(Equipement):
    def __init__(self,code,date,etat,prix,marque,taille):
        super().__init__(code,date,etat,prix)
        self.marque=marque
        self.taille=taille
    def __str__(self):
        return("le code est: "+str(self._code)+"la date est: "+str( self._date)+"etat est: "+self._etat+
               "le prix est: "+str(self._prix)+"la marque est: "+self.marque+"la taille est: "+str)
class table(Equipement):
    def __init__(self,code,date,etat,prix,longuer,largeur):
        super().__init__(code,date,etat,prix)
        self.longeur=longuer
        self.largeur=largeur
    def __dtr__(self):
        return("le code est: "+str(self._code)+"la date est: "+str( self._date)+"etat est: "+self._etat+
               "le prix est: "+str(self._prix)+"la longeur est: "+str(self.longeur)
               +"la largeur est: "+str(self.largeur))
class chaise(Equipement):
    def __init__(self, code, date, etat, prix,couleur):
        super().__init__(code, date, etat, prix)
        self.couleur=couleur
    def __str__(self):
        return("le code est: "+str(self._code)+"la date est: "+str( self._date)+
               "etat est: "+self._etat+
               "le prix est: "+str(self._prix)+"la couleur est; "+self.couleur)
class bureau:
    def __init__(self,code,description):
        self.code=code
        self.description=description
        self.nombre_dequipement=[]
    def __str__(self):
        return("le code est: "+str(self.code)+"la description est: "+self.description+
               "le nombre des equipement: "+str(self.nombre_dequipement))
    def ajouterEquipenent(self,equipement):
        self.nombre_dequipement.append(equipement)
    def rechercheEquipement(self,equipement):
        v=int(input("saisir le code de l'equipementpour le chercher : "))
        if v in self.nombre_dequipement.code:
            return equipement
        else:
            return("il n'existe pas")
    def ficheInventaire(self):
        print(self.nombre_dequipement)
    def supprimerEquipement(self):
        s=int(input("saisir le code ^pour supeimme l'equipement: "))
        for val in  self.nombre_dequipement.code:
            if s==self.nombre_dequipement.code:
                del val
                return self.nombre_dequipement
            else:
                return "ce equipmenet n'existe pas "
class entreprise:
    def __init__(self,nom,adresse,telephone):
        self.lsBureaux=[]
        self.nom=nom
        self.adresse=adresse
        self.telephone=telephone
    def __str__(self):
        return("le nom est : "+self.nom+"l'adresee est: "+self.adresse+
               "le telephone est: "+str(self.telephone)+self.lsBureaux)
    def ajouterBureau(self,bureau):
        self.lsBureaux.append(bureau)
    def rechercheEquipement(self,code):
        code=int(input("saisir le code de l'equipementpour le chercher : "))
        for val in self.lsBureaux:
            if val.code==code:
                return val
            else:
                return ("l'equiepment que tu cherche n'existe pas ")
    def localisation(self):
        code=int(input("saisir le code de l'equipement pour le chercher est retorner l'affectation: "))
        for val in self.lsBureaux:
            if val.code==code:
                return self.lsBureaux.description
    def transferEquipement(self, code, bureau_source, bureau_destination):
        equipement = bureau_source.rechercheEquipement(code)
        bureau_source.supprimerEquipement(code)
        bureau_destination.ajouterEquipement(equipement)

    def exporter(self, fichier):
        with open(fichier, 'w') as f:
            for bureau in self.bureaux:
                f.write(f"{bureau.code}, {bureau.description}\n")
                for equipement in bureau.equipements:
                    f.write(f"{equipement.code}, {equipement.date_acquisition}, {equipement.etat}, {equipement.prix_achat}\n")
            print(f"Données exportées avec succès dans le fichier {fichier}")


# Exemple d'utilisation
if __name__ == "__main__":
    ordinateur1 = ordinateur("001", "01/01/2023", "Opérationnel", 1000, "HP", 15)
    table1 = table("002", "01/02/2023", "Opérationnel", 500, 120, 80)
    chaise1 = chaise("003", "01/03/2023", "Non opérationnel", 50, "Bleu")

    bureau1 = bureau("B001", "Bureau principal")
    bureau1.ajouterEquipement(ordinateur1)
    bureau1.ajouterEquipement(table1)
    bureau1.ajouterEquipement(chaise1)

    entreprise1 = entreprise("Mon Entreprise", "123 Rue Principale", "0123456789")
    entreprise1.ajouterBureau(bureau1)

    print(entreprise1)
    print(bureau1)
    print(bureau1.rechercheEquipement("002"))
    entreprise1.localisation("002")

    fichier_export = "donnees_exportees.txt"
    entreprise1.exporter(fichier_export)