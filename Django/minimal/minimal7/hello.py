import sys

from pathlib import Path

from django.conf import settings
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView, FormView
from django import forms

################################################################################
# Formulaires
################################################################################

# Tout formulaire hérite de la classe Form
class ContactForm(forms.Form):
    # Chaque attribut est automatiquement considéré comme étant un champ de formulaire
    name = forms.CharField(label="Nom")
    # label précise le nom à afficher au visiteur, sinon, Django utilisera le nom brut de l'attribut
    email = forms.EmailField(label="Adresse e-mail")
    # On peut préciser le élément HTML (widget) que l'on souhaite pour le champ, commme un <textarea>
    message = forms.CharField(label="Votre message", widget=forms.Textarea)

class ContactBootstrapForm(forms.Form):
    # Pour avoir le style de Bootstrap, il faut rajouter la classe CSS "form-control"
    # à chaque champ et donc préciser systématiquement l'élément HTML (widget) voulu
    name = forms.CharField(label="Nom", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Adresse e-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Votre message", widget=forms.Textarea(attrs={'class': 'form-control'}))

################################################################################
# Vues
################################################################################

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # On permet le fait d'afficher un message temporaire comme dans Minimal 5
        if "tempmessage" in self.request.session:
            context["message"] = self.request.session["tempmessage"]
            del self.request.session["tempmessage"]

        context["image_right"] = "tennoji.jpg"
        return context

class ContactView(FormView):
    template_name = "contact.html"
    # Tout simplement la classe Python correspondant au formulaire à utiliser
    form_class = ContactForm
    # L'attribut success_url représente l'URL vers laquelle rediriger le visiteur
    # si le formulaire a été soumis avec succès. On utilise donc la fonction
    # reverse_lazy pour calculer l'URL correspondant au motif d'URL "home"
    success_url = reverse_lazy('home')

    # Cette fonction est appelée lorsque le formulaire est valide
    def form_valid(self, form):
        # Les données du formulaire se trouve dans le dictionnaire "cleaned_data"
        name = form.cleaned_data["name"]
        # On ajoute un message temporaire dans notre session
        self.request.session["tempmessage"] = f"Merci {name} pour votre message !"
        # On laisse la méthode d'origine renvoyer une réponse HTTP
        return super().form_valid(form)


class ContactBootstrapView(FormView):
    template_name = "contact-bootstrap.html"
    form_class = ContactBootstrapForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        self.request.session["tempmessage"] = f"Merci {name} pour votre message !"
        return super().form_valid(form)

################################################################################
# Paramètres et exécution
################################################################################

urlpatterns = (
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactView.as_view(), name="contact"),
    path("contact-bootstrap", ContactBootstrapView.as_view(), name="contact-bootstrap"),
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
