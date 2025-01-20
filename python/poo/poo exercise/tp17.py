from datetime import date
class client:
    def __init__(self,code,client,nom,adresse,tel,email):
        self.code=code
        self.client=client
        self.nom=nom
        self.adresse=adresse
        self.tel=tel
        self.email=email
    def __str__(self):
        return("le code de client est: "+str(self.code)+"le client est: "+self.client+"le nom du client est: "+self.nom+"l'adrsse du client est: "+self.adresse+"le telephone est: "+str(self.tel)+"l'email du client est: "+self.email)
class produit:
    def __init__(self,reference,designation,prixunitaire,quantiteenstock):
        self.reference=reference
        self.designation=designation
        self.prixunitaire=prixunitaire
        self.quantiteenstock=quantiteenstock
    def __str__(self):
        return ("le reference est: "+self.reference+"le designation est: "+self.designation+"le prix unitaire est: "+self.prixunitaire+"la quantite en stock est: "+str(self.quantiteenstock))
class comande:
    numberofcomande=1000
    def __init__(self,cclient=None,datedecomade=None):
        self.numberofcomande +=1
        self.cclient=cclient
        self.datedecomande=datedecomade
        self.datedesysteme=date.today()
        self.ls_produits=[]
        self.ls_quantite=[]
    def TotalCommande(self,prixunitaire,quantiteenstock):
        self.somme=prixunitaire*quantiteenstock
        return "la somme total est: "+self.somme
    # def ajouterproduit()
    def __str__(self):
        return ("le numero de la commande: "+str(self.numberofcomande)+" le client est: "+self.cclient+"la date de la commande: "+self.datedecomande+"la date d'aujord'hui est: "+self.datedesysteme)
