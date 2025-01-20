from abc import ABC, abstractmethod #Abstract Base Classes
#classe abstraite
class Equipement(ABC):
    def __init__(self,code, prix,couleur):
        super().__init__()
        self._code=code
        self._prix=prix       
        self._couleur=couleur
    def afficherInfos(self):
        print("code:",self._code,
              "prix:",self._prix,            
              "couleur:",self._couleur)
    @abstractmethod
    def setCode(self,code):
        pass
class Table(Equipement):
    def __init__(self,code, prix,couleur,forme):
        super().__init__(code, prix,couleur)
        self.__forme=forme
    def afficherInfos(self):
        super().afficherInfos()
        print("la forme est : ",self.__forme)
    def setCode(self,code):
        self._code=code
t=Table(1,1000,"noire","ronde")
t.afficherInfos()
#ta=Equipement(2,2000,"jaune")
#ta.afficherInfos()

