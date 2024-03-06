import os
# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py liste_courses.py"

# Variables
liste_course = {
    "pates": 2,
    "sauce tomate": 1,
    "parmesan": 1
}

# Fonctions

def ClearC():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def show_actions():
    print("1 - Ajouter")
    print("2 - Supprimer")
    print("3 - Modifier")
    print("4 - Quitter")

def Lis():
    if len(liste_course) == 0:
        print("Il n'y a plus d'élément dans la liste")
        return False
    else:
        for Index, Item in enumerate(liste_course):
            print(f"{Index+1} - {Item} (Qté: {liste_course[Item]})")
        return True

def Val():
    Select = 0
    while True:
        try:
            Select = int(input("?: "))
        except:
            print(f"Merci de donner un entier entre 1 et {len(liste_course)}")
            
        else:
            print(f'if {Select}>=1 & {Select}<= {len(liste_course)}:')
            if Select>=1 & Select<= len(liste_course):
                return list(liste_course.keys())[Select-1]
            else:
                print(f"Merci de donner un entier entre 1 et {len(liste_course)}")
                

def Add():
    art = input("Nom de l'article")
    if art in liste_course:
        qt=input("Nombre à ajouter")
        liste_course[art]= liste_course[art]+qt
    else:
        qt=input("Nombre d'article")
        liste_course[art]=qt

def Del():
    if Lis():
        #del liste_course[Val()]
        print(Val())
    

            

#def Mod():
#    if Lis():

    
#########################
### Début du programe ###
#########################



while True:
    print("Bienvenue dans la liste de courses.\n")
    print("Que voulez vous faire ?")
    show_actions()
    try:
        Select = int(input("?:"))
    except:
        print("Ceci n'est pas un entier")
    else:
        match Select:
            case 1:
                ClearC()
                Add()
            case 2:
                ClearC()
                Del()
            case 3:
                ClearC()
                print(3)
            case 4:
                break
            case _:
                ClearC()
                print("Merci de rentrer un entier entre 1 et 4")
                show_actions
    






print("A bientot")
