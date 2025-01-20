n=int(input("saisir un nombre: "))
UPP=2
UP=3
print("le therme 1 est: ",UPP)
print("le therme 2 est: ",UP)
for i in range(3,n+1):
    U=UPP+(-1)*i*UP
    UP=U
    UPP=UP
    print("le thermes",i,"est: ",U)