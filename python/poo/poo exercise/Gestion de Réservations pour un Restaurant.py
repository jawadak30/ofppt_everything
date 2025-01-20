# Structure de données pour les tables et les clients
lstables = []
lsclients = []

# Fonctions pour gérer les tables
def ajouter_table(numero, capacite):
    lstables.append({'numero': numero, 'capacite': capacite, 'reservee': False})

def afficher_tables():
    for table in lstables:
        for key, value in table.items():
            print(f"{key}: {value}")

def rechercher_table(numero):
    for table in lstables:
        if table['numero'] == numero:
            return table

# Fonctions pour gérer les clients
def enregistrer_client(nom):
    lsclients.append({'nom': nom, 'numero_table': None})

def chercher_client(nom):
    for client in lsclients:
        if client['nom'] == nom:
            return client
    return None

def reserver_table():
    nom = input("Entrez votre nom : ")
    client = chercher_client(nom)
    if client:
        numero = int(input("Entrez le numéro de la table que vous voulez réserver : "))
        table = rechercher_table(numero)
        if table and not table['reservee']:
            table['reservee'] = True
            client['numero_table'] = numero
            print(f"La table {numero} a été réservée avec succès par {nom}.")
        else:
            print("Cette table n'est pas disponible.")
    else:
        print("Client inexistant.")

def liberer_table(numero):
    table = rechercher_table(numero)
    if table and table['reservee']:
        table['reservee'] = False
        print(f"La table {numero} a été libérée.")
    else:
        print("Cette table n'est pas réservée actuellement.")

# Boucle principale du programme
def main():
    while True:
        print("\nActions disponibles :")
        print("1: Ajouter une table")
        print("2: Afficher les tables")
        print("3: Rechercher une table")
        print("4: Enregistrer un client")
        print("5: Réserver une table")
        print("6: Libérer une table")
        print("7: Quitter")

        choix = input("Entrez le numéro de l'action que vous voulez effectuer : ")

        if choix == '1':
            numero = int(input("Entrez le numéro de la table : "))
            capacite = int(input("Entrez la capacité de la table : "))
            ajouter_table(numero, capacite)
        elif choix == '2':
            afficher_tables()
        elif choix == '3':
            numero = int(input("Entrez le numéro de la table à rechercher : "))
            table = rechercher_table(numero)
            if table:
                print("La table est " + ("réservée" if table['reservee'] else "disponible"))
            else:
                print("La table n'est pas dans le restaurant.")
        elif choix == '4':
            nom = input("Entrez le nom du client : ")
            enregistrer_client(nom)
        elif choix == '5':
            reserver_table()
        elif choix == '6':
            numero = int(input("Entrez le numéro de la table à libérer : "))
            liberer_table(numero)
        elif choix == '7':
            break
        else:
            print("Choix non valide, veuillez réessayer.")

if __name__ == "__main__":
    main()
