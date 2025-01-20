a=float(input("sasir le nombre des heures : "))
prix=10
if a<=39 :
    b=prix*a
    print("le prix est: ",b)
if a>=40 and a<=44 :
    c=(a*prix)+(prix*0.5)
    print("le prix est:",c)
if a>=45 and a<=49 :
    d=(a*prix)+(prix*0.75)
    print("le prix est: ",d)
if a>=50 :
    e=(a*prix)+(prix)
    print("le prix est: ",e)