class Person :
    def __init__(self,code,name,prenom):
         self.__code = code
         self.__name = name 
         self.__prenom = prenom
    def __str__(self):
         return("code"+self.__code+"name"+self.__name+"prenom"+self.__prenom)
    @property
    def code(self):
         return self.__code
    @code.setter
    def code(self, code):
         self.__code = code
p=Person("c1","ahmed","said")
var=p.code
print(var)
p.code="c3"
print(p.code)