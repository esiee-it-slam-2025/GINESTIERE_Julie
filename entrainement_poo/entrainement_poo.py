from Class import Creature as Creature, Hero as Hero, Monstre as Monstre
from whileTrue import *
import os, random

# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py entrainement_poo.py"

# Init variables
hero = None
monstre = None

armes = {"Epée": 5, "Arc": 4, "Couteau à beurre": 1}




def clearC():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')



# Début du jeu

def intro():
    print("===============================================================")
    print("|| Bienvenue dans le système de combat POO (Punch Out Out) ! ||")
    print("===============================================================")
    # Choix du nom, choix de l'arme

    # Création des instances

    # Attention pour modifier les variables globales dans une fonction en python vous devez d'abord utiliser cette ligne
    global hero, monstre
    hero = Hero(input("Quel est le nom de ton héros.\n->"))
    monstre = Monstre()
    
    clearC()

    combat()

# Boucle de combat


def combat():
    tourHeros = True
    print("Bagarre")
    while (hero.pv > 0) & (monstre.pv > 0):
        if tourHeros:
            print("1 - Attaquer")
            print("2- Lancer votre sort")
            select = WTrue("|>", 1, 2)

            if select == 1:
                hero.attaque(monstre)
            elif select == 2:
                monstre.attaque(monstre)

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
else:
    print("jaaj")