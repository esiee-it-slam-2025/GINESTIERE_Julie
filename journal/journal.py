"""
Cours "Advanced 2" - Exercice "Journal"
Réalisé par Xxxxx XXXXX
"""
import random
import argparse
from donnees import *
from datetime import datetime



class ElementJournal():
    date=""
    edition=""
    auteur=""
    contenu=""
    titre =""

    def __init__(self, auteur, edition, contenu):
        self.auteur = auteur
        self.edition = edition
        self.contenu =contenu


    def display(self):
        '''print(f"__{'_' * len(self.titre)}__")
        print(f"* {self.titre} *")
        print(f"__{'_' * len(self.titre)}__")
        print(self.contenu)'''

        return(f"--{'-' * len(self.titre)}--\n* {self.titre} *\n--{'-' * len(self.titre)}--\n{self.contenu}")










class Article(ElementJournal):

    def __init__(self, titre, auteur, edition, contenu):
        super().__init__(auteur, edition, contenu)
        self.titre = titre

    def display(self):
        
        return(f"{super().display()}\n{self.auteur}")







class Interview(ElementJournal):
    invite=""

    def __init__(self, invite, auteur, edition, contenu):
        super().__init__(auteur, edition, contenu)
        self.invite = invite
        self.titre = f"{self.auteur} interview {self.invite}"
        






class Generateur():
    date = None
    edition = None

    def __init__(self, date, edition):
        self.date = date
        self.edition =edition

    def importer(self, articles, interviews):
        global eleListe
        eleListe = []
        for art in articles:
            if (art["date"] == self.date) & ((art["edition"] == self.edition) |(art["edition"] ==  "national")):
                eleListe.append(Article(art["titre"], art["auteur"], art["edition"], art["contenu"]))
        

        for int in interviews:
            if (int["date"] == self.date) & ((int["edition"] == self.edition) |(int["edition"] ==  "national")):
                eleListe.append(Interview(int["invite"], int["auteur"], int["edition"], int["contenu"]))

        return eleListe
        




    def afficher(self, elements):
        
        if len(elements) == 0:
            print("Pas d'articles ou d'interviws pour ce jour")
        else:    
            o =  "==================================\n*-*-*-*-*-* LeLutécien *-*-*-*-*-*\n==================================\n"
            '''print(f"==================================")
            print(f"*-*-*-*-*-* LeLutécien *-*-*-*-*-*")
            print(f"==================================")'''

            random.shuffle(eleListe)

            for elements in eleListe:
                o += "\n\n\n\n" + elements.display() +"\n"

            with open('./credits.txt', 'r', encoding='utf-8') as f:
                o += "\n\n\n\n\n\n\n" + f.read()

            with open('./output.txt', 'w', encoding='utf-8') as f:
                f.write(o)
            
            with open('./output.txt', 'r', encoding='utf-8') as f:
                print(f.read())

if __name__ == "__main__":

    # On crée l'instance de ce qui nous permets d'accepter des arguments à l'aide de la bibliothèque argparse
    parser = argparse.ArgumentParser(description="Génère le journal du jour selon une date et une région.")
    # On demande deux arguments positionnels (obligatoires) lors de l'appel de ce script
    parser.add_argument("date", help="Date du journal à générer, sous le format 'annee-mois-jour'")
    parser.add_argument("edition", help="Édition du journal à générer", choices=["national", "idf", "paca"])
    # Argparse nous renvoie ensuite un objet contenant les valeurs des arguments

    args = parser.parse_args()

    try:
        datetime.strptime(args.date, '%Y-%m-%d')
    except ValueError:
        print("Date invalide merci de mettre une date sous la forme est YYYY-MM-DD")
        raise SystemExit
    # On crée une instance de Générateur en lui passant la date et l'édition du journal que l'on veut voir
    # selon ce qui a été écrit dans le terminal lors de l'exécution de ce fichier python
    generateur = Generateur(args.date, args.edition)
    
    # On appelle la méthode du générateur en lui passant les articles et interviews (importés au tout début de ce fichier)
    elements = generateur.importer(articles, interviews)
    
    # On renvoie les éléments récupérés à la ligne précédente pour afficher le journal dans le terminal
    generateur.afficher(elements)
