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
Dist=0

TarifsZ = [None, 210,260,300,340]
Zone=0

def clearC(sta=False):
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


# Définition du trajet
clearC(True)
while True:
    try:
        print("Quel est votre gare de départ?")
        GDép = int(input("K"))-1
        
        if (GDép < 0) | (GDép > len(stations_names) - 1):
            raise ValueError('')
    except:
        clearC(True)
        print(f"\nMerci de rentrer un valeur entre 1 et {len(stations_names)}\n")
    else:
        break

clearC(True)
while True:
    try:
        print("Quel est votre gare d'arrivé?")
        GArr = int(input("K"))-1
        if (GArr < 0) | (GArr > len(stations_names)-1) | (GDép == GArr):
            raise ValueError('')
    except:
        clearC(True)
        print(f"\nMerci de rentrer un valeur entre 1 et {len(stations_names)} exepté {GDép+1}\n")
    else:
        break
    



# Calculs de l'itinéraire
clearC()
if GDép < GArr:
    for gare in stations_names[GDép:GArr]:
        print(f"· -{gare}")
        print("|")
    print(f"· -{stations_names[GArr]}")
    
else:
    print(f"· -{stations_names[GDép]}")
    for gare in reversed(stations_names[GArr:GDép]):
        print("|")
        print(f"· -{gare}")
   
for gare in stations_distances[min(GDép,GArr):max(GDép,GArr)]:
    Dist += gare


# Choix de la bonne zone tarifaire
if Dist < 3:
    Zone=1
elif Dist < 7:
    Zone=2
elif Dist < 11:
    Zone=3
elif Dist < 15:
    Zone = 4
else:
    print("Hors zone tarifaire")
    quit()

print(f"Distance: {Dist}km")
print(f"Vous êtes en zone de tarification {Zone}")
print("********************************************")
print(f"Tarif plein {TarifsZ[Zone]} yen")
print(f"Tarif réduit {max(TarifsZ[Zone]/2,110)} yen")


# Decompte des voyageurs
while True:
    try:
        print("Nombre de passager.s au tarif plein:")
        NBAdu = int(input("Qté: "))
        if NBAdu < 0:
            raise Exception()
    except:
        clearC()
        print("\nMerci de rentrer un entier superieur ou egal à 0\n")
    else:
        break

clearC()
while True:
    try:
        print("Nombre de passager.s au tarif réduit:")
        NBRed = int(input("Qté: "))
        if NBRed < 0:
            raise Exception()
    except:
        clearC()
        print("\nMerci de rentrer un entier superieur ou egal à 0\n")
    else:
        break

clearC()

# Verification présence de voyageur
if NBRed + NBAdu == 0:
    print("Aucun passager")
    print("Au revoir")
    exit

# Calcul du coût total
Tot=(TarifsZ[Zone])*NBAdu + (max(TarifsZ[Zone]/2,110))*NBRed



# Affichage des détails du voyage et du tarif
# Affichage de la voie du train à emprunter
print(f"\nTotal: {Tot} yen")

if len(stations_distances[min(GDép,GArr):max(GDép,GArr)]) - 2 == 0:
    print(f"{stations_names[GDép]} ----> {stations_names[GArr]}")
else:
    print(f"{stations_names[GDép]} -- {len(stations_distances[min(GDép,GArr):max(GDép,GArr)]) - 2} arrêts --> {stations_names[GArr]}")

if GDép < GArr:
    print("Prendre direction 'Fukuokakuko (Airport)'")
else:
    print("Prendre direction 'Meinohama'")
    







