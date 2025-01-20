notes=[12,4,14,11,18,13,7,10,5,9,15,8,14,16]
thislist=[]
for i in range(0,14) :
    if notes[i]>10 :
        thislist.append(notes[i])
print("les valeurs superieures à 10 sont: ",thislist)