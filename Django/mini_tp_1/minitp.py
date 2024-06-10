
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

teams = {
    "france": {
        "nickname": "Les bleus",
        "win": 12
    },
    "bresil": {
        "nickname": "La selecao",
        "win": 11
    },
    "belgique": {
        "nickname": "Les diables rouges",
        "win": 2
    }
}

################################################################################
# Vues
################################################################################

# Créer une vue HomeView où on redéfini la méthode get pour renvoyer le template home.html
class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={
            "teams": teams
        }

        response = render(request, 'home.html', context)
        return response

class TeamView(View):
    def get(self, request, *args, **kwargs):
        global teams
        team = kwargs.get('team')
        if team in teams:
            context = {
                "pays":team,
                "team": teams[team]
            }
            response = render(request, 'team.html', context=context)
            return response
        else:
            return HttpResponse("<h1>404 not found</h1>")

class TeamData(View):
    def get(self, request, *args, **kwargs):
        
        global teams
        team = kwargs.get('team')
        if team in teams:
            return JsonResponse(teams[team], status=200)
        else:
            return JsonResponse({"error": "no team with this name"})
# Créer une vue TeamView qui renvoi le template team.html, avec les données nécéssaire à l'affichage de celui ci

# Créer une vue TeamView qui renvoi en JSON les données de l'équipe


################################################################################
# Paramètres et exécution
################################################################################


# Router
urlpatterns = (
    # Définir vues à utiliser en fonction de l'URL
    path("", HomeView.as_view()),
    path("equipe/<str:team>", TeamView.as_view()),
    path("equipe/data/<str:team>", TeamData.as_view()),
)

# Settings
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="e2y8+0rx5y(e$9@b)&vn@2%v=40@3fp+1bp&w_@e*m#yr^ya7x",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [
                "templates",
            ],
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                ],
            },
        },
    ],
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
