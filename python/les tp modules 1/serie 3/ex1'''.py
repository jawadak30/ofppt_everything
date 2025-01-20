n=int(input("saisir un nombre: "))
s=1
for i in range(1,n+1):
    s=s+(-1)**i/(i*2)
print(s)