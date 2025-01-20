from datetime import date
class Produit:
    #constructeur
    def __init__(self,numserie=None, intitule=None, distributeurs=None,
                 dateProd=None, prix=None, nomProducteur=None):
        self.__numserie=numserie
        self.__intitule=intitule
        self.__distributeurs=distributeurs
        self.__dateProd=dateProd
        self.__prix=prix
        self.__nomProducteur=nomProducteur
    #get
    def getnumserie(self):
        return self.__numserie
    def getintitule(self):
        return self.__intitule
    def getdistributeurs(self):
        return self.__distributeurs
    def getdateProd(self):
        return self.__dateProd
    def getprix(self):
        return self.__prix
    def getnomProducteur(self):
        return self.__nomProducteur
    #set
    def setnumserie(self,numserie):
        self.__numserie=numserie
    def setintitule(self,intitule):
        self.__intitule=intitule
    def setdistributeurs(self,distributeurs):
        self.__distributeurs=distributeurs
    def setdateProd(self,dateProd):
        self.__dateProd=dateProd
    def setprix(self,prix):
        self.__prix=prix
    def setnomProducteur(self,nomProducteur):
        self.__nomProducteur=nomProducteur
    #Méthodes
    def comparerProduits(self,  p=None,numserie=None ):
        if p is None and numserie is None:
            print("vous devez donner soit le numéro de série du produit ou le produit")
            return
        elif numserie is None:
            if self.__numserie==p.__numserie:
                #return True
                print("égalité par objet")
            else:
                #return False
                print("non égalité par objet")
        elif p is None:
            if self.__numserie==numserie:
                #return True
                print("égalité par numero de serie")
            else:
                #return False
                print("non égalité par numero de serie")
        
        else:
            print("donner soit le numéro de série soit le produit")
    def __str__(self):
        return (str("numserie: "+str(self.__numserie)+" intitule: "+self.__intitule                
               +" prix: "+str(self.__prix)+" nomProducteur: "+ self.__nomProducteur))
    def afficher(self):
        print("numserie: "+str(self.__numserie)+" \nintitule: "+self.__intitule                
               +"\nprix: "+str(self.__prix)+"\nnomProducteur: "+ self.__nomProducteur
              +"\ndate production: "+str(self.__dateProd))
        print("le nom des distributeurs: ")
        for i in range(len(self.__distributeurs)):
            print("nom distributeur:", self.__distributeurs[i])
    def remise(self,taux):
        self.__prix-=self.__prix*taux
    

#p=Produit(1,"intitule1",["nomdis1","nomdis2"],date(2022,5,29),100,"nomprod1")
#print(p)
P=[]
"""for i in range(2):
    print("--------saisir les infos du produit N°", i+1)
    numserie=int(input("NUMSERIE: "))
    intitule = input("intitule: ")
    n=int(input("le nombre des distributeurs: "))
    distributeurs=[]
    for j in range(n):
        distributeurs.append(input("donner le nom du distributeur: "))
    print("ok")
    annee=int(input("donner l'annee de production: "))
    mois=int(input("donner le mois de production: "))
    jour=int(input("donner le jour de production: "))
    dateProd=date(annee,mois,jour)
    prix = int(input("donner le prix: "))
    nomProducteur = input("donner le nom du producteur: ")
    prod= Produit(numserie,intitule,distributeurs,dateProd,prix,nomProducteur)
    P.append(prod)"""
p1=Produit(1,"intitule1",["nom11","nom2"],date(2022,5,29),100,"nomprod1")
p2=Produit(2,"intitule2",["nom22","nom2"],date(2022,5,29),200,"nomprod2")
p3=Produit(3,"intitule3",["nom33","nom2"],date(2022,5,29),300,"nomprod3")
P.append(p1)
P.append(p2)
P.append(p3)
"""for i in range(2):
    P[i].afficher()"""
p1.comparerProduits(p2)
p1.comparerProduits(numserie=1)

"""nom=input("donner le nom du ditstributeur: ")
listeProduits=[]
for p in P:
    if nom in p.getdistributeurs():
        print("-------ce distributeur existe-------------")
        existe=False
        for prod in listeProduits:
            if prod.comparerProduits(p)==True:                
                existe=True
        if existe==False:
            listeProduits.append(p)
print("la liste des produits de ce distributeur: ")
for p in listeProduits:
    p.afficher()"""
                
        
    


























                  
