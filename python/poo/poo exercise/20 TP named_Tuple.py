from collections import namedtuple #importation de la classe namedtuple du module collections
"""Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22) # instanciation par position ou en utilisant le nom du champs
print(p[0] + p[1]) # les champs sont accessibles par leurs indexes affiche :33
print(p.x + p.y) # les champs sont accessibles par nom affiche 33
print(p) # lisible dans un style nom=valeur affiche Point(x=11,y=22)"""


class Personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def AfficherInfos(self):
        print("nom : ", self.nom, " age : ",self.age)
class Stagiaire:
    def __init__(self, numinscri, filiere):
        self.numinscri=numinscri
        self.filiere=filiere
    def AfficherInfos(self):
        print("num inscription : ", self.numinscri, "filierer: ", self.filiere)
p1=Personne("nom1",20)
p2=Personne("nom2",30)
s1=Stagiaire(1111,"fil1")
L= namedtuple('Per_Stg',['Per','Stg'])
l=L((p1,p2),s1)
print("test namedtuple:")
for e in l.Per:
    e.AfficherInfos()
l.Stg.AfficherInfos()
"""Point = namedtuple ('Point',['x','y'])
print(Point._fields) #retourne les noms de champs affiche: (‘x’,’y’)
Color =namedtuple ('Color', ['red','green', 'blue'])
Pixel= namedtuple ('Pixel', Point._fields + Color._fields) #on crée un nouveau tuple
avec les champs de point et de color
print(Pixel(11,22,128,266,0)) #affiche: Pixel(x=11, y=22, red=128, green=266, blue=0)
"""