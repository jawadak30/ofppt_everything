import json #importer la bibliothèque json
quantiteFournitures= {" cahiers":134, "stylos":{"rouge":41,"bleu":74},"gommes":85} #déclarer un dictionnaire
fichier=open ("quantiteFournitures.json","w") #ouvrir un fichier en écriture
fichier.write(json.dumps(quantiteFournitures)) #transformer le dictionnaire en texte json
fichier.close() #fermer le fichier"""
#fichier = open ( "quantiteFournituress.json", "r" ) #ouvrir le fichier exemple.json en lecture
"""x=json.loads(fichier.read() ) #décoder le texte et le transformer en dictionnaire.
print(x)"""
