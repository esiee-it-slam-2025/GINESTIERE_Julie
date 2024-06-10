
import sys

from django.conf import settings
from django.urls import path
from django.http import HttpResponse, HttpResponseNotFound

################################################################################
# Données
################################################################################

names = {
    "tokyo": "Tōkyō",
    "paris": "Paris",
    "new-york": "New York"
}

temperatures = {
    "tokyo": 23,
    "paris": 17,
    "new-york": 20
}

################################################################################
# Vues
################################################################################


def index(request):
    html = f"""
    <h1>Django Minimal 2</h1>
    <h2>Bienvenue.</h2>
    """
    return HttpResponse(html)


def meteo(request, *args, **kwargs):
    # Les valeurs capturées sont transmises comme des arguments à mots clés,
    # elles se retrouvent donc dans "kwargs", qui se comporte comme un dictionnaire
    print(kwargs)
    city = kwargs.get('city')

    # Lorsque la ressource demandée n'est pas trouvée, on renvoie une erreur 404
    if not city in temperatures:
        # En plus de renvoyer un message différent pour un cas non prévu,
        # on renvoie aussi le code HTTP 404 grâce à HttpResponseNotFound
        return HttpResponseNotFound("<h1>Django Minimal 2</h1><h2>404 - Prévision météo inexistante</h2>")

    html = f"""
    <h1>Django Minimal 2</h1>
    <h2>Il fait {temperatures[city]}°c à {names[city]}.</h2>
    """
    return HttpResponse(html)

################################################################################
# Paramètres et exécution
################################################################################


urlpatterns = (
    path("", index),
    # Pour accepter une valeur dynamique dans une URL, on parle de "capture de valeur".
    # Il faut pour cela écrire entre chevrons le nom qui sera relié à cette valeur,
    # et précéder ça optionnellement d'un type de valeur accepté.
    # Ici, on accepte la valeur "city" de type "str".
    path("meteo/<str:city>", meteo),
)

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='e2y8+0rx5y(e$9@b)&vn@2%v=40@3fp+1bp&w_@e*m#yr^ya7x',
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
