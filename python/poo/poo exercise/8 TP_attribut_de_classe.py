class Fruit:
    nom = "fruit"
    def __init__(self, couleur, poids):
        self.couleur=couleur
        self.poids=poids
if __name__=="__main__":
    pomme= Fruit("verte",100)
    print(pomme.nom)
    print(Fruit.nom)
        
        
        
