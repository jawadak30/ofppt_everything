import csv #importer la bibliothèque csv
bonCommande = [{"produit":"cahier", "reference":"F452CP", "quantite":41, "prixUnitaire":1.6},
{"produit":"stylo bleu", "reference":"D857BL", "quantite":18, "prixUnitaire":0.95},
{"produit":"stylo noir", "reference":"D857NO", "quantite":18, "prixUnitaire":0.95},
] #déclarer des dictionnaires
fichier = open("bon-commande.csv", "w") #ouvrir un fichier en écrire
ecrivainCSV = csv.DictWriter(fichier,delimiter=";",fieldnames=bonCommande[0].keys())
#produire des lignes de sortie depuis les dictionnaires,
# fieldnames contient les clés des dictionnaires
ecrivainCSV.writeheader() # Ecrire la ligne d'en-tête avec le titre des colonnes
for ligne in bonCommande: # Parcourir les dictionnaires
    ecrivainCSV.writerow(ligne) #Ecrire une ligne dans le fichier
fichier.close()
