import random
NombreA = random.randint(0,10)
while True:
    try:
        NombreB = int(input("Entrer un nombre:"))
    except:
        print("Ceci n'est pas un entier")
    else:
        break



def wat (x, y):
    return((x+y)*2)

Resultat  = wat(NombreA, NombreB)

if Resultat > 20:
    print("Résultat énorme")
else:
    print("Résultat pas ouf")