import csv #importer la bibliothèque csv
fichier = open("annuaire.csv", "w") #ouvrir un fichier en mode écriture
ecrivainCSV = csv.writer(fichier,delimiter=";") #ouvrir un flux d’écriture
ecrivainCSV.writerow(["Nom","Prénom","Téléphone"]) #écrire une 1ère ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["Dubois","Marie","0198546372"]) #écrire une 2ème ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["Duval","Julien","0399741052"]) #écrire une 3ème ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["Jacquet","Bernard","0200749685"]) #écrire une 4ème ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["Martin","Julie","0399731590"]) #écrire une 5ème ligne dans le fichier annuaire.csv
fichier.close() #Fermer le fichier
