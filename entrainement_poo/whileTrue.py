def WTrue(IPText, min, max):
     
    while True:
            try:
                select = int(input(IPText))
                if (select > max) | (select < min):
                    raise Exception("Valeur incorrecte")
                break
            except:
                print(f"Erreur de saisie. Merci de saisir un entier entre {min+1} et {max}")
    return select