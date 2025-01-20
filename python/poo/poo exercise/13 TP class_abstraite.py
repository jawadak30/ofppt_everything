from abc import ABC, abstractmethod # Abstract Base Classes
class Equipement(ABC):    
    @abstractmethod
    def printInfos(self):
        pass
    def remise_prix(self,x):
        self.prix-=x
class Bureau(Equipement):
    def __init__(self,p):
        self.prix=p
    def printInfos(self):
        print("le prix du bureau est:",self.prix)

"""b=Bureau(100)
b.printInfos()
b.remise_prix(10)
b.printInfos()"""
bu=Equipement()
