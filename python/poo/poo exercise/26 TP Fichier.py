f =open("demofile3.txt","w") #ouvrir le fichier en mode écriture en effaçant son ancien contenu
f.write("domage!! l’ancient contenu est supprimé") #écrire la phrase domage!! l’ancient contenu est supprimé“
f.close() #fermer le fichier
f =open("demofile3.txt","r")
print(f.read()) # ouvrir et lire le fichier après l'ajout
