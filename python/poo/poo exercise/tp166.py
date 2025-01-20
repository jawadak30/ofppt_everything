# TP16 - Gestion de demandes de congé

from datetime import date
from enum import Enum
import re

def valid_date_input(msg):
    reg_date = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

    while True:
        my_date = input(msg + "(AAAA-MM-JJ)")
        matches = reg_date.search(my_date)
        if not matches:
            print("date invalide !")
            continue
        try:
            my_date = date.fromisoformat(my_date)
            my_today = date.today()
            if my_date < my_today:
                print("date invalide !")
                continue
            return my_date
        except:
            print("date invalide !")
            continue


def valid_input(msg):
    while True:
        v = input(msg)
        if len(v.strip()) == 0:
            print("Valeur vide !")
            continue
        return v
    

class Employe:
    nombre_employe = 1
    def __init__(self,nom,prenom):
        self.__num_matricule = Employe.nombre_employe
        Employe.nombre_employe += 1
        self.__nom = nom 
        self.__prenom = prenom
        self.__date_embauche = date.today()
        self.__solde_conge = 30
    
    @property
    def num_matricule(self):
        return self.__num_matricule

    @property
    def full_name(self):
        return self.__nom + " " + self.__prenom
    
    def __str__(self) -> str:
        return f"Info de Employe:\nNumero de matricule: {self.__num_matricule}\
            \nNom et Prenom : {self.__nom + " " + self.__prenom}\
            \nDate d'embauche : {self.__date_embauche}\
            \nSolde de Conge : {self.__solde_conge}"
    

class Manager(Employe):
    def __init__(self, nom, prenom,code_manager):
        super().__init__(nom, prenom)
        self.__code_manager = code_manager
        self.__ls_employe = []
    
    @property
    def code_manager(self):
        return self.__code_manager
    
    @property
    def ls_employe(self):
        return self.__ls_employe

    def liste_employe(self):
        if len(self.__ls_employe) == 0:
            print("liste vide!")
        else:
            print("Liste d'employe :")
            for emp in self.__ls_employe:
                print(emp.full_name)
    

    def ajouter_employe(self):
        print("Ajouter employe :")
        nom = valid_input("Entrer le nom")
        prenom = valid_input("Entrer le prenom")
        employe = Employe(nom,prenom)
        self.__ls_employe.append(employe)
        print("Employe ajoutee avec success!")



    def get_employe_by_matricule(self):
        num_matricule = int(valid_input("Entrer numero de matricule :"))
        for emp in self.__ls_employe:
            if emp.num_matricule == num_matricule:
                return emp
        
    
    def trier_employe(self):
        self.__ls_employe.sort(key= lambda emp : emp.full_name)
    
    def __str__(self) -> str:
        return f"Info de Manager:\
            \nCode Manager : {self.__code_manager}\
            \nNom et prenom: {self.full_name}\
            \nNombre des employes : {len(self.__ls_employe)}"

class ETAT(Enum):
    EN_COURS = 1
    VALIDE = 2
    REFUSE = 3

class DemandeConge:
    def __init__(self,code_employe,date_debut,duree,motif) -> None:
        self.__code_employe = code_employe
        self.__date_debut = date_debut
        self.__duree = duree
        self.__motif = motif
        self.__etat = ETAT.EN_COURS
    
    @property
    def code_employe(self):
        return self.__code_employe

    @property
    def duree(self):
        return self.__duree

    @property
    def etat(self):
        return self.__etat

    def valider(self):
        self.__etat = ETAT.VALIDE

    def refuser(self):
        self.__etat = ETAT.REFUSE
    
    def __str__(self) -> str:
        return f"Info de Demande :\
            \nCode employe :{self.__code_employe}\
            \nDuree : {self.__duree}\
            \nEtat: {self.__etat}"

class GestionConge:
    def __init__(self) -> None:
        self.__ls_manager = []
        self.__ls_demande_conge = []

    def ajouter_manager(self):
        print("Ajouter manager :")
        nom = valid_input("Entrer nom :")
        prenom = valid_input("Entrer prenom :")
        code_manager = valid_input("Entrer code manager :")
        manager = Manager(nom,prenom,code_manager)
        self.__ls_manager.append(manager)
        print("Manager ajoutee avec success!")
        n = int(valid_input("combien d'employe vous avez?"))
        for i in range(n):
            manager.ajouter_employe()

    def ajouter_demande_conge(self):
        print("Ajouter demande de conge :")
        code_employe = int(valid_input("Entrer code employe :"))
        date_debut = valid_date_input("Entrer date de debut :")
        duree = int(valid_input("Entrer duree :"))
        motif = valid_input("Entrer le motif :")
        self.__ls_demande_conge.append(DemandeConge(code_employe,date_debut,duree,motif))
    
    def liste_demande_conge_en_cours(self):
        ls_dc_en_cours = []
        for dc in self.__ls_demande_conge:
            if dc.etat == ETAT.EN_COURS:
                ls_dc_en_cours.append(dc)
        return ls_dc_en_cours
    
    def liste_demande_conge_by_employe(self,code_employe):
        ls_dc_by_employe = []
        for dc in self.__ls_demande_conge:
            if dc.code_employe == code_employe:
                ls_dc_by_employe.append(dc)
        return ls_dc_by_employe
    
    def liste_demande_conge_by_manager(self,code_manager):
        ls_dc_by_manager = []
        manager = None
        for m in self.__ls_manager:
            if m.code_manager == code_manager:
                manager = m
        if manager:
            ls_code_employe = [ ce.num_matricule for ce in manager.ls_employe ]
            for dc in self.__ls_demande_conge:
                if dc.code_employe in ls_code_employe:
                    ls_dc_by_manager.append(dc)
        return ls_dc_by_manager

    def duree_total_conge(self):
        ls_code_employe = [e.code_employe for e in self.__ls_demande_conge]
        ls_duree_total_conge = {e:0 for e in ls_code_employe}
        for dc in self.__ls_demande_conge:
            ls_duree_total_conge[dc.code_employe] += dc.duree
        return ls_duree_total_conge


# TESTS

# def print_l(l):
#     for i in l:
#         print(i)

# gc = GestionConge()

# gc.ajouter_manager()
# gc.ajouter_manager()

# gc.ajouter_demande_conge()
# gc.ajouter_demande_conge()
# gc.ajouter_demande_conge()
# gc.ajouter_demande_conge()

# print("liste dc par employe")
# l = gc.liste_demande_conge_by_employe(2)
# print_l(l)
# l = gc.liste_demande_conge_by_employe(4)
# print_l(l)
# l = gc.liste_demande_conge_by_employe(5)
# print_l(l)

# print("liste dc par manager")
# l = gc.liste_demande_conge_by_manager("any")
# print_l(l)
# l = gc.liste_demande_conge_by_manager("any2")
# print_l(l)

# print("liste dc en cours")
# l = gc.liste_demande_conge_en_cours()
# print_l(l)

# print("liste duree")
# l = gc.duree_total_conge()
# print(l)


# m = Manager("any","any","any")

# m.ajouter_employe()
# m.ajouter_employe()
# m.ajouter_employe()
# m.ajouter_employe()

# m.trier_employe()

# m.liste_employe()