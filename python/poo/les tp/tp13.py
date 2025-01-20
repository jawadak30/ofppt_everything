from abc import ABC,abstractmethod
import json

class Vehicule(ABC):
    @property
    @abstractmethod
    def numero_immatriculation(self):
        pass
    @property
    @abstractmethod
    def date_achat(self):
        pass
    @property
    @abstractmethod
    def etat(self):
        pass
    @property
    @abstractmethod
    def prix_achat(self):
        pass
    

    def __str__(self):
        return f"Immatriculation: {self.numero_immatriculation}\nDate d'achat: {self.date_achat}\nEtat: {self.etat}\nPrix d'achat: {self.prix_achat}\n"

class Voiture(Vehicule):
    def __init__(self,numero_immatriculation,date_achat,etat,prix_achat,marque,modele,couleur) -> None:
        self.__numero_immatriculation = numero_immatriculation
        self.__date_achat = date_achat
        self.__etat = etat
        self.__prix_achat = prix_achat
        self.__marque = marque
        self.__modele = modele 
        self.__couleur = couleur 

    @property
    def numero_immatriculation(self):
        return self.__numero_immatriculation
    
    @numero_immatriculation.setter
    def numero_immatriculation(self,value):
        self.__numero_immatriculation = value
    
    @property
    def date_achat(self):
        return self.__date_achat
    
    @date_achat.setter
    def date_achat(self,value):
        self.__date_achat = value
    
    @property
    def etat(self):
        return self.__etat
    
    @etat.setter
    def etat(self,value):
        self.__etat = value
    
    @property
    def prix_achat(self):
        return self.__prix_achat
    
    @prix_achat.setter
    def prix_achat(self,value):
        self.__prix_achat = value

    @property
    def marque(self):
        return self.__marque
    
    @marque.setter
    def marque(self,value):
        self.__marque = value
    
    @property
    def modele(self):
        return self.__modele

    @modele.setter
    def modele(self,value):
        self.__modele = value
    
    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self,value):
        self.__couleur = value
    
    def __str__(self):
        return super().__str__() + f"Marque: {self.__marque}\nModele: {self.__modele}\nCouleur: {self.__couleur}"
    



class Camion(Vehicule):
    def __init__(self,numero_immatriculation,date_achat,etat,prix_achat,capacite,dimension) -> None:
        self.__numero_immatriculation = numero_immatriculation
        self.__date_achat = date_achat
        self.__etat = etat
        self.__prix_achat = prix_achat
        self.__capacite = capacite
        self.__dimension = dimension

    @property
    def numero_immatriculation(self):
        return self.__numero_immatriculation
    
    @numero_immatriculation.setter
    def numero_immatriculation(self,value):
        self.__numero_immatriculation = value
    
    @property
    def date_achat(self):
        return self.__date_achat
    
    @date_achat.setter
    def date_achat(self,value):
        self.__date_achat = value
    
    @property
    def etat(self):
        return self.__etat
    
    @etat.setter
    def etat(self,value):
        self.__etat = value
    
    @property
    def prix_achat(self):
        return self.__prix_achat
    
    @prix_achat.setter
    def prix_achat(self,value):
        self.__prix_achat = value

    @property
    def capacite(self):
        return self.__capacite
    
    @capacite.setter
    def capacite(self,value):
        self.__capacite = value

    @property
    def dimension(self):
        return self.__dimension
    
    @dimension.setter
    def dimension(self,value):
        self.__dimension = value
    
    def __str__(self):
        return super().__str__() + f"Capacité: {self.__capacite}\nDimension: {self.__dimension}"


class Moto(Vehicule):
    def __init__(self,numero_immatriculation,date_achat,etat,prix_achat,cylindree,type) -> None:
        self.__numero_immatriculation = numero_immatriculation
        self.__date_achat = date_achat
        self.__etat = etat
        self.__prix_achat = prix_achat
        self.__cylindree = cylindree
        self.__type = type

    @property
    def numero_immatriculation(self):
        return self.__numero_immatriculation
    
    @numero_immatriculation.setter
    def numero_immatriculation(self,value):
        self.__numero_immatriculation = value
    
    @property
    def date_achat(self):
        return self.__date_achat
    
    @date_achat.setter
    def date_achat(self,value):
        self.__date_achat = value
    
    @property
    def etat(self):
        return self.__etat
    
    @etat.setter
    def etat(self,value):
        self.__etat = value
    
    @property
    def prix_achat(self):
        return self.__prix_achat
    
    @prix_achat.setter
    def prix_achat(self,value):
        self.__prix_achat = value

    @property
    def cylindree(self):
        return self.__cylindree
    
    @cylindree.setter
    def cylindree(self,value):
        self.__cylindree = value

    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self,value):
        self.__type = value

    def __str__(self):
        return super().__str__() + f"La cylindrée: {self.__cylindree}\nType: {self.__type}"


class Agence:
    def __init__(self,code,adresse) -> None:
        self.__code = code 
        self.__adresse = adresse 
        self.__lsVehicule = []
    
    @property
    def code(self):
        return self.__code
    
    @property
    def adresse(self):
        return self.__adresse

    @property
    def lsVehicule(self):
        return self.__lsVehicule

    def ajouter_vehicule(self,vehicule):
        "This method return True if the vehicule is added and False otherwise"
        for v in self.__lsVehicule:
            if v.numero_immatriculation == vehicule.numero_immatriculation:
                return False
        self.__lsVehicule.append(vehicule)
        return True

    def rechercher_vehicule(self,numero_immatriculation):
        for v in self.__lsVehicule:
            if v.numero_immatriculation == numero_immatriculation:
                return v
        raise Exception("Vehicule non trouvé")


    def inventaire(self):
        if len(self.__lsVehicule) == 0:
            print("Listes vide!")
            return
        print("Liste des Vehicules:")
        for v in self.__lsVehicule:
            print(v)
            print("="*20)

    def supprimer_vehicule(self,numero_immatriculation):
        for v in self.__lsVehicule:
            if v.numero_immatriculation == numero_immatriculation:
                self.__lsVehicule.remove(v)
    
    def __str__(self) -> str:
        return f"Code: {self.__code}\nAdresse: {self.__adresse}\nNombre de Vehicules: {len(self.__lsVehicule)}"



class EntrepriseLocation:
    def __init__(self,nom) -> None:
        self.__nom = nom
        self.__liste_agence = []

    def ajouter_agence(self,agence):
        "This method returns True if the agency is added and False otherwise"
        for ag in self.__liste_agence:
            if ag.code == agence.code:
                return False
        self.__liste_agence.append(agence)
    
    def rechercher_vehicule_global(self,numero_immatriculation):
        for ag in self.__liste_agence:
            for v in ag.lsVehicule:
                if v.numero_immatriculation == numero_immatriculation:
                    return v
        print("Vehicule non trouve")
                

    def localisation(self,numero_immatriculation):
        for ag in self.__liste_agence:
            for v in ag.lsVehicule:
                if v.numero_immatriculation == numero_immatriculation:
                    print(ag)
                    return
        print("Vehicule non trouve")
    
    def transfert_vehicule(self,numero_immatriculation,code_agence):
        nv_agence = None
        for ag in self.__liste_agence:
            if ag.code == code_agence:
                nv_agence = ag
        if nv_agence:
            for ag in self.__liste_agence:
                for v in ag.lsVehicule:
                    if v.numero_immatriculation == numero_immatriculation and code_agence != ag.code:
                        ag.lsVehicule.remove(v)
                        nv_agence.lsVehicule.append(v)


    def exporter(self):
        data = {}
        data["nom"] = self.__nom
        data["liste d'agences"] = []
        for ag in self.__liste_agence:
            ag_info = {}
            ag_info["code"] = ag.code
            ag_info["adresse"] = ag.adresse
            ag_info["liste de vehicules"] = []
            for v in ag.lsVehicule:
                v_info = {}
                for att in dir(v):
                    if "_" not in att:
                        v_info[att] = getattr(v,att)
                ag_info["liste de vehicules"].append(v_info)
            data["liste d'agences"].append(ag_info)          
        with open(self.__nom + ".json","w") as f:
            json.dump(data,f)






# MANUAL TESTS WITHOUT MENU

# agence
ag1 = Agence(123,"Maroc")
ag2 = Agence(132,"Maroc")
# ajouter vehicule
v1 = Voiture(123,"any","any",123,"any","any","any")
v2 = Voiture(132,"any","any",123,"any","any","any")

ag1.ajouter_vehicule(v1)
ag2.ajouter_vehicule(v2)
# rechercher vehicule
print("\nRECHERCHE =====")
r = ag1.rechercher_vehicule(123)
print(r)
print("="*20)
r = ag2.rechercher_vehicule(132)
print(r)
# inventaire

print("\nINVENTAIRE =====")
print("="*20)
ag1.inventaire()
print("="*20)
ag2.inventaire()
# supprimer vehicule
# ag1.supprimer_vehicule(123)
# ag2.supprimer_vehicule(132)

# ag1.inventaire()
# ag2.inventaire()

# EntrepriseLocation
entreprise = EntrepriseLocation("CompanyX")
# ajouter agence
entreprise.ajouter_agence(ag1)
entreprise.ajouter_agence(ag2)
# recherche global
print("\nRECHERCHE GLOBAL =====")
r = entreprise.rechercher_vehicule_global(123)
print(r)
print("="*20)

r = entreprise.rechercher_vehicule_global(132)
print(r)

# localisation
print("\nLOCALISATION =====")
entreprise.localisation(123)
print("="*20)
entreprise.localisation(132)

# transfert vehicule
entreprise.transfert_vehicule(numero_immatriculation=123,code_agence=132)

# exporter
entreprise.exporter()
