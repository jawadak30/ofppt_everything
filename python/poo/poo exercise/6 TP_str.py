class Voiture:
    def __init__(self):
        self.__couleur="rouge"
        self.__marque="audi"
    def getCouleur(self):
        return self.__couleur
    def getMarque(self):
        return self.__marque
    def __str__(self):
        return "couleur:"+self.__couleur+"    marque:"+ self.__marque
if __name__=="__main__":
    v = Voiture()
    print(v)#permet d'imprimer l'objet directement
        
