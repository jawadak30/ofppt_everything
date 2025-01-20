class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    # Constructeur de copie
    def __copy__(self):
        return type(self)(self.nom, self.age)
    def __str__(self):
        return "nom :"+ self.nom +"age :"+ str(self.age)
    

# Création d'un objet
p1 = Personne("Ali", 2)
print("Objet1:",p1)
# Copie de l'objet
import copy
p2 = copy.copy(p1)
print("Objet2:",p2)
# Vérification que l'objet copié est une nouvelle instance
print(p1 is p2)  # False
print(p1 == p2)
print(p1.nom == p2.nom)  # True"""
