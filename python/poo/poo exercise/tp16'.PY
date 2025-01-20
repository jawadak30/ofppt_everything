import datetime

class Employe:
    nombre_employes = 0

    def __init__(self, nom, prenom):
        Employe.nombre_employes += 1
        self.numero_matricule = Employe.nombre_employes
        self.nom = nom
        self.prenom = prenom
        self.date_embauche = datetime.date.today()
        self.solde_conges = 30  # Exemple de solde initial

    def __str__(self):
        return f"Matricule: {self.numero_matricule}, Nom: {self.nom}, Prénom: {self.prenom}, Date d'embauche: {self.date_embauche}, Solde de congés: {self.solde_conges}"

class Manager(Employe):
    def __init__(self, nom, prenom, code_manager):
        super().__init__(nom, prenom)
        self.code_manager = code_manager
        self.employes = []

    def __str__(self):
        return f"Matricule: {self.numero_matricule}, Nom: {self.nom}, Prénom: {self.prenom}, Code Manager: {self.code_manager}"

    def liste_employes(self):
        return [employe.nom for employe in self.employes]

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def get_employe_by_code(self, code):
        for employe in self.employes:
            if employe.numero_matricule == code:
                return employe
        return None

    def trier_employes(self):
        self.employes.sort(key=lambda x: x.nom)

class DemandeConge:
    def __init__(self, code_employe, date_debut, duree, motif):
        self.code_employe = code_employe
        self.date_debut = date_debut
        self.duree = duree
        self.motif = motif
        self.etat = "En cours"

    def valider(self):
        self.etat = "Validé"

    def refuser(self):
        self.etat = "Refusé"

class GestionConge:
    def __init__(self):
        self.managers = []
        self.demandes_conge = []

    def ajouter_demande_conge(self, demande):
        self.demandes_conge.append(demande)

    def liste_demande_conge_en_cours(self):
        return [demande for demande in self.demandes_conge if demande.etat == "En cours"]

    def liste_demande_conge_par_employe(self, code_employe):
        return [demande for demande in self.demandes_conge if demande.code_employe == code_employe]

    def liste_demande_conge_par_manager(self, code_manager):
        manager = next((mgr for mgr in self.managers if mgr.numero_matricule == code_manager), None)
        if manager:
            employes_manager = manager.employes
            return [demande for demande in self.demandes_conge if demande.code_employe in [emp.numero_matricule for emp in employes_manager]]
        return []

    def duree_total_conge(self):
        duree_total = {}
        for demande in self.demandes_conge:
            if demande.code_employe not in duree_total:
                duree_total[demande.code_employe] = demande.duree
            else:
                duree_total[demande.code_employe] += demande.duree
        return duree_total