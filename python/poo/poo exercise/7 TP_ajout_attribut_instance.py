class Voiture:
    def __init__(self):
        self.couleur="red"
    def __str__(self):
        return "couleur:"+self.couleur
if __name__=="__main__":
    v1=Voiture()
    print(v1)
    print(v1.__dict__)
    v2=Voiture()
    v2.marque="audi"
    print(v2)
    print(v2.__dict__)
    v3=Voiture()
    print(v3)
    print(v3.__dict__)
    
    
    
