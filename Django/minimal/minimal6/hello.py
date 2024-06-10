import sys

from pathlib import Path

from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

################################################################################
# Vues
################################################################################

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # On stocke dans le contexte le nom d'un fichier statique que l'on voudra
        # utiliser dans le template
        context["image_right"] = "tennoji.jpg"
        return context

class AboutView(TemplateView):
    template_name = "about.html"

################################################################################
# Paramètres et exécution
################################################################################

urlpatterns = (
    path("", HomeView.as_view(), name="home"),
    path("a-propos", AboutView.as_view(), name="about"),
)

# On garde de côté le chemin absolu vers le dossier de notre projet
BASE_DIR = Path(__file__).resolve().parent

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
        "django.contrib.sessions",
        # Rajout de l'application Django gérant les fichiers statiques
        "django.contrib.staticfiles",
    ],
    MIDDLEWARE=[
        "django.contrib.sessions.middleware.SessionMiddleware",
    ],
    SESSION_ENGINE="django.contrib.sessions.backends.signed_cookies",
    # Indique à Django dans quels dossier(s) aller chercher les fichiers statiques auxquels
    # on fera appel, dans nos templates par exemple avec la balise {% static %}
    STATICFILES_DIRS=[
        # C'est bien l'opérateur "diviser" que l'on utilise ici, mais mis à la suite
        # du BASE_DIR, il permet de concaténater des chemins.
        BASE_DIR / "static"
    ],
    # Préfixe utilisé sur toutes les URLs qui viseront des fichiers statiques
    STATIC_URL="/assets/"
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
