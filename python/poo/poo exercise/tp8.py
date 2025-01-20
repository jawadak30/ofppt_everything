class Patient:
    def __init__(self,Numérodedossier,Nom,Prénom,Datedenaissance,Sexe,Adresse,Numérosécuritésociale):
        self.__Numérodedossier=Numérodedossier
        self.__Nom=Nom 
        self.__Prénom=Prénom
        self.__Datedenaissance=Datedenaissance
        self.__Sexe=Sexe
        self.__Adresse=Adresse
        self.__Numérosécuritésociale=Numérosécuritésociale
    def get_Numérodedossier(self):
        return(self.__Numérodedossier) 
    def get_nom(self):
        return(self.__Nom)
    def get_Prénom(self):
        return(self.__Prénom)
    def get_Datedenaissance(self):
        return(self.__Datedenaissance)
    def get_Sexe(self):
        return(self.__Sexe)
    def get_Adresse(self):
        return(self.__Adresse)
    def get_Numérosécuritésociale(self):
        return(self.__Numérosécuritésociale)
    def __str__(self):
        return("le numero se serie est: "+str(self.__Numérodedossier)+"le nom est: "+self.__Nom+
               "le prenom est: "+self.__Prénom+"la date de naissance est: "+str(self.__Datedenaissance)+
               "le sexe est: "+self.__Sexe+"ladresse est; "+str(self.__Adresse)+
               "le numéro de serie est: "+str(self.__Numérosécuritésociale))
class Medcin:
    def __init__(self,Numéroidentification,Nom,Prénom,Spécialité):
        self.__Numéroidentification=Numéroidentification
        self.__Nom=Nom
        self.__Prénom=Prénom
        self.__Spécialité=Spécialité
    def get_Numéroidentification(self):
        return(self.__Numéroidentification)
    def get_Nom(self):
        return(self.__Nom)
    def get_Prénom(self):
        return(self.__Prénom)
    def get_Spécialité(self):
        return(self.__Spécialité)
    def __str__(self):
        return("le Numéroidentification est: "+str(self.__Numéroidentification)+"le nom est: "+self.__Nom+
               "le prénom est: "+self.__Prénom+"la spécialité est: "+self.__Spécialité)
class RendezVous:
    def __init__(self,numeroDeRrendezVous,Patient,Medcin,Date,heuredurendezvous,Motifdeconsultation):
        self.__numeroDeRrendezVous=numeroDeRrendezVous
        self.__Patient=Patient
        self.__Medcin=Medcin
        self.__Date=Date
        self.__heuredurendezvous=heuredurendezvous
        self.__Motifdeconsultation=Motifdeconsultation
    def get_numeroDeRrendezVous(self):
        return(self.__numeroDeRrendezVous)
    def get_Patient(self):
        return(self.__Patient)
    def get_Medcin(self):
        return(self.__Medcin)
    def get_Date(self):
        return(self.__Date)
    def get_heuredurendezvous(self):
        return(self.__heuredurendezvous)
    def get_Motifdeconsultation(self):
        return(self.__Motifdeconsultation)
    def __str__(self):
        return("le numero De Rrendez-Vous"+str(self.__numeroDeRrendezVous)+"le patient est: "+self.__Patient+
               "le medcin est: "+self.__Medcin+"la date est: "+str(self.__Date)+
               "l'heure de rendez-vous est: "+str(self.__heuredurendezvous)+"le motif de consultation est: "+self.__Motifdeconsultation)
class Traitement:
    def __init__(self,Numérodetraitement,Patient,description,Datededébut,datedefinprévue):
        self.__Numérodetraitement=Numérodetraitement
        self.__Patient=Patient
        self.__description=description
        self.__Datededébut=Datededébut
        self.__datedefinprévue=datedefinprévue
    def get_Numérodetraitement(self):
        return(self.__Numérodetraitement)
    def get_Patient(self):
        return(self.__Patient)
    def get_description(self):
        return(self.__description)
    def get_Datededébut(self):
        return(self.__Datededébut)
    def get_datedefinprévue(self):
        return(self.__datedefinprévue)
    def __str__(self):
        return("le numero de traitement est: "+str(self.__Numérodetraitement)+"le patient est: "+self.__Patient+
               "la date d'inscription set : "+str(self.__description)+"la date de debut: "+str(self.__Datededébut)+
               "la date de fin prévue est: "+str(self.__datedefinprévue))
class  GestionClinique:
    def __init__(self):
        self.Patient=[]
        self.Medcin=[]
        self.Rendezvous=[]
        self.Traitement=[]
    def ajouter_patient(self,Pat):
        if Patient.get_Numérodedossier() not in self.Patient: 
            self.Patient.append(Pat)
            return(self.Patient)
        else:
            return("ce patient existe ")
    def ajouter_medcin(self,Medc):
        if Medcin.get_Numéroidentification() not in self.Medcin:
            self.Medcin.append(Medc)
            return(Medc)
        else:
            return("ce medcin esiste: ")
    def ajouter_rendz(self,Rend):
        if RendezVous.get_numeroDeRrendezVous() not in self.Rendezvous:
            self.Rendezvous.append(Rend)
            return(Rend)
        else:
            return("ce numero de rendez-vous existe")
    def ajouter_traitement(self,Traite):
        if Traitement.get_Numérodetraitement() not in self.Traitement:
            self.Traitement.append(Traite)
            return(Traite)
        else:
            return("ce traitement est pris")
gest=GestionClinique()
Numérodedossier=int(input("saisir le numero de serie du patient: "))
Nom=input("saisir le nom du patient: ") 
Prénom=input("saisir le prénom du patient: ")
Datedenaissance=int(input("saisir la date de naissance: "))
Sexe=input("saisir le sexe du patient: ")
Adresse=input("saisir l'adresse: ")
Numérosécuritésociale=input("saisir le numero de securite sociale: ")
pat=Patient(Numérodedossier,Nom,Prénom,Datedenaissance,Sexe,Adresse,Numérosécuritésociale)
print(gest.ajouter_patient(pat))