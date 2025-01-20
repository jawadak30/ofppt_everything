n=int(input("saisir la langueur de la liste: "))
a=int(input("saisir un nombre: "))
thislist=[]
for i in range(0,n+1):
   thislist.append(a)
   a=int(input("saisir un nombre: "))
for i in range(1,n) :
   if thislist[i]==thislist[i] :
        del thislist[i]
   print(thislist)