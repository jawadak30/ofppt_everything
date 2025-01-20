class Calcul:
    num1 = 10                       #attribut de classe
    def __init__(self, num2):
        self.num2 = num2            #attribut d'instance
    def mtd_instance(self, num3):
        print("Une méthode normale.")
        return self.num1 + self.num2 + num3
    @classmethod
    def mtd_class(cls, num3):
        print("Une methode de classe.")
        return cls.num1 + num3
    @staticmethod
    def mtd_statique(num3):
        print("Une methode statique.")
        return num3

"""obj = Calcul(20)
print(obj.mtd_instance(30))"""
obj1 = Calcul(20)
"""print(obj1.mtd_class(30))
print(Calcul.mtd_class(30))"""
print(obj1.mtd_statique(30))
print(Calcul.mtd_statique(30))

