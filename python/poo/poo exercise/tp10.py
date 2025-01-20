class joueur:
    def __init__(self,nom=None,age=None,position=None):
        self.nom=nom
        self.age=age
        self.position=position
        self.experimente="expiremente"
    def CalculerPrime(self,match):
        s=0
        i=0
        while match=="interieure":
            r=r+1
            primetotal=s+20000*r
            if self.experimente==True:
                primetotal=primetotal+primetotal*0.5
            return("le prime total des matvh interieure est:",primetotal)
        while match=="exterieure":
            i=i+1
            primetotal=s+30000*i
            if self.experimente==True:
                primetotal=primetotal+primetotal*0.5
        return("le prime total est ",primetotal)
class international(joueur):
    def __init__(self,)