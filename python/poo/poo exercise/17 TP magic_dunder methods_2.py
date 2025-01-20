#magic method
#dunder method
#special method
#appliquer la surcharge des opérateurs
class Produit:
    def __init__(self,prix):
        self.prix=prix
    #surcharge de méthode    
    def CalculPrix(self,taxe=None):
        #print(self.prix+taxe)# créer une erreur si taxe est None: number+None
        if taxe is None :
            print(self.prix)
        else:
            print(self.prix+taxe)
    #surcharge des opérateurs : __add__ est la méthode magic de +
    def __add__(self,p):
        return self.prix+p.prix
    def __lt__(self,p):
        if self.prix<p.prix:
            return True
        else:
            return False
        
        
p1=Produit(1000)
p2=Produit(200)
print(p1+p2)
if p1<p2:
    print("p1 a le plus petit prix")
else:
    print("p2 a le plus petit prix")





    
