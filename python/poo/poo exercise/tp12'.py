class Equipement:
    def __init__(self, code, date_acquisition, etat, prix_achat):
        self.code = code
        self.date_acquisition = date_acquisition
        self.etat = etat
        self.prix_achat = prix_achat

    def __str__(self):
        return f"Code: {self.code}, Date d'acquisition: {self.date_acquisition}, État: {self.etat}, Prix d'achat: {self.prix_achat}"


class Ordinateur(Equipement):
    def __init__(self, code, date_acquisition, etat, prix_achat, marque, taille_ecran):
        super().__init__(code, date_acquisition, etat, prix_achat)
        self.marque = marque
        self.taille_ecran = taille_ecran

    def __str__(self):
        return super().__str__() + f", Marque: {self.marque}, Taille de l'écran: {self.taille_ecran}"


class Table(Equipement):
    def __init__(self, code, date_acquisition, etat, prix_achat, longueur, largeur):
        super().__init__(code, date_acquisition, etat, prix_achat)
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        return super().__str__() + f", Longueur: {self.longueur}, Largeur: {self.largeur}"


class Chaise(Equipement):
    def __init__(self, code, date_acquisition, etat, prix_achat, couleur):
        super().__init__(code, date_acquisition, etat, prix_achat)
        self.couleur = couleur

    def __str__(self):
        return super().__str__() + f", Couleur: {self.couleur}"


class Bureau:
    def __init__(self, code, description):
        self.code = code
        self.description = description
        self.equipements = []

    def __str__(self):
        return f"Code du bureau: {self.code}, Description: {self.description}, Nombre d'équipements: {len(self.equipements)}"

    def ajouterEquipement(self, equipement):
        self.equipements.append(equipement)

    def rechercheEquipement(self, code):
        for equipement in self.equipements:
            if equipement.code == code:
                return equipement
        raise Exception(f"L'équipement avec le code {code} n'a pas été trouvé dans ce bureau.")

    def ficheInventaire(self):
        for equipement in self.equipements:
            print(equipement)

    def supprimerEquipement(self, code):
        equipement = self.rechercheEquipement(code)
        self.equipements.remove(equipement)


class Entreprise:
    def __init__(self, nom, adresse, telephone):
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.bureaux = []

    def __str__(self):
        return f"Nom de l'entreprise: {self.nom}, Nombre de bureaux: {len(self.bureaux)}"

    def ajouterBureau(self, bureau):
        self.bureaux.append(bureau)

    def rechercheEquipement(self, code):
        for bureau in self.bureaux:
            try:
                return bureau.rechercheEquipement(code)
            except Exception:
                pass
        raise Exception(f"L'équipement avec le code {code} n'a pas été trouvé dans l'entreprise.")

    def localisation(self, code):
        for bureau in self.bureaux:
            try:
                equipement = bureau.rechercheEquipement(code)
                print(f"L'équipement avec le code {code} est dans le bureau: {bureau.code}")
                return
            except Exception:
                pass
        print(f"L'équipement avec le code {code} n'a pas été trouvé dans l'entreprise.")

    def transferEquipement(self, code, bureau_source, bureau_destination):
        equipement = bureau_source.rechercheEquipement(code)
        bureau_source.supprimerEquipement(code)
        bureau_destination.ajouterEquipement(equipement)

    def exporter(self, fichier):
        with open(fichier, 'w') as f:
            for bureau in self.bureaux:
                f.write(f"{bureau.code}, {bureau.description}\n")
                for equipement in bureau.equipements:
                    f.write(f"{equipement.code}, {equipement.date_acquisition}, {equipement.etat}, {equipement.prix_achat}\n")
            print(f"Données exportées avec succès dans le fichier {fichier}")


# Exemple d'utilisation
if __name__ == "__main__":
    ordinateur1 = Ordinateur("001", "01/01/2023", "Opérationnel", 1000, "HP", 15)
    table1 = Table("002", "01/02/2023", "Opérationnel", 500, 120, 80)
    chaise1 = Chaise("003", "01/03/2023", "Non opérationnel", 50, "Bleu")

    bureau1 = Bureau("B001", "Bureau principal")
    bureau1.ajouterEquipement(ordinateur1)
    bureau1.ajouterEquipement(table1)
    bureau1.ajouterEquipement(chaise1)

    entreprise1 = Entreprise("Mon Entreprise", "123 Rue Principale", "0123456789")
    entreprise1.ajouterBureau(bureau1)

    print(entreprise1)
    print(bureau1)
    print(bureau1.rechercheEquipement("002"))
    entreprise1.localisation("002")

    fichier_export = "donnees_exportees.txt"
    entreprise1.exporter(fichier_export)