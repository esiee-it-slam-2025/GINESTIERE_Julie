# Projet "Minimal 5"

Lorsqu'une vue utilise principalement des templates, Django nous propose d'hériter d'une classe bien plus pratique pour cet effet. Nous continuerons à voir de nouveaux tags et filtres utilisables au sein d'un template.

Aussi, nous allons utiliser le système de "sessions" servant à garder en mémoire certaines informations à travers plusieurs pages voire plusieurs visites d'un même visiteur. Bien qu'il existe plusieurs façons de reconnaître la session d'un visiteur en particulier, cela se fait généralement en déposant un cookie dans le navigateur de ce dernier.

Par rapport aux récentes législations comme le [RPGD](https://www.cnil.fr/fr/cookies-et-traceurs-que-dit-la-loi), l'usage d'une session à l'aide d'un dépôt de cookie pourrait facilement rentrer dans le cas où il faille demander au visiteur son consentement au préalable. Cependant, l'usage d'un cookie pour assurer le fonctionnement strictement minimal du site web tel que voulu par l'utilisateur (pour faire fonctionner la connexion de ce dernier à son compte par exemple) consiste une exception. En réalité, la plupart des sites internet utilisant des systèmes d'analyse d'audience ainsi que des affichages publicitaires, leur usage des cookies dépasse largement le spectre du "fonctionnement minimal" et il leur faut demander un consentement à l'utilisateur.

## 📚 Notions

* [TemplateView](https://docs.djangoproject.com/fr/4.0/ref/class-based-views/base/#templateview)
* Templates : variable autogénérée ["request"](https://docs.djangoproject.com/fr/4.0/ref/templates/api/#django-template-context-processors-request)
* Template tags : [url](https://docs.djangoproject.com/fr/4.0/ref/templates/builtins/#url), [for](https://docs.djangoproject.com/fr/4.0/ref/templates/builtins/#for)
* Template filters : [date](https://docs.djangoproject.com/fr/4.0/ref/templates/builtins/#date), [upper](https://docs.djangoproject.com/fr/4.0/ref/templates/builtins/#upper)
* [Sessions](https://docs.djangoproject.com/fr/4.0/topics/http/sessions/)
* [Handler404](https://docs.djangoproject.com/fr/4.0/ref/urls/#handler404)

## ⏩ Démarrage du projet

    python hello.py runserver

## 🔗 URLs à essayer

* http://localhost:8000/
* http://localhost:8000/a-propos
* http://localhost:8000/deconnexion
* GET http://localhost:8000/api
* POST http://localhost:8000/api
