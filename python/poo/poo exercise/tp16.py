from datetime import date
class employe:
    matricule=0
    def __init___(self,nom,prenom,priceofconge):
        employe.matricule+=1
        self.matricule= employe.matricule
        self.nom=nom
        self.prenom=prenom
        self.datedembauche=date.today()
        self.priceofconge=priceofconge
    def __str__(self):
        return("le matricule est: "+str(self.matricule)+"le nom est: "+self.nom+"le prénom est: "+self.prenom+"la date de sortie est: "+self.datedembauche+"le prix de congé est: "+self.priceofconge)
class manager(employe):
    def __init__(self,nom,prenom,priceofconge,codeofmanager):
        super().__init__(self,self,nom,prenom,priceofconge)
        self.codeofmanager=codeofmanager
        self.ls_employe=[]
    def __str__(self):
        return super.__str__()+"le code est: "+str(self.codeofmanager)+"names of employses :"+self.ls_employe
    def ajouterEmploye(self,employe):
        if employe.matricule not in self.ls_employe:
            self.ls_employe.append(employe.nom)
            return self.ls_employe
        else:
            return "ce employe existe"
    def getEmployeByCode(self,matri):
        for employe in self.ls_employe:
            if employe.matricule==matri:
                return employe
            else:
                return "ce employe n'existe pas "
    def trierEmployes(self):
        return self.ls_employe.sort(key= lambda emp : emp.nom)
class DemandeConge:
    def __init__(self,codeofemploye,duration,motif):
        self.codeofemploye=codeofemploye
        self.dateofdebut=date.today()
        self.duration=duration
        self.motif=motif
        self.etat="en cours"
    def valider(self,code):
        for employe in self.ls_employe:
            if employe.codeofemploye==code:
                employe.etat.append("validé")
                return employe
            else:
                return "ce employe n'existe pas"
    def refuser(self,code):
         for employe in self.ls_employe:
            if employe.codeofemploye==code:
                employe.etat.append("refusé")
                return employe
            else:
                return "ce employe n'existe pas"
class GestionCongé:
    def __init__(self,ls_manager=None,ls_demandeconge=None):
        self.ls_manager=[]
        self.ls_demandeconge=[]
    def ajouterDemandeConge(self,conge):
        if conge.codeofemploye not in self.ls_demandeconge:
            self.ls_demandeconge.append(conge)
            return self.ls_demandeconge
        else:
            return "ce congé déja existe"
    def listeDemandeCongeEnCours(self):
        self.ls_encour=[]
        for employe in self.ls_demandeconge:
            if employe.etat=="en cours":
                self.ls_encour.append(employe)
            return self.ls_encour
    def listeDemandeCongeParEmploye(self,code):
        if DemandeConge.codeofemploye not in self.ls_demandeconge:
            codeofemploye=input("saisir le code de l'employe: ")
            duration=input("write la durée: ")
            motif=input("saisir le motif de ce congé: ")
            self.ls_demandeconge.append(DemandeConge(codeofemploye,duration,motif))
            