
import os, json, time, random
from Questionnaire import *
from whileTrue import *



OClef =None
Salles = None
Etages =None
try:
    OClef = json.load(open('OClef.json'))
    Salles = json.load(open('Salles.json'))
    Etages = json.load(open('Etages.json'))
    Ennemis = json.load(open('Ennemis.json'))
    Nourriture = json.load(open('Nourriture.json'))
except:
    print('\033[1;31mLes fichiers Oclef.json & Salles.json n\'ont pas été trouvé.\nIl est conseillé de ne pas executer ce programme depuis VS code.\033[0;37m')
    quit()

Code=""


personnage = hero(input('Comment t\'appelle tu?\n'), questionnaire())

plats = [
    {
        "Nom":"Ramen",
        "Qt":2
    },
    {
        "Nom":"Onigiri",
        "Qt":10
    },
    {
        "Nom":"Udon",
        "Qt":2
    },
    {
        "Nom":"Curry",
        "Qt":2
    }
]

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

def fight(Record):
    lEnnemis = []
    for i, E in enumerate(Record):
        lEnnemis.append({"Nom":E,"Attaque":Ennemis[E]["Attaque"]*Ennemis[E]["Multiplicateur"]*Record[E], "PV":Ennemis[E]["PV"]})
    tours=-1
    select = 0
    while personnage["PV"] > 0 | sum(Ennemis["PV"] for Ennemis in lEnnemis) > 0:
        if tours:
            tours = False
            while True:
                print("C'est votre tour")
                print("├──[Actions]'\n|   →1. Attaquer\n│   →2. Parer\n│   →3. Inventaire\n│   →4. Fuir")
                select = WTrue("|>",1,4)
                match select:
                    case 1:
                        ERang = 0
                        if len(lEnnemis)!=1:
                            print("0 - Menu précedent")
                            for i, item in enumerate(lEnnemis):
                                print(f"{i+1} - {item['Nom']}")
                            ERang = WTrue('|>',0,len(lEnnemis)) - 1
                        if ERang != -1:
                            print(f"Vous lancer {personnage['Attaques'][0]['Nom']} et lui faites {personnage['Attaques'][0]['Dégats']} de dégats")
                            lEnnemis[ERang]["PV"] -= personnage['Attaques'][0]["Dégats"]
                            if lEnnemis[ERang]["PV"] < 1:
                                print(f"{lEnnemis.pop(ERang)['Nom']} est mort.")
                                
                            break
        
                            
                            
                    case 2:
                        break
                    case 3:
                        print("0 - Menu précedent")
                        for i, item in enumerate(inventaire):
                            print(f"{i+1} - {item['Nom']}")
                        IRang = WTrue('|>',0,len(inventaire)) - 1
                        if IRang !=-1:
                            if list(inventaire)[IRang] in Nourriture:
                                personnage["PV"]=min(personnage["PVM"], personnage["PV"] + Nourriture[list(inventaire)[IRang]]["PV"])
                                UTText(f"Vous manger un {plats[select-1]['Nom']}")
                            
                            break


                    case 4:
                        break
        else:
            if select == 4:
                print("Vous prenez la fuite")
                break
            coef = 0.8 if (select == 2) else 1
            for item in lEnnemis:
                print(f"{Ennemis[item['Nom']]['Dialogue'][random.randint(0,2)]}")
                print(f"-{item['Attaque']}PV")
                personnage["PV"] -= item['Attaque'] * coef
            tours = True
            

def Action(Record):
    match Record["Type"]:
        case "print":
            UTText(Record["Texte"])
        case "fight":
            UTText(Record["Texte"])
            fight(Record["Ennemis"])
        case "NOClef":
            if(Record["Objet"] not in objets_cles):
                UTText(Record["Texte1"])
                objets_cles.append(Record["Objet"])
            else:
                UTText(Record["Texte2"])
        case "Unique":
            eval(Record["Function"])


def Escaliers(Etage):
    print(f"Vous êtes à l'étage {Etage}")
    while True:
        try:
            Etage = int(input("Vous allez à l'étage >"))
            if (Etage > 3) | (Etage < 0):
                raise Exception()
            return Etage
        except:
            print("Entrez une valeur entre 0 et 3")

# ********************************************************************************
# UNIQUE
# ********************************************************************************
def cantine():
    while True:
        Qt=1
        print("Bonjour, voici les plats restants pour vous:")
        print("0 - Partir")
        for i, plat in enumerate(plats):
            print(f"{i+1} - {plat['Nom']} (Reste {plat['Qt']})") if (plat['Qt'] > 0) else False
        select = WTrue('Que voulez-vous prendre?', 0, len(plats))

        if select != 0:
            if plats[select-1]["Qt"]>0:
                if Nourriture[plats[select-1]["Nom"]]["Portable"]:
                    print(f"|Combien de {plats[select-1]['Nom']} voulez-vous emporter?")
                    Qt = WTrue('|>',1,plats[select-1]["Qt"])
                    try:
                        inventaire[plats[select-1]['Nom']] += Qt
                    except:
                        inventaire[plats[select-1]['Nom']] = Qt
                    print(f"Vous prenez {select} {plats[select-1]['Nom']}")
                else:
                    personnage["PV"]=min(personnage["PVM"], personnage["PV"] + Nourriture[plats[select-1]["Nom"]]["PV"])
                    UTText(f"Vous manger un {plats[select-1]['Nom']}")
                plats[select-1]["Qt"] -=Qt

            else:
                UTText(f"Il n'y a plus de {plats[select-1]['Nom']}")

        else:
            break


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
    for i, action in enumerate(Salles[Code]["Deplacements"]):
        print(f'│   →{i+1+act}. {action["Nom"]}')
        dep += 1
    select = WTrue('|>', 1, dep)
    if select > act:
        clearC()
        if(Salles[Code]["Deplacements"][select-1-act]["Key"] == None) | (Salles[Code]["Deplacements"][select-1-act]["Key"] in objets_cles):
            return Salles[Code]["Deplacements"][select-1-act]["Code"]
        print(f'Vous n\'avez pas accès à cette salle, il vous faut \"{Salles[Code]["Deplacements"][select-1-act]["Key"]}\"')            
    else:
        Action(Salles[Code]["Actions"][select-1])
    
    return Code
# ********************************************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction

if __name__ == "__main__":
    Code = intro()
    
    Etage = 0

    while True:
        clearC()
        if (Code == "E"):
            Etage = Escaliers(Etage)
            Code = Etages[Etage]["Hub"]
        Code = lieu(Code)

    print("Fin du jeu.")
