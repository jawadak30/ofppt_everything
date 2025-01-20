class ville:
    def __init__(self,nom,population):
        self.__nom=nom
        self.__population=population
    def __str__(self):
        return("le nom de la ville est: "+self.__nom+"la population est: "+str(self.__population))
class pays:
    def __init__(self,nom,capitale):
        self.list=[]
        self.nom=nom
        self.capitale=capitale
    def Ajouter_ville(self,vil):
        if vil not in self.list:
            self.list.append(vil)
            for val in self.list:
                print(val)
        else:
            print("cette ville existe ")
    def Nombres_ville(self,vil):
        self.list.append(vil)
        s=0
        for vil in self.list:
            s=s+1
        print("le nombre des ville est: ",s)
    def Rechercher(self,vil):
        if vil in self.list:
            return("la ville que tu cherche existe ")
        else:
            return(-1)
    def Supprimer_ville(self,vil):
        if vil==ville.self.list:
            del self.list[ville]
        return(self.list)
    def Trier_par_population(self,population):
        self.list.sort(population)
        return(self.list)
    def Population_total(self,population):
        if population is not None:
            return(sum(population))
vill=pays("msdsd",12)
nbr=int(input("saisir le nombre des ville: "))
for i in range(nbr):
    nom=str(input("saisir le nom de la ville : "))
    population=int(input("saisir le nombre de la population: "))
    vil=ville(nom,population)
vill.Ajouter_ville(vil)