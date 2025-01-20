class Voiture:
    """ classe voiture avec option couleur """
    def __init__(self):
        self.couleur="rouge"
    def getCouleur(self):
        """ another doc """
        print("Recuperation de la couleur:")
        return self.couleur        
if __name__=="__main__":
    mv=Voiture()
    print(mv.__doc__)
    print(mv.getCouleur.__doc__)
