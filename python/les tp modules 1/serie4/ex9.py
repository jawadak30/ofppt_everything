moyennes=float=[14.84,14.14,16.22,8.85,14.84,13,15.85,9.99,12.04,15.03,16.22,12.84,10.20,11.03]
max=moyennes[0]
min=moyennes[0]
for j in range(0,3):
    for i in range(1,14) :
        if min<i :
            moyennes==min
        if max>i :
            moyennes==max
    print("les trois valeurs les plus grand sont: ",moyennes)
    print("les valeurs minimales sont : ",moyennes)