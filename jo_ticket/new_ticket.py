import json, uuid, os
from datetime import datetime


class IntervalError(Exception):

    def __init__(self, min, max):
        self.message= f"L'entier doit se trouver entre {str(min)} et {str(max)}"
        super().__init__(self.message)

class CharError(Exception):

    def __init__(self):
        self.message= f"Merci de donner UNE lettre"
        super().__init__(self.message)

class CurError(Exception):
    def __init__(self, licur):
        self.message =f"Merci de choisir parmis ces devises {licur}"
        super().__init__(self.message)




class Ticket():
    def __init__(self, event_id, category, seat, currency, table = {"Silver":{"EUR": 40,"USD":65},"Gold":{"EUR": 50,"USD":80},"Platinium":{"EUR": 80,"USD":95}}):
        self.id = str(uuid.uuid4())
        self.event_id=event_id
        self.seat=seat
        match category:
            case 1:
                self.category = "Silver"
            case 2:
                self.category = "Gold"
            case 3:
                self.category = "Platinium"
        self.currency=currency
        self.price = table[self.category][self.currency]
    
    def ToJSON(self):
        return(json.dumps({"id": self.id,"event_id": self.event_id,"category": self.category,"seat": self.seat,"price": self.price,"currency": self.currency}))

events = json.load(open('events.json', 'r', encoding="utf-8"))
stadiums = json.load(open('stadiums.json', 'r', encoding="utf-8"))

if not os.path.isfile("newTickets.json"):
    with open("newTickets.json", "w") as f:
        f.write("[]")
tickets = json.load(open('newTickets.json', 'r', encoding="utf-8"))


#MATCH
for event in events:
    print(f"{event['id']}/ {event['team_home']} - {event['team_away']} ({datetime.fromisoformat(event["start"]).strftime("%d/%m à %H:%M")})")

match = 0
while True:
    try:
        match = int(input("Choisissez le match > "))
        if not 1 <= match <= len(events):
            raise IntervalError(1,len(events))
        break
    except IntervalError as err:
        print(err.message)
    except TypeError:
        print("Merci de rentrer un entier")
    except ValueError:
        print("Merci de rentrer un entier")



#CATEGORIE
print("\n1/ Silver")
print("2/ Gold")
print("3/ Platinium")
cat = 0
while True:
    try:
        cat = int(input("Choisissez la categorie > "))
        if not 1 <= cat <= 3:
            raise IntervalError(1,3)
        break
    except IntervalError as err:
        print(err.message)
    except TypeError:
        print("Merci de rentrer un entier")
    except ValueError:
        print("Merci de rentrer un entier")

#DEVISE
cur = ""
while True:
        try:
            curListe=["USD", "EUR"]
            cur = input("Choisissez la devise > ").upper()
            if not cur in curListe:
                raise CurError(curListe)
            break
        except CurError as err:
            print(err.message)


#PLACE
place=0
rang=""
if cat != 1:
    while True:
        try:
            rang = input("\nChoisissez le rang (A à Z) > ")
            if (len(rang) != 1) or ( not rang.isalpha()):
                raise CharError()
            break
        except CharError as err:
            print(err.message)
    rang = rang.upper()

    while True:

        try:
            place = int(input("Choisissez le n° de place > "))
            break
        except TypeError:
            print("Merci de rentrer un entier")
        except ValueError:
            print("Merci de rentrer un entier")
    
    NewT = Ticket(match, cat, f"{rang}-{place}", cur)
else:
    NewT = Ticket(match, cat, "free", cur)

print(NewT.ToJSON())



tickets.append(json.loads(NewT.ToJSON()))

with open('./newTickets.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(tickets))