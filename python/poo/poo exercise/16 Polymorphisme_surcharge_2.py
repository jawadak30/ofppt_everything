#En python la surcharge de méthode est définie par if else
class Produit:
    def __init__(self,prix):
        self.prix=prix
    #surcharge de méthode    
    def CalculPrix(self,taxe=None):
        #print(self.prix+taxe)
        if taxe is None :
            print(self.prix)
        else:
            print(self.prix+taxe)        
        
p=Produit(100)
p.CalculPrix()



