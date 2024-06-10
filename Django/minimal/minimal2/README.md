# Projet "Minimal 2"

Pour commencer à avoir une application web dynamique, nous allons faire en sorte d'avoir des URLs dynamiques qui peuvent accepter différentes valeurs, que nous pourrons utiliser afin de renvoyer des pages au contenu différent.

Le but sera simplement de renvoyer une (fausse) prévision météo pour trois villes, selon l'URL ouverte. Également, nous allons utiliser une nouvelle façon de répondre à une requête lorsque l'on veut renvoyer une erreur 404.

## 📚 Notions

* URLconf : [syntaxe](https://docs.djangoproject.com/fr/4.0/topics/http/urls/#example)
* Vues : kwargs
* [HttpResponseNotFound](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpResponseNotFound)

## ⚙️ Démarrage du projet

    python hello.py runserver

## 🔗 URLs à essayer

* http://localhost:8000/
* http://localhost:8000/meteo/tokyo
* http://localhost:8000/meteo/paris
* http://localhost:8000/meteo/new-york
* http://localhost:8000/meteo/london
