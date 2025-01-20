class Voiture:
    def __init__(self):
        self.couleur="rouge"
        self.marque="audi"
    def afficher(self):
        print("couleur:", self.couleur)
if __name__=="__main__":
    v = Voiture()
    print(v.__dict__)
