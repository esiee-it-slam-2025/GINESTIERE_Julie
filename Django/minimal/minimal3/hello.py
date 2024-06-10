
import sys

from django.conf import settings
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.views import View

################################################################################
# Vues
################################################################################

# Notre vue est désormais une classe, qui hérite de la classe View
class HomeView(View):

    # On peut définir une méthode pour chaque verbe HTTP existant,
    # et Django s'en servira automatiquement selon le verbe de la requête reçue
    def get(self, request, *args, **kwargs):
        html = f"""
        <h1>Django Minimal 3</h1>
        <h2>Page d'accueil</h2>
        """
        return HttpResponse(html)

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        response = {
            "article_id": article_id,
            "content": "Contenu de l'article ici..."
        }
        # Par rapport à un HttpResponse, le JsonResponse va :
        # 1) Sérializer automatiquement la valeur Python vers en JSON
        # 2) Renvoyer une réponse HTTP avec le bon Content-Type "application/json"
        return JsonResponse(response)

    # Cette méthode sera donc utilisée pour les requêtes ayant le verbe POST
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')

        # Pour récupérer les données transmises dans le corps de la requête HTTP,
        # on va utiliser request.POST qui se comporte comme un dictionnaire
        article_content = request.POST.get('content')

        # Si l'on considère que la requête reçue est incomplète, on peut
        # renvoyer une réponse différente avec un code de statut 400 qui
        # laisse entendre une requête erronée
        if article_content is None:
            response = {
                "error": "Missing 'content' field"
            }
            return JsonResponse(response, status=400)
        
        # Une vraie API irait enregistrer quelque chose dans ce cas,
        # mais nous allons rester simple pour ce projet et juste
        # renvoyer les données reçues
        response = {
            "article_id": article_id,
            "content": article_content,
            "status": "saved"
        }
        return JsonResponse(response)

################################################################################
# Paramètres et exécution
################################################################################

urlpatterns = (
    # Pour lier une vue à une URL, une méthode est prévue à cet effet sur la classe : as_view()
    path("", HomeView.as_view()),
    path("article/<int:id>", ArticleView.as_view()),
)

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='e2y8+0rx5y(e$9@b)&vn@2%v=40@3fp+1bp&w_@e*m#yr^ya7x',
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
