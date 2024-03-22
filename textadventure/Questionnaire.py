def hero(nom, lettre):
    match lettre:
        case 'a':
            return {
                'Nom': nom,
                'Classe': 'Flame',
                'PV':90,
                'PVM':90,

                'Attaques':[
                    {
                    'Nom':'Jet de flamme',
                    'Description': 'Lance une raffale de flammes qui créé des dégats de zones.',
                    'Dégats':20
                    }
                ]
            }
        case 'b':
            return{
                'Nom': nom,
                'Classe': 'Celeste',
                'PV':80,
                'PVM':80,
                'Attaques':[
                    {
                    'Nom':'Foudre aveuglante',
                    'Description': 'Foudroie l''ennemi avec 50%% de chance de dégats de zone. Peut paralyser l''ennemi dan 10%% des cas',
                    'Dégats':20
                    }
                ]
            }
        case 'c':
            return{
                'Nom': nom,
                'Classe': 'Titanium',
                'PV':100,
                'PVM':100,
                'Attaques':[
                    {
                    'Nom':'Seisme',
                    'Description': 'Frappe terrstre qui peut etourdir l''ennemi et l''empecher de se proteger au prochain tour',
                    'Dégats':20
                    }
                ]
            }
        case 'd':
            return{
                'Nom': nom,
                'Classe': 'Aqua',
                'PV':90,
                'PVM':90,
                'Attaques':[
                    {
                    'Nom':'Vague',
                    'Description': 'Repousse l''ennemi avec une vague immense. 10%% de chance de faire une deuxieme attaque infligeant la moitié des dégats',
                    'Dégats':18
                    }
                ]
            }

def questionnaire():
    questions = [
        "Quelle est votre couleur préférée ?\n a) Rouge\n b) Bleu\n c) Vert\n d) Jaune\n",
        "Quelle est votre principale qualité ?\n a) Courage\n b) Intelligence\n c) Force\n d) Compassion\n",
        "Quel est votre environnement préféré ?\n a) Les montagnes\n b) La ville\n c) La forêt\n d) L'océan\n",
        "Quel est votre animal préféré parmi ceux-ci ?\n a) Loup\n b) Aigle\n c) Lion\n d) Dauphin\n",
        "Quel genre de livre préférez-vous ?\n a) Science-fiction\n b) Histoire\n c) Fantastique\n d) Philosophie\n",
        "Quelle est votre activité favorite parmi celles-ci ?\n a) Faire du sport\n b) Dessiner ou peindre\n c) Méditer\n d) Aider les autres\n",
        "Quel est votre élément préféré ?\n a) Feu\n b) Air\n c) Terre\n d) Eau\n",
        "Quelle est votre arme imaginaire de prédilection ?\n a) Épée flamboyante\n b) Arc magique\n c) Marteau de la justice\n d) Trident des profondeurs\n",
        "Quel est votre superpouvoir rêvé ?\n a) Voler\n b) Télépathie\n c) Super-force\n d) Guérison\n",
        "Quel est votre motivation principale ?\n a) Protéger les innocents\n b) Découvrir la vérité\n c) Combattre le mal\n d) Apporter la paix\n"
    ]
    
    scores = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    hero_types = {'a': 'Feu', 'b': 'Éclaireur Céleste', 'c': 'Titan Vert', 'd': 'Aquamirage'}
    
    for question in questions:
        response = input(question).strip().lower()
        while response not in ['a', 'b', 'c', 'd']:
            print("Veuillez choisir parmi les options données.")
            response = input(question).strip().lower()
        scores[response] += 1
    
    max_score = max(scores.values())
    result = [hero for hero, score in scores.items() if score == max_score]
    
    q_bonus = {'a': 'a) Tout casser sans risque de représailles',
               'b': 'b) Faire reigner la justice',
               'c': 'c) Inspirer la crainte aux criminels',
               'd': 'd) Pour venger ou faire plaisir à un proche'
               }

    if(len(result)>1):
        print('Pourquoi voulez-vous être un hero?')
        for lettre in q_bonus:
            if(lettre in result):
                print(q_bonus[lettre])
        response = input(' > ')
        while response not in result:
            print(f'Merci de donner une de ces reponses {result}')
            response = input(' > ')
        result = response
    else:
        result = result[0]

    
    return result
