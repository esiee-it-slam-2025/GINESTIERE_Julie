# Exercice "Mini TP 2"

Premier vrai projet Django

## Réalisation
Réaliser une petite application Django à partir de ce que l'ont vient de voir dans le cours.

Générer un projet Django avec la commande `django-admin startproject minitp2`

Vous pouvez vous inspirer de `starterapp` pour créer les dossiers (notament les dossiers views, templates, et static)

### ⚠️ Pensez à :
- Ajouter le nom de votre appli (`minitp2` dans la liste `INSTALLED_APPS` de votre config)
- Importer les classes que vous utilisez
- Importer vos vue dans le fichier `urls.py`

L'application doit contenir 3 pages :
- Une page d'accueil (URL de base)
  - Entête
  - Texte de bienvenu
  - Image (n'importe la quelle)
- Une page de quizz
  - Une question (n'importe la quelle)
  - Un champ nom
  - Un champ réponse
  - Un bouton envoyer
  - La validation du formulaire envoi sur la page résultat
- Une page de résultat
  - Si le quizz a été validé
    - Un message de remerciement avec le nom de l'utilisateur
    - Si la réponse est bonne un message de succes
    - Si la réponse est mauvaise un message d'echec
  - Si le quizz n'a pas été validé
    - Un message qui demande de faire le quizz avant tout
    - Un lien vers le quizz

## Objectif
L'application doit gérer plusieurs URL :
- La page d'accueil (URL par defaut)
- La page quizz : `/quizz`
- La page résultat : `/result`

Il faut donc utiliser **3 vues** et **3 templates**

Les 3 pages ont une base commune (entête), utilisez l'héritage de template pour ne pas duppliquer de code.

Les liens sont à écrire dans le template via leur nom dans le router en utilisant la notation `{% url "page" %}`

La page quizz doit utiliser une vue de type FormView et un formulaire sous forme d'une classe

Il faudra utiliser l'affichage conditionnel pour la page de résultat, 2 conditions à prévoir : 
- L'utilisateur à rempli ou non le formulaire juste avant
- L'utilisateur à donné ou non la bonne réponse

## Conseil
- Allez **pas à pas**
- Faites des **logs** (print()), ils apparaitront dans votre terminal !
- Posez des questions, ne restez pas bloqué