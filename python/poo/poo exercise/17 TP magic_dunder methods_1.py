#magic method
#dunder method
#special method

y=12
z=15
#1. t=y+z # addition ou concaténation
#2. les méthodes __xx__ : magic ou  double underscore méthodes
t=int.__add__(y,z)
print(t)
x=y*3 # multiplication ou réplication
#c'est une surchage des opérateurs
