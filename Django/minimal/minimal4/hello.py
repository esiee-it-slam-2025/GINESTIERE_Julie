
import sys
from datetime import datetime

from django.conf import settings
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

################################################################################
# Données
################################################################################

previsions = {
    "tokyo": {
        "name": "Tōkyō",
        "temperature": 23
    },
    "paris": {
        "name": "Paris",
        "temperature": 17
    },
    "new-york": {
        "name": "New York",
        "temperature": 20
    }
}

################################################################################
# Vues
################################################################################


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # render() accepte comme 1er argument la requête HTTP reçue,
        # et comme 2e argument le nom du fichier de template à utiliser
        response = render(request, "home.html")
        # On peut donc directement renvoyer le résultat de render()
        return response


class SearchView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get("term")
        # Pour passer des valeurs à un template, on passe par ce qu'on
        # appelle un "contexte", c'est à dire un dictionnaire contenant
        # toutes les variables qui seront lisibles dans notre template
        context = {
            "search_term": term,
        }
        return render(request, "search.html", context)


class WeatherView(View):
    def get(self, request, *args, **kwargs):
        city = kwargs.get("city")

        # Si la ville demandée n'existe pas, on préfère rediriger vers la
        # page d'accueil de notre site web grâce au raccourci redirect()
        # auquel on passe le nom de l'URL cible
        if city not in previsions.keys():
            return redirect("home")

        context = {
            "previsions": previsions[city]
        }
        return render(request, "meteo.html", context)

################################################################################
# Paramètres et exécution
################################################################################


urlpatterns = (
    # On peut attribuer un nom à une URL afin d'y faire référence dans le code
    # sans soucis même si le chemin de l'URL change à l'avenir
    path("", HomeView.as_view(), name="home"),
    path("search", SearchView.as_view()),
    path("meteo-a-<slug:city>", WeatherView.as_view()),
)

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="e2y8+0rx5y(e$9@b)&vn@2%v=40@3fp+1bp&w_@e*m#yr^ya7x",
    # Configuration nécessaire à l'usage de templates
    TEMPLATES=[
        {
            # Usage du moteur de templates par défaut de Django
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            # Indique dans quels dossiers se trouvent les fichiers templates
            "DIRS": [
                "templates",
            ],
            # Indique les données auxquelles on veut avoir accès au sein des templates
            "OPTIONS": {
                "context_processors": [
                    # Pour accéder à des infos de débug
                    "django.template.context_processors.debug",
                    # Pour accéder à la requête HttpRequest de la vue qui utilise notre template
                    "django.template.context_processors.request",
                ],
            },
        },
    ],
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
