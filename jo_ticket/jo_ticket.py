
# Import des bibliothèques standard
import locale, json, qrcode
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def search(self, key, value):
    for item in self:
        if item.get(key) == value:
            return item
    return None

# Import des bibliothèques tierces
'''
coor = {
    "QR": (111,334),
    "EDom": (20,430),
    "EExt": (107,505),
    "Sta": (55,587),
    "Vil": (1155,375),
    "DD": (55,656),
    "HD": (1155,485),
    "Cat": (650,605),
    "Pla": (845,605),
    "Pri": (995,605)
}
'''

# Ce code sert à indiquer à Python que l'on voudra afficher des dates
# en français lors de l'utilisation de datetime.strptime()
locale.setlocale(locale.LC_TIME, "fr_FR")


#with open('events.json', 'r') as f:
events = json.load(open('events.json', 'r', encoding="utf-8"))
stadiums = json.load(open('stadiums.json', 'r', encoding="utf-8"))
tickets = json.load(open('tickets.json', 'r', encoding="utf-8"))
P24font36 = ImageFont.truetype('fonts/Paris2024.ttf', 36, encoding="utf-8")
P24font22 = ImageFont.truetype('fonts/Paris2024.ttf', 22, encoding="utf-8")
bleu =  (51, 19, 104)
blanc =  (255, 255, 255)

coor = {
    "QR": (111,334),
    "EDom": (20,430),
    "EExt": (107,505),
    "Lieu": (55,587),
    "Hor": (55,656),
    "Cat": (83, 755),
    "Pla": (236, 755),
    "Pri": (350, 755)
}


# Préparation des polices
# Lecture des documents JSON
it =0
# Boucle sur chaque billet...
for ticket in tickets:
    # Préparation des textes à écrire
    it+=1
    event = search(events, "id",ticket["event_id"] )
    stadium = search(stadiums, "id", event["stadium_id"])
    start = datetime.fromisoformat(event["start"]).strftime("%d/%m/%Y à %H:%M")
    seat = ticket["seat"] if ticket["seat"] != "free" else "Libre"
    price = f"{ticket['price']}{'€' if ticket['currency'] != 'USD' else '$'}"
    # Ouverture de l'image de fond
    with Image.open("ticketJO.png") as im:
        draw = ImageDraw.Draw(im)
        # Écriture des informations du match
        draw.text(coor["EDom"], event["team_home"], fill=bleu, font=P24font36)
        draw.text(coor["EExt"], event["team_away"], fill=bleu, font=P24font36)
        draw.text(coor["Lieu"], f"{stadium['name']} - {stadium['location']}", fill=blanc, font=P24font22)
        draw.text(coor["Hor"], start, fill=blanc, font=P24font22)
        draw.text(coor["Cat"], ticket["category"], fill=blanc,anchor="ma" ,font=P24font22)
        draw.text(coor["Pla"], seat, fill=blanc,anchor="ma" ,font=P24font22)
        draw.text(coor["Pri"], price, fill=blanc,anchor="ma" ,font=P24font22)



        qr = qrcode.QRCode(box_size=4)
        qr.add_data(ticket["id"])
        qr.make()
        im.paste(qr.make_image().resize((134,134)), (132, 842))

        im.save(f"tickets/{it}.png")