class Produit:
    def __init__(self,prix):
        self.prix=prix
    #surcharge de méthode
    def CalculPrix(self,taxe):
        print(self.prix+taxe)
    def CalculPrix(self):
        print(self.prix)
p=Produit(100)
p.CalculPrix()
#p.CalculPrix(10)

