# Projet "Minimal 4"

Il est temps de commencer à utiliser des templates dans notre application web. Grâce à la fonction de raccourci `render()`, on peut à la fois réaliser le rendu d'un fichier template selon des données (appelé "contexte"), puis en obtenir une `HttpResponse` que notre vue pourra renvoyer.

Les templates Django utilisent leur [propre langage](https://docs.djangoproject.com/fr/4.0/ref/templates/language/) dont nous étudierons l'écriture au fil des projets.

## 📚 Notions

* Fonctions shortcut : [render()](https://docs.djangoproject.com/fr/4.0/topics/http/shortcuts/#render), [redirect()](https://docs.djangoproject.com/fr/4.0/topics/http/shortcuts/#redirect)
* Templates : [affichage de variables](https://docs.djangoproject.com/fr/4.0/ref/templates/language/#variables)
* Template tags : [if](https://docs.djangoproject.com/fr/4.0/ref/templates/builtins/#if)

## ⏩ Démarrage du projet

    python hello.py runserver

## 🔗 URLs à essayer

* http://localhost:8000/
* http://localhost:8000/search
* http://localhost:8000/search?term=test
* http://localhost:8000/meteo-a-tokyo
* http://localhost:8000/meteo-a-paris
* http://localhost:8000/meteo-a-new-york
* http://localhost:8000/meteo-a-londres
