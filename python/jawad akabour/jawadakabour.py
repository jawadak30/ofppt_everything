from abc import ABC,abstractmethod
from collections import deque
class velo(ABC):
    def __init__(self,numerodeserie,dateachat,etat,prixdachat):
        self.numerodeserie=numerodeserie
        self.dateachat=dateachat
        self.etat=etat
        self.prixdachat=prixdachat
    @abstractmethod
    def get_etat(self):
        pass
    def __str__(self):
        return("le numero de serie est: "+str(self.numerodeserie))+"la date d'achat est: "+str(self.dateachat)+"l'etat est: "+self.etat+"le prix d'achat est: "+self.prixdachat
class veloelectrique(velo):
    def __init__(self,numerodeserie,dateachat,etat,prixdachat,puissancedemouteur,autonomie,vitessemaximale):
        super().__init__(numerodeserie,dateachat,etat,prixdachat)
        self.puissancedemouteur=puissancedemouteur
        self.autonomie=autonomie
        self.vitessemaximale=vitessemaximale
    def __str__(self):
        return super.__str__()+"la puissance de mouteur est: "+str(self.puissancedemouteur)+"l'autonomie de batterie est: "+str(self.autonomie)+"la vitesse maximale est: "+str(self.vitessemaximale)
    def comparervelo(self,firstautonomie,secondautonomie):
        if firstautonomie==secondautonomie:
            return True
        else:
            return False
class velodecourse(velo):
    def __init__(self,numerodeserie,dateachat,etat,prixdachat,typedecadre,poids,typedefreins):
        super().__init__(numerodeserie,dateachat,etat,prixdachat)
        self.typedecadre=typedecadre
        self.poids=poids
        self.typedefreins=typedefreins
    def __str__(self):
        return super().__str__()+"le type de cadre est: "+self.typedecadre+"le poids est: "+str(self.poids)+"le type des freins est :"+self.typedefreins
class velohybride(veloelectrique,velodecourse):
    def __init__(self,puissancedemouteur,autonomie,typedecadre,poids):
        veloelectrique().__init__(self,puissancedemouteur,autonomie)
        velodecourse().__init__(self,typedecadre,poids)
    def __str__(self):
        return "la puissance de mouteur est: "+str(self.puissancedemouteur)+"l'autonomie de batterie est: "+str(self.autonomie)+"le type de cadre est; "+self.typedecadre+"le poids est: "+str(self.poids)
class magasin:
    def __init__(self,code,adresse):
        self.code=code
        self.adresse=adresse
        self.lsv=deque()
    def __str__(self):
        return "le code est: "+str(self.code)+"l'adrsee st: "+self.adresse+"le nombre des velos est: "+str(len(self.lsv))
    def ajoutervelo(self,velo):
        self.lsv.append(velo)
        return self.lsv
    def rechercher_velo(self,numerodeserie):
        for velo in self.lsv:
            if velo.numerodeserie==numerodeserie:
                return velo
            else:
                return "ce velo n'existe pas"
    def inventaire(self):
        lsvelo=[]
        for velo in self.lsv:
            lsvelo.append(velo)
    def suprimervelo(self,numerodeserie):
        for velo in self.lsv:
            if velo.numerodeserie==numerodeserie:
                self.lsv.pop(velo)
            else:
                return "ce velo n'existe pas "