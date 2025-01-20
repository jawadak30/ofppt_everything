class chauffeur:
    def __init__(self,cin,prenom,nom):
        self.__cin=cin
        self.__prenom=prenom
        self.__nom=nom
    def get_cin(self):
        return(self.__cin)
    def grt_prenom(self):
        return(self.__prenom)
    def get_nom(self):
        return(self.__nom)
    def __str__(self):
        return("le cin de chauffeur est: "+str(self.__cin)+
               "le prénom de chauffeur est: "+self.__prenom+
               "le nom de chaufeur est: "+self.__nom)
class Bus:
    def __init__(self,Immatriculation,Marque,Type):
        self.__Immatriculation=Immatriculation
        self.__Marque=Marque
        self.__Type=Type
    def get_Immatriculation(self):
        return(self.__Immatriculation)
    def get_marque(self):
        return(self.__Marque)
    def get_type(self):
        return(self.__Type)
    def __str__(self):
        return("le matricule de bus est: "+str(self.__Immatriculation+
                                               "la marque de bus est: "+self.__Marque+
                                               "le type de bus est: "+self.__Type))
class voyage:
    numerodevoyage=0
    def __init__(self,vchauffeur,vbus,datevoyage,villedepart,villearrive,nombredevoyageurs,prixdubillet):
        self.__vchauffeur=vchauffeur
        self.__vbus=vbus
        self.__datevoyage=datevoyage
        self.__villedepart=villedepart
        self.__villearrive=villearrive
        self.__nombredevoyageurs=nombredevoyageurs
        self.__prixdubillet=prixdubillet
        voyage.numerodevoyage+=1
        self.id=voyage.numerodevoyage
        self.__recettevoyage =self.__nombredevoyageurs*self.__prixdubillet
    def get_vchauffeur(self):
        return(self.__vchauffeur)
    def get_vbus(self):
        return(self.__vbus)
    def get_datevoyage(self):
        return(self.__datevoyage)
    def get_villedepart(self):
        return(self.__villedepart)
    def get_villearrive(self):
        return(self.__villearrive)
    def get_nombredevoyageurs(self):
        return(self.__nombredevoyageurs)
    def grt_prixdebillet(self):
        return(self.__prixdubillet)
    def get_recettevoyage(self):
        return(self.__recettevoyage)
    def __str__(self):
        return("le numero du voyage est: "+str(self.id)+"le chauffeuer de bus est: "+self.__vchauffeur+
               "le bus conduit par ce chauffeur est: "+self.__vbus+
               "la date de voyage est: "+str(self.__datevoyage+
                "la ville dee départ est; "+self.__villedepart+
                "la ville d'arivvé est: ")+self.__villearrive+
                "le nombre de voyageur est: "+str(self.__nombredevoyageurs)+
                "prix de billet est: "+str(self.__prixdubillet)+
                "la reccete du voyage est: "+str(self.__recettevoyage))
class GestionVoyage:
    def ajouter_chauffeur(self,chauf):
        lschauffeur=[]
        lschauffeur.append(chauf)
        for val in lschauffeur:
           print(val)
    def AjouterBus(self,bus):
        lsbus=[]
        lsbus.append(bus)
        for val in lsbus:
            print(val)
    def AjouterVoyage(self,voy):
        lsvoyage=[]
        lsvoyage.append(voy)
        for val in lsvoyage:
            print(lsvoyage)
    




gestion=GestionVoyage()
cin=input("saisir le cin de chauffeur: ")
prenom=input("saisir le prénom de chauffeur: ")
nom=input("saisir le nom de chauffeur: ")
chauf=chauffeur(cin,prenom,nom)
print(chauf)
Immatriculation=input("saisir le matricule de bus pour l'ajouter :")
Marque=input("saisir la marque de bus: ")
Type=input("saisir le type de bus")
bus=Bus(Immatriculation,Marque,Type)
vchauffeur=input("saisir le chauffeur pour cette voyage: ")
vbus=input("saisir le bus dans cette voyage: ")
datevoyage=int(input("saisir la date de voyage: "))
villedepart=input("saisir la ville de depart de voyage :")
villearrive=input("saisir la ville d'arrivé de voyage: ")
nombredevoyageurs=int(input("saisir le nombre des voyageurs: "))
prixdubillet=int(input("saisir le prix de billet :"))
voy=voyage(vchauffeur,vbus,datevoyage,villedepart,villearrive,nombredevoyageurs,prixdubillet)
gestion.AjouterVoyage(voy)
gestion.AjouterBus(bus)
gestion.ajouter_chauffeur(chauf)