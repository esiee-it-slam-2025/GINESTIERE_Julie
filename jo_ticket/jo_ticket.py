
# Import des bibliothèques standard
import locale, datetime, json, os
from PIL import Image

# Import des bibliothèques tierces
coor = {
    QR: {x: 111, y:340},
    EDom: {x: 877, y:115},
    EExt: {x: 877, y:242},
    Sta: {x: 705, y:375},
    Vil: {x: 1155, y:375},
    DD: {x: 705, y:485},
    HD: {x: 1155, y:485},
    Cat: {x: 650, y:605},
    Pla: {x: 845, y:605},
    Pri: {x: 995, y:605},
}
# Ce code sert à indiquer à Python que l'on voudra afficher des dates
# en français lors de l'utilisation de datetime.strptime()
locale.setlocale(locale.LC_TIME, "fr_FR")


#with open('events.json', 'r') as f:
events = json.load(open('events.json'))
stadiums = json.load(open('stadiums.json'))
tickets = json.load(open('tickets.json'))


# Préparation des polices

# Lecture des documents JSON

# Boucle sur chaque billet...
for ticket in tickets:
    # Préparation des textes à écrire
    False
    # Ouverture de l'image de fond
    with Image.open("ticketJO.png") as im:
        # Écriture des informations du match
        False
        # Génération et écriture du QR Code

        # Sauvegarde du billet
