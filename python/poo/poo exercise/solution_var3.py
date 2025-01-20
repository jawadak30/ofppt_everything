# creating lists

lschambres = []
lsclients = []


# print all rooms info
def afficher_chambres():
    if len(lschambres) == 0:
        print("== Pas de chambres!")
        return
    print("== LISTES DES CHAMBRES:")
    for chambre in lschambres:
        for key, value in chambre.items():
            print(f"- {key} : {value}")

        print("*" * 20)


# search for a room
def rechercher_chambre(numero_chambre):
    for chambre in lschambres:
        if chambre["numero_chambre"] == numero_chambre:
            return chambre
    return None


# add a room to the list
def ajouter_chambre(numero_chambre, type_chambre, prix_par_nuit):
    if rechercher_chambre(numero_chambre):
        print("== Chambre deja existe")
    else:
        chambre = dict(
            numero_chambre=numero_chambre,
            type_chambre=type_chambre,
            prix_par_nuit=prix_par_nuit,
            reservee=False,
        )
        lschambres.append(chambre)


# search clients list
def chercher_client(cin):
    for client in lsclients:
        if client["cin"] == cin:
            return client
    return None


# add a client
def ajouter_client(cin):
    if chercher_client(cin):
        print("== Client deja existe")
    else:
        client = dict(cin=cin, numero_chambre="")
        lsclients.append(client)


# reserve a room
def reserver_chambre():
    cin = input(
        "Entrer votre cin svp: "
    )  # we suppose that the cin is a string e.g: "T28374"
    client = chercher_client(cin)
    if client:
        numero_chambre = input("Entrer num de chambre svp: ")
        chambre = rechercher_chambre(numero_chambre)
        if chambre:
            if not chambre["reservee"]:
                chambre["reservee"] = True
                client["numero_chambre"] = numero_chambre
                print("== La chambre a ete reservee")
            else:
                print("== La chambre est deja reservee")
        else:
            print("== La chambre n'existe pas")
    else:
        print("== Ce client n'existe pas")


# make a room available again
def retourner_chambre(numero_chambre):
    chambre = rechercher_chambre(numero_chambre)
    if chambre and chambre["reservee"]:
        # empty the "numero_chambre" from client dictionary
        for client in lsclients:
            if client["numero_chambre"] == numero_chambre:
                client["numero_chambre"] = ""
        chambre["reservee"] = False
        print("== La chambre est liberee")
    else:
        print("== La chambre n'existe pas")


# calculate the costs
def calcule_facture(nbr, numero_chambre):
    chambre = rechercher_chambre(numero_chambre)
    if chambre:
        if chambre["reservee"]:
            return nbr * chambre["prix_par_nuit"]
        else:
            print("== La chambre n'est reservee")
            return None
    else:
        print("== La chambre n'existe pas")
        return None


# main
def main():
    print("=" * 40)
    print("GESTION DES CHAMBRES D'HOTELS".center(40))
    print("=" * 40)
    while True:
        print()
        print("MENU")
        print("-" * 20)
        print("1: AJOUTER UNE CHAMBRE")
        print("2: AFFICHER LES CHAMBRES")
        print("3: RESERVER UNE CHAMBRE")
        print("4: RETOURNER UNE CHAMBRE")
        print("5: AJOUTER UN CLIENT")
        print("6: CALCULER LA FACTURE")
        print("0: QUITTER")
        try:
            choice = int(input("Choisir votre choix: "))
        except:
            print("== Mauvaise Entree!")
            continue
        match (choice):
            case 1:
                numero_chambre = input("Entrer le num de chambre: ")
                type_chambre = input("Entrer type de chambre: ")
                prix_par_nuit = int(input("Entrer le prix de la chambre: "))
                ajouter_chambre(numero_chambre, type_chambre, prix_par_nuit)
            case 2:
                afficher_chambres()
            case 3:
                reserver_chambre()
            case 4:
                numero_chambre = input("Entrer le numero de la chambre: ")
                retourner_chambre(numero_chambre)
            case 5:
                cin = input("Entrer votre cin: ")
                ajouter_client(cin)
            case 6:
                nbr = int(input("Entre le nombre de nuits: "))
                numero_chambre = input("Entrer le numero de la chambre: ")
                facture = calcule_facture(nbr, numero_chambre)
                if facture:
                    print(f"Votre facture est {facture}")
            case 0:
                break
            case _:
                print("Mauvais choix!")


if __name__ == "__main__":
    main()
