class appareil:
    def __init__(self,reference,puissance,poids,prix):
        self.reference=reference
        self.puissance=puissance
        self.poids=poids
        self.prix=prix
    def __str__(self):
        return("le reference est: "+self.reference+"la puissance est: "+str(self.puissance)+"w "+
               "le poids est: "+str(self.poids)+"le prix est: "+str(self.prix))
    def classe_Eneergetique(self):
        if self.puissaance>1000:
            print("la classe est: C")
        elif self.puissaance>300:
            print("la classe est: B")
        else:
            print("la classe est: A")
class tv(appareil):
    def __init__(self,reference,puissance,poids,prix,type,frequency):
        super().__init__(reference,puissance,poids,prix)
        self.type=type
        self.frequency=frequency
    def __str__(self):
        appareil.__str__()
        return("le type est: "+self.type+"le frequence est: "+str(self.frequency)+"hz")
class velo(appareil):
    def __init__(self,reference,puissance,poids,prix,distance):
        super().__init__(reference,puissance,poids,prix)
        self.distance=distance
    def rouler(self):
        s=0
        if self.distance==1000:
            s=s+1
        return("le kilomitrage est: ",s)
    def charge(self):
        a=int(input("saisir le nombre des heures que tu attende pour la charge: "))
        if self.puissance !=0:
            print("le velo se charger")
            c=0
            while True:
                a=a-1
                c=c+10
                if a==0:
                    break
            return("l'autonomie est : ",c,"km")
        else:
            print("la charge est stoper")
    def __str__(self):
        return("le reference est: "+self.reference+"la puissance est: "+str(self.puissance)+"w "+
               "le poids est: "+str(self.poids)+"le prix est: "+str(self.prix))
reference=input("saisir le réference: ")
puissance=int(input("saisir la puissance: "))
poids=input("saisir le poids: ")
prix=int(input("saisir le prix: "))
distance=int(input("saisir la distance en m: "))
v=velo(reference,puissance,poids,prix,distance)
print(v)
print(v.charge())
print(v.rouler())

