from datetime import date
class Livre:
    def __init__(self,isbn=None, titre=None, noms=None,
                 datePub=None, prix=None, nomEdition=None):
        self.__isbn=isbn
        self.__titre=titre
        self.__noms=noms
        self.__datePub=datePub
        self.__prix=prix
        self.__nomEdition=nomEdition
    def comparerLivres(self, l=None, isbn=None):
        if l is None and isbn is None:
            print("vous devez donner soit l'ISBN du livre ou le livre")
            return 
        elif l is None:
            if self.__isbn==isbn:
                return True
            else:
                return False
        elif isbn is None:
            if self.__isbn==l.__isbn:
                return True
            else:
                return False
        else:
            print("donner soit ISBN soit le ivre")
    def __str__(self):
        return (str("isbn: "+str(self.__isbn)+" titre: "+self.__titre                
               +" prix: "+str(self.__prix)+" nomEdition: "+ self.__nomEdition))
    def afficher(self):
        print("isbn: "+str(self.__isbn)+" titre: "+self.__titre                
               +" prix: "+str(self.__prix)+" nomEdition: "+ self.__nomEdition
              +"date publication: "+str(self.__datePub))
        print("le nom des auteurs: ")
        for i in range(len(self.__noms)):
            print("nom auteur:", self.__noms[i])
    def promotion(self,taux):
        self.__prix-=self.__prix*taux
    

#l=Livre(1,"titre1",["nom1","nom2"],date(2022,5,29),100,"Edit1")
#print(l)
L=[]
"""for i in range(2):
    print("--------saisir les infos du livre N°", i+1)
    isbn=int(input("ISBN: "))
    titre = input("titre: ")
    n=int(input("le nombre des auteurs: "))
    noms=[]
    for j in range(n):
        noms.append(input("donner le nom de l'auteur: "))
    print("ok")
    annee=int(input("donner l'annee de publication: "))
    mois=int(input("donner le mois de publication: "))
    jour=int(input("donner le jour de publication: "))
    datePub=date(annee,mois,jour)
    prix = int(input("donner le prix: "))
    nomEdition = input("donner le nom de l'édition: ")
    liv= Livre(isbn,titre,noms,datePub,prix,nomEdition)
    L.append(liv)"""
l1=Livre(1,"titre1",["nom11","nom2"],date(2022,5,29),100,"Edit1")
l2=Livre(2,"titre2",["nom22","nom2"],date(2022,5,29),200,"Edit2")
l3=Livre(3,"titre3",["nom33","nom2"],date(2022,5,29),300,"Edit3")
L.append(l1)
L.append(l2)
L.append(l3)
for i in range(2):
    L[i].afficher()
    

























                  
