class Personne:
    code = 0  # Attribut de classe pour l'auto-incrémentation

    def __init__(self,nom):
        self.nom=nom
        Personne.code += 1  # Incrémenter le compteur pour chaque nouvelle instance
        self.id = Personne.code    # Affecter l'id unique à l'instance
    def __str__(self):
        return "nom: "+self.nom+" code: "+str(self.id)

p1 = Personne("n1")

p2 = Personne("n2")

p3 = Personne("n3")

print(p1)
print(p2)
print(p3)

  
  
  
