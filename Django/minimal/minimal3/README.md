# Projet "Minimal 3"

Pour ce projet, nous allons apprendre le minimum nécessaire pour simuler le comportement d'une API.

Pour rappel, une requête HTTP envoyée à une URL possède toujours un "verbe" afin que le serveur web qui la traite puisse y répondre différemment si besoin. Le verbe HTTP par défaut est `GET`, lorsque vous ouvrez une URL dans un navigateur par exemple. Lorsque l'on soumet un formulaire web, le verbe HTTP utilisé est souvent `POST`. Il existe aussi de [nombreux autres verbes HTTP](https://developer.mozilla.org/fr/docs/Web/HTTP/Methods).

Dans notre application web, on peut évidemment répondre différemment selon le verbe de la requête HTTP reçue. Pour faciliter cela, on va définir nos vues à l'aide de classes plutôt que de simples fonctions. Aussi, nous allons répondre avec du contenu au [format JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation), une chose coutume pour une API.

## 📚 Notions

* Vues : [classe View](https://docs.djangoproject.com/fr/4.0/topics/class-based-views/intro/#using-class-based-views)
* [HttpRequest](https://docs.djangoproject.com/fr/4.0/ref/request-response/#httprequest-objects) : données POST
* [JsonResponse](https://docs.djangoproject.com/en/4.0/ref/request-response/#jsonresponse-objects)

## ⏩ Démarrage du projet

    python hello.py runserver

## 🔗 URLs à essayer

Il existe de nombreuses façons de créer une requête HTTP avec un verbe autre que `GET`, à l'aide d'un outil en ligne de commande par exemple. Pour se faciliter la tâche, on peut évidemment utiliser un outil avec interface graphique tel que Postman.

* http://localhost:8000/
* http://localhost:8000/article/15

Pour la dernière URL, vous pouvez faire varier le chiffre, changer le verbe de la requête HTTP en `POST` tout en passant une valeur dans le champ `content` afin de constater la réponse en conséquence.

L'outil `curl` permet de tester rapidement cette URL avec un verbe `POST` et une valeur dans la variable `content` :

    curl -X POST -F content=Texte_du_contenu http://localhost:8000/article/15
