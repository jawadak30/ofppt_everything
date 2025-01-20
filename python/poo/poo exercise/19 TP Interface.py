from abc import abstractmethod
class Comparable:
  @abstractmethod
  def CompareTo():
     pass
# les classes qui implémentent l'interface :
class Personne(Comparable):
   def __init__(self,nom,age):
      self.__nom=nom
      self.__age=age
   def CompareTo(self,p):
      if self.__age==p.__age:
         return True
      else:
         return False
class Outils(Comparable):
  def __init__(self, long, prix):
    self.__longueur=long
    self.__prix=prix
  def CompareTo(self,o):
    if self.__longueur==o.__longueur:
       return True
    else:
       return False
#objets
p1=Personne("n1",20)
p2=Personne("n2",20)
o1=Outils(60,450)
o2=Outils(60,450)
if (p1.CompareTo(p2)):
   print("ont le meme age")
else:
   print("ages différents")
if (o1.CompareTo(o2)):
   print("meme longueur")
else:
   print("longueurs différents")
