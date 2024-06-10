# Projet "Minimal 6"

Afin d'utiliser dans nos templates des fichiers dits "statiques", comme des images, vidéos, sons ou encore des styles CSS, on rajoute justement l'application contrib "static" qui va faciliter la gestion et l'usage de ces derniers au sein de nos fichiers de template.

Pour réduire le code dupliqué et pour se rapprocher de la conception réelle d'un site web, nous allons voir la notion simple mais efficace de l'héritage entre plusieurs templates. Chacun de nos templates, représentant des pages différentes de notre site, prendront donc comme base le fichier `_base.html`.

## 📚 Notions

* [Fichiers statiques](https://docs.djangoproject.com/fr/4.0/howto/static-files/)
* Templates : [héritage de fichiers](https://docs.djangoproject.com/fr/4.0/ref/templates/language/#template-inheritance)

## ⏩ Démarrage du projet

    python hello.py runserver

## 🔗 URLs à essayer

* http://localhost:8000/
* http://localhost:8000/a-propos
