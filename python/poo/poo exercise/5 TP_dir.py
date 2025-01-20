class Voiture:
    def __init__(self):
        self.__couleur='red'
        self.__marque='audi'
    def getCouleur(self):
        return self.__couleur
    def getMarque(self):
        return self.__marque
    def afficher(self):
        print("couleur:",self.__couleur,"marque:", self.__marque)
if __name__=="__main__":
    v=Voiture()
    print(dir(Voiture))
        
