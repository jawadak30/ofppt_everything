def ajouter_chambre(numero_chambre,type_chambre,prix_par_nuit):
    lschambres.append(chambre)
    print(lschambres)
def afficher_chambre():
    for item in chambre:
        print(item)
def rechercher_chambre(numero_chambre):
    numero_chambre=int(input("saisir le numero de chambre pour le trouver: "))
    for keys in chambre:
        if numero_chambre in keys:
           return(numero_chambre)
        else:
            return("objet vide")
def ajouter_client(cin):
    cin=int(input("saisir le cin du client: "))
    lsclients.append(client.get[cin])
    print(lsclients)
def chercher_client(cin):
    if cin in client[cin]:
        return("ce nombre existe ")
    else:
        return("objet vide ")

lschambres=[]
lsclients=[]
for i in range(0,2):
    numero_chambre=int(input("saisir le numero de chambre: "))
    type_chambre=str(input("saisir lr type de chambre: "))
    prix_par_nuit=float(input("saiisr le prix de chambre: ,"))
    chambre={"numero_chambre":numero_chambre,"type_cambre":type_chambre,"prix_par_nuit":prix_par_nuit}
ajouter_chambre(numero_chambre,type_chambre,prix_par_nuit)
afficher_chambre()
for i in range(0,2):
    cin=int(input("saisir le cin du client: "))
    numero_chambre=str("vide")
    client={"le cin du client":cin,"le nummero dr chambre:":numero_chambre}
ajouter_client(cin)
print(chercher_client(cin))