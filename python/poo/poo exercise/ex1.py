class Etudiant :
    def __init__(identifiant, nom, note, ville):
        identifiant.nom = nom
        identifiant.note = note
        identifiant.ville = ville
        print()
p=Etudiant("akabour","4000","CHELLALTE")
print(p)