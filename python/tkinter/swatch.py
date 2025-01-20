# Importer les modules nécessaires
import sys
from tkinter import *
import time
import random

# Créer une fonction qui génère une couleur aléatoire en hexadécimal
def random_color():
    # Choisir trois valeurs aléatoires entre 0 et 255
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Convertir les valeurs en hexadécimal
    r = hex(r)[2:]
    g = hex(g)[2:]
    b = hex(b)[2:]
    # Ajouter des zéros si nécessaire
    if len(r) == 1:
        r = "0" + r
    if len(g) == 1:
        g = "0" + g
    if len(b) == 1:
        b = "0" + b
    # Concaténer les valeurs avec le préfixe #
    color = "#" + r + g + b
    # Retourner la couleur
    return color

# Créer une fonction qui affiche un nuancier avec 16 couleurs aléatoires
def swatch():
    # Créer une fenêtre
    window = Tk()
    window.title("Nuancier")
    # Créer un canevas
    canvas = Canvas(window, width=400, height=400)
    canvas.pack()
    # Créer une liste vide pour stocker les couleurs
    colors = []
    # Créer une boucle pour générer 16 couleurs aléatoires
    for i in range(16):
        # Générer une couleur aléatoire
        color = random_color()
        # Ajouter la couleur à la liste
        colors.append(color)
        # Calculer les coordonnées du rectangle correspondant à la couleur
        x1 = (i % 4) * 100
        y1 = (i // 4) * 100
        x2 = x1 + 100
        y2 = y1 + 100
        # Dessiner le rectangle avec la couleur
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    # Afficher les couleurs dans la console
    print("Les couleurs du nuancier sont :")
    for i in range(16):
        print(colors[i])
    # Lancer la boucle principale
    window.mainloop()

# Appeler la fonction swatch
swatch()