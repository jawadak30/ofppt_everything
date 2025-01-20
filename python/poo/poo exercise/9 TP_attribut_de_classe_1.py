#la modification de l’attribut de classe à l’aide de l’instance n’affectera que l’instance modifiée.
class Fruit:
    nom = "fruit"
    def __init__(self, couleur, poids):
        self.couleur=couleur
        self.poids=poids
if __name__=="__main__":
    pomme= Fruit("verte",100)
    banane=Fruit("jaune",100)
    print(pomme.nom)
    pomme.nom="bon fruit"
    print(pomme.nom)
    print(banane.nom) 
        
        
        
