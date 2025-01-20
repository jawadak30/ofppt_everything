def factoriel(n) :
    s=0
    for i in range(1,n-1) :
        n=s+n*i
    print(n)
    return(n)
n=int(input("saisir un nombre: "))
factoriel(n)