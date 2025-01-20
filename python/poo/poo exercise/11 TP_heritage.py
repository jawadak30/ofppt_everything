#classe mère
class Personne:
    def __init__(self,n,p):
        self.nom=n
        self.prenom=p
    def afficherInfos(self):
        print("nom:",self.nom,"prénom:",self.prenom)
#classe fille
class Stagiaire(Personne):   
    def __init__(self,n,p,notes):
        #self.nom=n
        #self.prenom=p
        #Personne.__init__(self,n,p)
        super().__init__(n,p)
        self.notes =notes
    def afficherNotes(self):
        print(self.notes)
    def afficherInfos(self):
        #print("nom:",self.nom,"prénom:",self.prenom)
        #print("notes:",self.notes)
        Personne.afficherInfos(self)
        self.afficherNotes()
        
stg=Stagiaire("n1","p1",10)
stg.afficherInfos()
        
        
      
       


















