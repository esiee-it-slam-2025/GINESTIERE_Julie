import sys
from datetime import datetime

from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect

################################################################################
# Données
################################################################################

team = [
    {
        "firstname": "John",
        "lastname": "Djangoo",
        "title": "Développeur back-end"
    },
    {
        "firstname": "Mélanie",
        "lastname": "Réacte",
        "title": "Développeuse front-end"
    },
]

################################################################################
# Vues
################################################################################

# Lorsque l'on souhaite faire par défaut le rendu et le renvoi d'un template,
# on peut alors hériter de la classe TemplateView
class Error404View(TemplateView):
    # On précise alors le fichier de template que l'on souhaite utiliser
    template_name = "error_404.html"

class HomeView(TemplateView):
    template_name = "home.html"
    # Toutes les valeurs de ce dictionnaire seront injectées dans le
    # contexte du template, ce qui peut s'avérer utile lorsque ces
    # valeurs ne changent jamais
    extra_context = {
        "page_title": "Page d'accueil"
    }

    # Tout comme dans une classe héritant de View, on peut choisir
    # d'exécuter du code uniquement lors d'une requête HTTP de type GET
    def get(self, request, *args, **kwargs):

        # On souhaite incrémenter une variable à chaque visite de la page d'accueil.
        # Si elle n'existe pas, il faut la créer. La session étant un dictionnaire,
        # il suffit de vérifier la présence d'une clé portant son nom dedans
        if not "visites" in request.session:
            # Notre variable commence donc à zéro
            request.session["visites"] = 0

        # Puis on incrémente systématiquement la variable d'une visite
        request.session["visites"] += 1

        # Vu que l'on remplace la méthode "get" de TemplateView qui s'occupe du rendu
        # du template, on peut appeler la méthode d'origine à l'aide du super() pour
        # ensuite en renvoyer le résultat, correspondant alors au comportement d'origine
        return super().get(request, *args, **kwargs)

    # Cette méthode permet de remplacer le contexte qui sera utilisé au sein
    # du template lors de son rendu par TemplateView
    def get_context_data(self, **kwargs):
        # On commence par appeler la méthode d'origine pour avoir le contexte existant,
        # toujours à l'aide de super(), pour garder son contenu existant
        context = super().get_context_data(**kwargs)
        
        # Le contexte étant un dictionnaire, on y rajoute les valeurs de notre choix
        context["heure"] = datetime.now()

        # Même sans que cette méthode reçoive la requête HTTP comme argument, on peut
        # y accéder avec self.request
        if "tempmessage" in self.request.session:
            # Le message stocké pendant la déconnexion est lu
            # puis inséré dans une nouvelle clé du contexte
            context["message"] = self.request.session["tempmessage"]
            # On supprime alors la variable de la session car elle n'est plus utile
            del self.request.session["tempmessage"]

        # Le contexte est finalement renvoyé
        return context

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # La liste "team" sera disponible dans notre template sous le nom "equipe"
        context["equipe"] = team
        return context

def logout(request):
    # On vide intégralement la session de tout son contenu
    request.session.flush()
    # Puis on y stocke un message temporaire que l'on utilisera plus tard
    request.session["tempmessage"] = "Votre session a bien été remise à zéro."
    return redirect("home")

class APITest(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Endpoint API de test")

    # Cette méthode sera exécutée lorsque la vue reçoit une requête HTTP
    # avec le verbe "POST"
    def post(self, request, *args, **kwargs):
        message = request.POST["message"]
        html = f"Message reçu : {message}"
        return HttpResponse(html)

################################################################################
# Paramètres et exécution
################################################################################

urlpatterns = (
    path("", HomeView.as_view(), name="home"),
    path("a-propos", AboutView.as_view(), name="about"),
    path("deconnexion", logout, name="logout"),
    path("api", APITest.as_view(), name="apitest"),
    # En mode debug, Django n'affichera jamais notre page prévue pour une
    # erreur 404 afin de nous afficher des informations plus utiles.
    # Il est donc coutume de créer une URL spéciale afin de nous laisser
    # accéder à cette page lorsque l'on est en train de la développer.
    path("erreur-404", Error404View.as_view()),
)

# En plus de la variable "urlpatterns", Django ira chercher une variable "handler404"
# qui détermine la vue à renvoyer systématiquement en cas d'erreur 404,
# et ce qu'importe la vue où elle apparaît
handler404 = Error404View.as_view()

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
    INSTALLED_APPS=[
        # Rajout de l'application Django gérant les sessions
        "django.contrib.sessions",
    ],
    MIDDLEWARE=[
        # Rajout du middleware Django pour gérer les sessions au niveau des requêtes/réponses HTTP
        "django.contrib.sessions.middleware.SessionMiddleware",
    ],
    # Le suivi des sessions s'effectuera à l'aide de cookies chiffrés à partir de la SECRET_KEY
    SESSION_ENGINE="django.contrib.sessions.backends.signed_cookies"
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
