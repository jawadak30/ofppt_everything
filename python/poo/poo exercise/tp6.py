
class Article:
    def __init__(self,numerodeserie=None,pht=None,quantiteenstock=None,quantiteminimale=None):
        self.__numerodeserie=numerodeserie
        self.__pht=pht
        self.__quantiteenstock=quantiteenstock
        self.__quantiteminimale=quantiteminimale
    def get_numerodeserie(self):
        return(self.__numerodeserie)
    def set_numerodeserie(self,numerodeserie):
        self.__numerodeserie=numerodeserie
    def get_pht(self):
        return(self.__pht)
    def set_pht(self,pht):
        self.__pht=pht
    def get_quantiteenstock(self):
        return(self.__quantiteenstock)
    def set_quantiteenstock(self,quantiteenstock):
        self.__quantiteenstock=quantiteenstock
    def get_quantiteminimale(self):
        return(self.__qucantiteminimale)
    def set_quantiteminimale(self,quantiteminimale):
        self.__quantiteminimale=quantiteminimale
    def afficher(self):
        print("le numero de serie est: ",self.__numerodeserie,
              "le prix hors tax est: ",self.__pht,
              "la quentite en stock est: ",self.__quantiteenstock,
              "la quantite minimale est: ",self.__quantiteminimale)
    def approvisionner(self):
        print("------------e stock par une quantité ---------------")
        print("la quentite en stock est: ",self.__quantiteenstock)
    def achat(self):
        if self.__quantiteenstock<self.__quantiteminimale:
            print(" la quantité qui reste est inférieure à la quantité minimale")
        else:
            if self.__quantiteenstock>self.__quantiteminimale:
                print("la quantité qui reste est superieure à la quantité minimale")
class Habit(Article):
    def __init__(self,numerodeserie=None,pht=None,quantiteenstock=None,quantiteminimale=None,couleur=None,taille=None):
        Article.__init__(self,numerodeserie=None,pht=None,quantiteenstock=None,quantiteminimale=None)
        self.__couleur=couleur
        self.__taille=taille
    def get_couleur(self):
        return(self.__couleur)
    def set_couleur(self,couleur):
        self.__couleur=couleur
    def get_taille(self):
        return(self.__taille)
    def set_taille(self,taille):
        self.__taille=taille
    def affichage(self):
        print("la couleur est: ",self.__couleur,"   ,   ","la taille est: ",self.__taille)
    def afficher(self):
        Article.afficher(self)
        self.affichage()
class Electromenager(Article):
    def __init__(self, numerodeserie=None, pht=None, quantiteenstock=None, quantiteminimale=None, poids=None,garantie=None):
        Article.__init__(self,numerodeserie=None, pht=None, quantiteenstock=None, quantiteminimale=None)
        self.__poids=poids
        self.__garantie=garantie
    def get_poids(self):
        return(self.__poids)
    def set_poids(self,poids):
        self.__poids=poids
    def get_garantie(self):
        return(self.__garantie)
    def set_garantie(self,garantie):
        self.__garantie=garantie
    def DateDeFinGarantie(self):
        s=0
        garantie=int(input("saisir le garantie en mpois: "))
        garantie=garantie+s
        print("le garantie sera termine après: ",garantie)
p=Article()
p.set_numerodeserie(1222)
p.set_pht(12)
p.set_quantiteenstock(1444)
p.set_quantiteminimale(14455)
p.afficher()
p.approvisionner()
p.achat()
h=Habit()
h.set_numerodeserie(12)
h.set_pht(13)
h.set_quantiteenstock(1222)
h.set_quantiteminimale(12)
h.set_couleur('white')
h.set_taille(180)
h.afficher()
h.achat()
a=Electromenager()
a.set_numerodeserie(1222)
a.set_pht(12)
a.set_quantiteenstock(1444)
a.set_quantiteminimale(14455)
a.afficher()
a.approvisionner()
a.achat()
a.DateDeFinGarantie()
