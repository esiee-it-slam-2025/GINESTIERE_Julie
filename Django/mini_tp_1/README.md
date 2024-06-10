# Exercice "Mini TP 1"

La meilleure manière de comprendre le fonctionnement de Django reste de l'utiliser !
(Pensez bien à vérifier si vous avez installé Django)

## Réalisation
Réaliser une mini application Django à partir du fichier `minitp.py`, une base de code existe déjà sur ce fichier.

La page d'accueil contient simplement la liste des équipes (écrites en dur dans le HTML) avec un lien clicable permettant d'acceder à la page de cette équipe.

La page équipe contient le surnom de l'équipe et un message, ce message est différent si l'équipe à plus ou moins de 10 victoire (clé `win` dans le dictionnaire `teams`). Elle contient également un lien permettant d'acceder à toute les informations de l'équipe au format JSON.

Si le nom de l'équipe tapé dans l'URL n'existe pas dans la page *équipe* ou *données équipe* rediriger vers l'accueil

## Objectif
L'application doit donc gérer plusieurs URL :
- La page d'accueil (URL par defaut)
- La page équipe : `/equipe/<nomDeLEquipe>`
- Les données d'une équipe : `/equipe/<nomDeLEquipe>/data`

Il faut donc utiliser **3 vues** et **2 templates** (à remplir)

Pour le moment les liens sont à écrire **en dur** en HTML, à terme nous les rendront automatique.

La page équipe doit afficher le surnom de l'équipe et afficher un contenu différent selon le résultat de la condition décrite ci dessus.
De plus cette page affiche un lien qu'il faudra **construire de manière dynamique** (avec le nom de l'équipe).

Faire une **redirection** vers la *home* si le nom de l'équipe saisie dans l'URL n'existe pas

Pour lancer l'application `python minitp.py runserver`

## Conseil
- Allez **pas à pas**
- Faites des **logs** (print()), ils apparaitront dans votre terminal !
- Verifiez bien que vos données passent entre votre **vue** et votre **template**.