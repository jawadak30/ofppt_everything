import datetime
class Personne:
    def __init__(self, n, p,d):
        self._nom=n # protected
        self.__prenom=p #private
        self.dateNaissance= d #public
class Eleve(Personne):
    def __init__(self,n,p,d,notes,fil):
        super().__init__(n,p,d)
        self.notes=notes
        self.filiere=fil
    def afficher(self):
        print("date naissance:",self.dateNaissance)
        print("nom:", self._nom)
        #print("prenom:",self.__prenom)
p=Personne("n1","p1",datetime.date(2022,5,24))
print("date naissance de la personne:",p.dateNaissance)
print("nom de la personne:", p._nom)
#print("prenom de la personne:", p.__prenom)
print("prenom de la personne:", p._Personne__prenom)
"""e=Eleve("n2","p2",datetime.date(2022,5,25),[14,13,16],"dev")
e.afficher()"""
