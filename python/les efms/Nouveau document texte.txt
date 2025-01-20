def ajouter_chambre(numero_chambre,type_chambre,prix_par_nuit):
    lschambres.append(chambre)
    print(lschambres)
def afficher_chambre():
    for item in chambre:
        print(item)
def rechercher_chambre(numero_chambre):
    numero_chambre=int(input("saisir le numero de chambre pour afficher s'il existe: "))
    for numero_chambre in chambre:
        if numero_chambre in chambre:
            return(numero_chambre)
        else:
            b="vide"
            return(b)
def ajouter_client(cin):
    lsclient.append(client)
def chercher_client(cin):
    cin=int(input("saisir le cin du clirnt pour le chercher: "))
    if cin in lsclient:
        return(cin)
    else:
        c="aucun client"
        return(c)
def reserver_chambre():
    cin=int(input("saisirle cin de client pour reserver la chambre: "))
    if cin==cin:
        print("la sale reserve")
    else:
        print("la salle est vide")
lschambres=[]
lsclient=[]
for i in range(0,2):
    numero_chambre=int(input("saisir le numero de chambre: "))
    type_chambre=str(input("saisir le type de chambre: "))
    prix_par_nuit=int(input("saiisr le prix de chambre: "))
    chambre={"numero_chambre":numero_chambre,"type de chambre":type_chambre,"prix par nuit":prix_par_nuit}
ajouter_chambre(numero_chambre,type_chambre,prix_par_nuit)
afficher_chambre()
print("le numero de chmbre chercher est: ",rechercher_chambre(numero_chambre))
for i in range(0,2):
    cin=int(input("saisir le cin de client: "))
    client={"le cin de client":cin,"numero_chambre":"   "}
ajouter_client(cin)
print("le client chercher: ",chercher_client(cin))