from abc import ABC
import re
from datetime import date
import json

numero_regex = re.compile(r"^\d{1,3}-[a-z]-\d{1,2}$")
mail_regex = re.compile(r"^\w+@\w+\.\w+$")

class IllegalCategorie(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class Chambre:
    def __init__(self,numero = None,categorie = None, type_lit = None, etage = None) -> None:
        if numero is not None:
            match = numero_regex.match(numero)
            if match:
                self.numero = numero
            else:
                raise ValueError("Format invalide!")
        if categorie is not None:
            if categorie in ["standard","luxe","suite"]:
                self.categorie = categorie
            else:
                raise IllegalCategorie("Categorie invalide!")
        
        self.type_lit = type_lit
        self.etage = etage
    
    def __str__(self) -> str:
        return f"Chambre Info:\n\
Numero: {self.numero}\n\
Categorie: {self.categorie}\n\
Type de lit: {self.type_lit}\n\
Etage: {self.etage}"


    def set_categorie(self,categorie):
        if categorie in ["standard","luxe","suite"]:
            self.categorie = categorie
        else:
            raise IllegalCategorie("Categorie invalide!")
    
    def set_numero(self,numero):
        match = numero_regex.match(numero)
        if match:
            self.numero = numero
        else:
            raise ValueError("Format invalide!")


class Client(ABC):
    def __init__(self,tel = None,mail = None) -> None:
        self.tel = tel
        if mail is not None:
            match = mail_regex.match(mail)
            if match:
                self.mail = mail
            else:
                raise ValueError("Format invalide!")
    
    def set_mail(self,mail):
        match = mail_regex.match(mail)
        if match:
            self.mail = mail
        else:
            raise ValueError("Format invalide!")
    
    def __str__(self) -> str:
        return f"{type(self).__name__} Info:\n\
Tel : {self.tel}\n\
Mail : {self.mail}\n"



class ClientParticulier(Client):
    def __init__(self, tel=None, mail=None,cin = None,nom=None,prenom = None) -> None:
        super().__init__(tel, mail)
        self.cin = cin
        self.nom = nom
        self.prenom = prenom
    
    def __str__(self) -> str:
        return super().__str__() + f"CIN : {self.cin}\nNom complet : {self.nom + ' ' + self.prenom}"

class ClientEntreprise(Client):
    def __init__(self, tel=None, mail=None,num_rgc = None) -> None:
        super().__init__(tel, mail)
        self.num_rgc = num_rgc
    
    def __str__(self) -> str:
        return super().__str__() + f"Numero de registre de commerce : {self.num_rgc}"


class IllegalDuree(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class Reservation:
    num_res_counter = 1
    def __init__(self,client = None,chambre = None,date_debut = None,date_fin = None,montant_jour = None,retour = False) -> None:
        self.num_res = Reservation.num_res_counter
        Reservation.num_res_counter += 1
        self.client = client
        self.chambre = chambre
        self.date_debut = date_debut
        self.date_fin = date_fin
        # the dates must be date objects NOT string!!!
        duree = date_fin - date_debut
        if duree.days <= 1:
            raise IllegalDuree("La duree est invalide! Doit depasser un jour!")
        self.montant_jour = montant_jour
        self.retour = retour
    
    def montant_res(self):
        if self.montant_jour:
            duree = self.date_fin - self.date_debut
            return duree.days * self.montant_jour
    
    def retourner(self):
        self.retour = True
    
    def __str__(self) -> str:
        return f"Client: {self.client}\nChambre: {self.chambre}\nDate debut: {self.date_debut}\nDate fin: {self.date_fin}"

class EnsembleReservation:
    def __init__(self) -> None:
        self.lsRes = []
        self.lsClient = []
        self.lsChambre = []
    
    def ajouter_client(self):
        print("Ajouter un client")
        tel = input("Entrer votre tel:")
        for client in self.lsClient:
            if client.tel == tel:
                print("Client deja existe!")
                return
        print("Choisir type de client")
        print("1: Particulier")
        print("2: Entreprise")
        choix = input("Entrer votre choix")
        match(choix):
            case "1":
                cin = input("Entrer le cin: ")
                nom = input("Entrer le nom: ")
                prenom = input("Entrer le prenom: ")
                client = ClientParticulier(tel=tel,cin=cin,nom=nom,prenom=prenom)
                self.lsClient.append(client)
            case "2":
                num_rgc = input("Entrer votre numero de registre de commerce :")
                client = ClientEntreprise(tel=tel,num_rgc=num_rgc)
                self.lsClient.append(client)
            case _:
                print("choix invalide!")
        
    def ajouter_chambre(self):
        print("Ajouter Chambre")
        numero = input("Entrer le numero de chambre: ")
        for ch in self.lsChambre:
            if ch.numero == numero:
                print("Chambre deja existe!")
                return
        categorie = input("Entrer categorie :")
        type_lit = input("Entrer type de lit :")
        etage = input("Entrer etage :")
        ch = Chambre(numero,categorie,type_lit,etage)
        self.lsChambre.append(ch)

    def rechercher_chambre(self,numero):
        for ch in self.lsChambre:
            if ch.numero == numero:
                return ch
    
    def rechercher_client(self,tel):
        for client in self.lsClient:
            if client.tel == tel:
                return client
    
    def rechercher_res_par_chambre(self,numero):
        lsRes = []
        for res in self.lsRes:
            if res.chambre.numero == numero:
                lsRes.append(res)
        if len(lsRes) > 0:
            return lsRes
    
    def is_reservation_possible(self,res,date_debut,date_fin):
        # check if the start date is between date_debut and date_fin
        if res.date_debut > date_debut and res.date_debut < date_fin:
            return False
        # check if the end date is between date_debut and date_fin
        if res.date_fin > date_debut and res.date_fin < date_fin:
            return False
        # check if the reservation include both date_debut and date_fin
        if res.date_debut < date_debut and res.date_fin > date_fin:
            return False
        return True

    def reservation_expiree(self,num_res):
        for res in self.lsRes:
            if res.num_res == num_res:
                if res.date_fin < date.today():
                    return True
        return False

    def ajouter_res(self):
        print("Ajouter une reservation")
        num_ch = input("Entrer numero de chambre")
        ch = self.rechercher_chambre(num_ch)
        if ch:
            tel = input("Entrer votre tel :")
            client = self.rechercher_client(tel)
            date_debut = input("Entrer date de debut: (AAAA-MM-JJ)")
            date_debut = date.fromisoformat(date_debut)
            date_fin = input("Entrer date de fin: (AAAA-MM-JJ)")
            date_fin = date.fromisoformat(date_fin)
            lsRes = self.rechercher_res_par_chambre(num_ch)
            reservation_possible = True
            for res in lsRes:
                result = self.is_reservation_possible(res,date_debut,date_fin)
                if not result:
                    reservation_possible = False
                    break
            if reservation_possible:
                montant_jour = int(input("Entrer montant journalier : "))
                res = Reservation(client,ch,date_debut,date_fin,montant_jour)
                self.lsRes.append(res)
            else:
                print("Chambre occupé!")
                return
        
    def info_res(self,tel):
        client = self.rechercher_client(tel)
        montant_global = 0
        for res in self.lsRes:
            if res.client == client:
                print(res)
                print("montant de reservation",res.montant_res())
                montant_global += res.montant_res()
        print("montant global: ",montant_global)

    
    def sauvgarder(self):
        lsClient = {}
        lsClient["liste_clients"] = []
        for res in self.lsRes:
            if self.reservation_expiree(res.res_num):
                client = {}

                client["tel"] = res.client.tel
                if isinstance(res.client,ClientParticulier):
                    client["cin"] = res.client.cin
                    client["nom"] = res.client.nom
                    client["prenom"] = res.client.prenom
                else:
                    client["num_rgc"] = res.client.num_rgc
                lsClient["liste_clients"].append(client)
        with open("info_clients.json","w") as f:
            json.dump(lsClient,f)

