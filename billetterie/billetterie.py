"""
Cours "Introduction 1" - Exercice "Billetterie"
"""
import os


# Variables
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8,
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}
stations_names = list(stations.keys())
stations_distances = list(stations.values())
NBAdu = 0
NBRed = 0
GDép = 0
GArr = 0

def clearC(sta=True):
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    
    # Introduction
    print("           /////// ")
    print("         ///       ")
    print("  //////////////   ")
    print("      ///          ")
    print("///////            ")
    print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")

    # Questions à l'utilisateur
    print("Vous êtes sur la ligne K")
    if sta:
        for index, stations in enumerate(stations_names):
            print(f"{index+1}./ {stations}")



clearC()
while True:
    try:
        print("Quel est votre gare de départ?")
        GDép = int(input("K"))-1
        if GDép < 0 | GDép > len(stations_names)-1:
            raise Exception()
    except:
        clearC()
        print(f"Merci de rentrer un valeur entre 1 et {len(stations_names)}")
    else:
        break

clearC()
while True:
    try:
        print("Quel est votre gare d'arrivé?")
        GArr = int(input("K"))-1
        if GArr < 0 | GArr > len(stations_names)-1  | GArr == GDép:
            raise Exception()
    except:
        clearC()
        print(f"Merci de rentrer un valeur entre 1 et {len(stations_names)} exepté {GDép}")
    else:
        break

clearC(False)
while True:
    try:
        print("Nombre de passager.s au tarif plein:")
        NBAdu = int(input("Qté: "))-1
        if NBAdu < -1:
            raise Exception()
    except:
        clearC(False)
        print("Merci de rentrer un entier superieur ou egal à 0")
    else:
        break

clearC(False)
while True:
    try:
        print("Nombre de passager.s au tarif plein:")
        NBRed = int(input("Qté: "))-1
        if NBRed < -1:
            raise Exception()
    except:
        clearC(False)
        print("Merci de rentrer un entier superieur ou egal à 0")
    else:
        break

if NBRed + NBAdu == 0:
    print("Aucun passager")
    print("Au revoir")
    exit

# Calculs de l'itinéraire

# Choix de la bonne zone tarifaire

# Calcul du coût total

# Affichage des détails du voyage et du tarif

# Affichage de la voie du train à emprunter
