class Employe:
    def __init__(self, ID, Nom, Prenom):
        self.ID = ID
        self.Nom = Nom
        self.Prenom = Prenom

    def get_ID(self):
        return self.ID

    def get_Nom(self):
        return self.Nom

    def get_Prenom(self):
        return self.Prenom

    def __str__(self):
        return f"Employé(ID={self.ID}, Nom={self.Nom}, Prénom={self.Prenom})"


class Salle:
    def __init__(self, Numero, Nom, Capacite):
        self.Numero = Numero
        self.Nom = Nom
        self.Capacite = Capacite

    def get_Numero(self):
        return self.Numero

    def get_Nom(self):
        return self.Nom

    def get_Capacite(self):
        return self.Capacite

    def __str__(self):
        return f"Salle(Numéro={self.Numero}, Nom={self.Nom}, Capacité={self.Capacite})"


class Reservation:
    numero_reservation_autoincrement = 1

    def __init__(self, employe, salle, date_debut, date_fin, objectif_reunion):
        self.numero_reservation = Reservation.numero_reservation_autoincrement
        self.employe = employe
        self.salle = salle
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.objectif_reunion = objectif_reunion

    def get_numero_reservation(self):
        return self.numero_reservation

    def get_employe(self):
        return self.employe

    def get_salle(self):
        return self.salle

    def get_date_debut(self):
        return self.date_debut

    def get_date_fin(self):
        return self.date_fin

    def get_objectif_reunion(self):
        return self.objectif_reunion

    def __str__(self):
        return f"Réservation(N° {self.numero_reservation}, Employé: {self.employe}, " \
               f"Salle: {self.salle}, Date début: {self.date_debut}, Date fin: {self.date_fin}, " \
               f"Objectif: {self.objectif_reunion})"


class GestionReservations:
    def __init__(self):
        self.employes = []
        self.salles = []
        self.reservations = []

    def AjouterEmploye(self, employe):
        if not any(e.get_ID() == employe.get_ID() for e in self.employes):
            self.employes.append(employe)
            print(f"Employé ajouté: {employe}")
        else:
            print(f"Un employé avec le même ID ({employe.get_ID()}) existe déjà.")

    def AfficherEmployes(self):
        print("Liste des employés:")
        for employe in self.employes:
            print(employe)

    def AjouterSalle(self, salle):
        if not any(s.get_Numero() == salle.get_Numero() for s in self.salles):
            self.salles.append(salle)
            print(f"Salle ajoutée: {salle}")
        else:
            print(f"Une salle avec le même numéro ({salle.get_Numero()}) existe déjà.")

    def AfficherSalles(self):
        print("Liste des salles:")
        for salle in self.salles:
            print(salle)

    def AjouterReservation(self, reservation):
        employe_id = self.RechercherEmploye()
        salle_numero = self.RechercherSalle()

        if employe_id is not None and salle_numero is not None:
            employe = self.RechercherPersonne(employe_id, self.employes)
            salle = self.RechercherPersonne(salle_numero, self.salles)

            reservation = Reservation(employe, salle, reservation.get_date_debut(), reservation.get_date_fin(), reservation.get_objectif_reunion())
            self.reservations.append(reservation)
            print(f"Réservation ajoutée: {reservation}")

            Reservation.numero_reservation_autoincrement += 1

    def RechercherPersonne(self, personne_id, liste_personnes):
        for personne in liste_personnes:
            if isinstance(personne, Employe) and personne.get_ID() == personne_id:
                return personne
            elif isinstance(personne, Salle) and personne.get_Numero() == personne_id:
                return personne
        return None

    def RechercherEmploye(self):
        while True:
            employe_id = int(input("Saisir l'ID de l'employé: "))
            if self.RechercherPersonne(employe_id, self.employes):
                return employe_id
            else:
                print("Employé non trouvé. Veuillez saisir un autre ID.")

    def RechercherSalle(self):
        while True:
            salle_numero = input("Saisir le numéro de la salle: ")
            if self.RechercherPersonne(salle_numero, self.salles):
                return salle_numero
            else:
                print("Salle non trouvée. Veuillez saisir un autre numéro.")

    def RechercherReservation(self):
      while True:
        reservation_numero = int(input("Saisir le numéro de la réservation: "))
        for reservation in self.reservations:
             if reservation.get_numero_reservation() == reservation_numero:
                print(f"Réservation trouvée: {reservation}")
                return reservation_numero
             print("Réservation non trouvée. Veuillez saisir un autre numéro.")




if __name__ == "__main__":
    gestion_reservations = GestionReservations()

    while True:
        print("\nMenu:")
        print("1. Ajouter un employé")
        print("2. Afficher la liste des employés")
        print("3. Ajouter une salle")
        print("4. Afficher la liste des salles")
        print("5. Ajouter une réservation")
        print("6. Rechercher un employé")
        print("7. Rechercher une salle")
        print("8. Rechercher une réservation")
        print("9. Afficher la liste des réservations")
        print("10. Quitter")

        choix = input("Veuillez choisir une option (1-10): ")

        if choix == "1":
            id_employe = int(input("Saisir l'ID de l'employé: "))
            nom_employe = input("Saisir le nom de l'employé: ")
            prenom_employe = input("Saisir le prénom de l'employé: ")
            employe = Employe(id_employe, nom_employe, prenom_employe)
            gestion_reservations.AjouterEmploye(employe)
        elif choix == "2":
            gestion_reservations.AfficherEmployes()
        elif choix == "3":
            numero_salle = input("Saisir le numéro de la salle: ")
            nom_salle = input("Saisir le nom de la salle: ")
            capacite_salle = int(input("Saisir la capacité de la salle: "))
            salle = Salle(numero_salle, nom_salle, capacite_salle)
            gestion_reservations.AjouterSalle(salle)
        elif choix == "4":
            gestion_reservations.AfficherSalles()
        elif choix == "5":
            date_debut = input("Saisir la date de début de la réservation (format YYYY-MM-DD HH:MM): ")
            date_fin = input("Saisir la date de fin de la réservation (format YYYY-MM-DD HH:MM): ")
            objectif_reunion = input("Saisir l'objectif de la réunion: ")
            reservation = Reservation(None, None, date_debut, date_fin, objectif_reunion)
            gestion_reservations.AjouterReservation(reservation)
        elif choix == "6":
            employe_id = gestion_reservations.RechercherEmploye()
            print(f"Employé trouvé: {gestion_reservations.RechercherPersonne(employe_id, gestion_reservations.employes)}")
        elif choix == "7":
            salle_numero = gestion_reservations.RechercherSalle()
            print(f"Salle trouvée: {gestion_reservations.RechercherPersonne(salle_numero, gestion_reservations.salles)}")
        elif choix == "8":
            reservation_numero = gestion_reservations.RechercherReservation()
            print(f"Réservation trouvée: {gestion_reservations.RechercherPersonne(reservation_numero, gestion_reservations.reservations)}")
        elif choix == "9":
            gestion_reservations.AfficherReservations()
        elif choix == "10":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez saisir un nombre entre 1 et 10.")
