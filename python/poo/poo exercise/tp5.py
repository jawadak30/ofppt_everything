class Employe:
    def __init__(self,ID,nom,Prenom):
        self.__ID=ID
        self.__nom=nom
        self.__Prenom=Prenom
    def get_ID(self):
        return(self.__ID)
    def get_nom(self):
        return(self.__nom)
    def get_Prenom(self):
        return(self.__Prenom)
    def __str__(self):
        return("le ID est: "+str(self.__ID)+
               "le nom est: "+self.__nom+
               "le prenom est: "+self.__Prenom)
class Salle:
    def __init__(self,numero,nom,capacite):
        self.__numero=numero
        self.__nom=nom
        self.__capacite=capacite
    def get_numero(self):
        return(self.__numero)
    def get_nom(self):
        return(self.__nom)
    def get_capacite(self):
        return(self.__capacite)
    def __str__(self):
        return("le numero est: "+str(self.__numero)+
               "le nom est: "+self.__nom+
               "la capacite est: "+self.__capacite)
class reservation:
    numero=0
    def __init__(self,employe,salle,dateDeEntre,dateDeSortie,heureDeDebut,heureDeFin,objectif):
        self.__employe=employe
        self.__salle=salle
        self.__dateDeEntre=dateDeEntre
        self.__dateDeSortie=dateDeSortie
        self.__heureDeDebut=heureDeDebut
        self.__heureDeFin=heureDeFin
        self.__objectif=objectif
        reservation.numero = reservation.numero+1
    def get_employe(self):
        return(self.__employe)
    def get_salle(self):
        return(self.__salle)
    def get_dateDeEntre(self):
        return(self.__dateDeEntre)
    def get_dateDeSortie(self):
        return(self.__dateDeSortie)
    def get_heureDeDebut(self):
        return(self.__heureDeDebut)
    def get_heureDeFin(self):
        return(self.__heureDeFin)
    def get_objectif(self):
        return(self.__objectif)
    def __str__(self):
        return("numero de reservation est: "+str(self.number)
               +"les details de l'employe sont: "+self.__employe
               +"la salle est: "+self.__salle+
               "la date d'enré est: "+self.__dateDeEntre+
               "la date de sortie est: "+self.__dateDeSortie+
               "l'heure de début est: "+self.__heureDeDebut+
               "l'heure de sortie est : "+self.__heureDeFin+
               "l'objectif est: "+self.__objectif)
class GestionRéservations:
    def __init__(self):
        self.listeemploye=[]
        self.listesalle=[]
        self.listereservation=[]
    def AjouterEmployé(self,employe):
        if Employe.get_ID not in self.listeemploye:
            self.listeemploye.append(employe)
            return(self.listeemploye)
        else:
            return("ce employe",employe," est existe dans la liste des employe")
    def AjouterSalle(self,salle):
        if salle.get_numero() not in self.listesalle:
            self.listesalle.append(salle)
            return(self.listesalle)
        else:
            return("cette salle ",salle,"existe")
    def Ajouterreservation(self):
        if Salle.get_numero(self) not in self.listereservation: 
            self.listereservation.append(res)
            return(self.listereservation)
        else:
            return("cette salle",salle,"est existé")
    def RechercherEmployé(self):
        id=int(input("saisir 'id de l'employe pour le chercher s'il existe: "))
        if id in self.listeemploye.get_ID():
            return("l'employé chercher existe",employe)
        else:
            return("l'employé chercher n'existe pas")
    def RechercherSalle(self):
        nr=int(input("saisir le numero de la salle pour chercher :"))
        if nr in self.listesalle.get_numero():
            return("cette salle ",salle," existe")
        else:
            return("le salle n'existe pas")
    def RechercherRéservation(self):
        nm=int(input("saisir le numero de la reservation pour le chercher: "))
        if nm == reservation.numero:
            return("cette resesrvation est existé")
        else: 
            return("cette reservation n'est pas existé")
    def AfficherRéservations(self):
        return(self.listereservation)
p=GestionRéservations()
nbr=int(input("saisir le nombre des employe pour l'ajouter a la liste: "))
for i in range(nbr):
    ID=int(input("saisir l'id de l'emplye: "))
    nom=input("saisir le nom de l'emplye: ")
    Prenom=input("saisir le prenom de l'employe: ")
employe=Employe(ID,nom,Prenom)
print(p.AjouterEmployé(employe))
nbr=int(input("saisir le nombre des salle pour ajouter une sale"))
for i in range(nbr):
    numero=int(input("saisir le numero de la salle: "))
    name=str(input("saisir le nom de la salle: "))
    capacite=int(input("saisir la capacité de la salle: "))
    salle=Salle(numero,name,capacite)
print(p.AjouterSalle(salle))
c=int(input("saisir le nombre de rservation pour l'ajouté: "))
for i in range(c):
    employe=str(input("saisir le nom de l'employe: "))
    salle=int(input("saisr le numero de la salle :"))
    dateDeEntre=int(input("saisir le date d'entr: "))
    dateDeSortie=int(input("saisi rla deate de sortie: "))
    heureDeDebut=int(input("saisir l'heure d'entré: "))
    heureDeFin=int(input("saisie l'heure de sortie: "))
    objectif=input("saisr l'objectif: ")
    res=reservation(employe,salle,dateDeEntre,dateDeSortie,heureDeDebut,heureDeFin,objectif)
print(p.Ajouterreservation())
print(p.RechercherEmployé())
print(p.RechercherSalle())
print(p.RechercherRéservation())
print(p.AfficherRéservations())