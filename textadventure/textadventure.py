
import os, json, time
from Questionnaire import *


OClef =None
Salles = None
Etages =None
try:
    OClef = json.load(open('OClef.json'))
    Salles = json.load(open('Salles.json'))
    Etages = json.load(open('Etages.json'))
except:
    print('\033[1;31mLes fichiers Oclef.json & Salles.json n''ont pas été trouvé.\nIl est conseillé de ne pas executer ce programme depuis VS code.\033[0;37m')
    quit()

Code=""


personnage = hero(input('Comment t\'appelle tu?\n'), "a")#questionnaire()

plats = "Ramen,Onigiri,Udon,Curry"  # À transformer en liste

plats_stock = {}  # À remplir avec les plats

objets_cles = ["smartphone"]
inventaire = {}

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************
def clearC():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def UTText(Text):
    for i, l in enumerate(Text):
        clearC()
        print(Text[0:i+1])
        time.sleep(0.01)
    time.sleep(2)
    clearC()

def fight():
    print("a")

def Action(Record):
    match Record["Type"]:
        case "print":
            UTText(Record["Texte"])
        case "fight":
            UTText(Record["Texte"])
            fight(Record["Ennemi"])


def Escaliers(Etage):
    print(f"Vous êtes à l'étage {Etage}")
    while True:
        try:
            Etage = int(input("Vous allez à l'étage >"))
            if Etage > 3 | Etage < 0:
                raise Exception()
            return Etage
        except:
            print("Entrez une valeur entre 0 et 3")
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
    Code = '0-H'
    return lieu(Code)

# ********************************************************************************
# LIEUX
# ********************************************************************************
def lieu(Code):
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
        if(Salles[Code]["Déplacements"][select-1-act]["Key"] == None) | (Salles[Code]["Déplacements"][select-1-act]["Key"] in objets_cles):
            return Salles[Code]["Déplacements"][select-1-act]["Code"]
        print(f'Vous n\'avez pas accès à cette salle, il vous faut \"{Salles[Code]["Déplacements"][select-1-act]["Key"]}\"')            
    else:
        Action(Salles[Code]["Actions"][select-1])
    
    return Code
# ********************* ***********************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction

if __name__ == "__main__":
    Code = intro()
    
    Etage = 0

    while True:
        if (Code == "E"):
            Etage = Escaliers(Etage)
            Code = Etages[Etage]["Hub"]
        Code = lieu(Code)

    print("Fin du jeu.")
