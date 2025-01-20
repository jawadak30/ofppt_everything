class AlbumMusical:
    def __init__(self,titre,genre,anné):
        self.titre=titre
        self.genre=genre
        self.anné=anné
    def afficher(self):
        print("le,titre est: ",self.titre,"le genre est: ",self.genre,"l'anné est: ",self.anné)
    def __str__(self):
        return("le,titre est: "+self.titre+"le genre est: "+self.genre+"l'anné est: "+str(self.anné))
class musicien:
    def __init__(self,ID, nom, albums):
        self.ID=ID
        self.nom=nom
        self.albums=albums
        self.thislist=[]
    def affichage(self):
        print("donner le id de l'album: ",self.ID,"donner le nom : ",self.nom,"donner l'album: ",self.albums)
    def __str__(self):
        return("donner le id de l'album: "+str(self.ID)+"donner le nom : "+self.nom+"donner l'album: "+self.albums)
    def ajouter(self):
        a=str(input("saisir le titre de l'alnbum: "))
        b=str(input("saisir le genre: "))
        c=int(input("saisir l'anné : "))
        f=AlbumMusical(a,b,c)
        self.thislist.append(f)
        f.afficher()