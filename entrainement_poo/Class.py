class Creature():
    # Ajouter les autres attributs
    degats = 0
    pv = 0
    effets = {}

    def attaque(self, cible):
        cible.pv -=self.degats # A supprimer quand la fonction sera écrite

# Ajouter les autres classes
class Hero(Creature):
    nom = ''
    degats = 20
    pMana = 100
    pv = 100

    def __init__(self, nom):
        self.nom = nom
    
    
    def magie(self, cible):
        cible.pv -= (2*self.degats)
        self.pMana -= 1


class Monstre(Creature):
    pv = 50
    degats = 5
    def __init__(self):
        pass

    def venin(self, cible):
        cible.effets["poison-1"] = 5