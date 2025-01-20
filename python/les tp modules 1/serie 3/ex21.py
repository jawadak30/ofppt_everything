a=int(input("saisir le jour: "))
b=int(input("saisir le mois: "))
c=int(input("saisir l'année: "))
if b==2 :
    if a>=28 :
        e=b+1
        a=1
        c=c
        print(a,"/",e,"/",c)
    elif a>=1 :
        a=a+1
        b=b
        c=c
        print(a,"/",b,"/",c)
else :
    if a>=1 :
        if a<=29 :
           f=a+1
           b=b
           c=c
           print(f,"/",b,"/",c)
        else :
           g=b+1
           a=1
           c=c
           print(a,"/",g,"/",c)
           if b==12 :
               r=1
               a=1
               c=c+1
               print(a,"/",r,"/",c)
