
import os, json
from Questionnaire import *




try:
    OClef = json.load(open('OClef.json'))
    Salles = json.load(open('Salles.json'))
except:
    print('\033[1;31mLes fichiers Oclef.json & Salles.json n''ont pas été trouvé.\nIl est conseillé de ne pas executer ce programme depuis VS code.\033[0;37m')
    quit()



personnage = hero(input('Comment t''appelle tu?\n'), "a")#questionnaire()

plats = "Ramen,Onigiri,Udon,Curry"  # À transformer en liste

plats_stock = {}  # À remplir avec les plats

objets_cles = ["smartphone"]
inventaire = {}
Code = ""

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************
def clearC():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def Action(Record):
    eval(Record["Type"]+'("' + Record["Action"] + '")')

# ********************************************************************************
# INTRODUCTION
# ********************************************************************************

def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print(f"|| Bienvenue à A.U. {personnage['Nom']}! ||")
    print("===============================")

    # Demander un âge et écrire cette information dans le dictionnaire "personnage"

    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un

    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"

    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"
    Code = "0-H"
    lieu()

# ********************************************************************************
# LIEUX
# ********************************************************************************
def lieu():
    act = 0
    select=None
    print(f'│[{Salles[Code]["Nom"]}]')
    print(f'├──[Actions]')
    for i, action in enumerate(Salles[Code]["Actions"]):
        print(f'│   →{i+1}. {action["Nom"]}')
        act+=1
    dep = act
    print(f'├──[Déplacements]')
    for i, action in enumerate(Salles[Code]["Déplacements"]):
        print(f'│   →{i+1+act}. {action["Nom"]}')
        dep += 1
    while True:
        try:
            select = int(input('│>'))
            if select > dep | select < 0:
                raise Exception("Valeur incorrecte")
            break
        except:
            print(f"Erreur de saisie. Merci de saisir un entier entre 1 et {dep}")
    if select > act:
        clearC()
        Code = Salles[Code]["Déplacements"][select-1-act]["Code"]
    else:
        Action(Salles[Code]["Actions"][select-1])
# ********************* ***********************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction

if __name__ == "__main__":
    Code = "0-H"
    intro()
    
    while True:
        breakpoint()
        lieu()

    print("Fin du jeu.")
