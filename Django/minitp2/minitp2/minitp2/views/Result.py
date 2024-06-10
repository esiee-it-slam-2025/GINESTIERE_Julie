from django.views.generic import TemplateView

class ResultView(TemplateView):
    template_name = "Result.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not "answer" in self.request.session:
            context["result"]={
                "type":"Error",
                "message":"Vous n'avez pas repondu à cette question"
            }
        else:
            context["result"]={"type":"","message":""}
            context["result"]["type"]="False"
            match (self.request.session["answer"]).lower():
                case "requin":
                    context["result"]["message"]="Presque! Soit plus précis!"
                case "blahaj":
                    context["result"]={
                        "type":"True",
                        "message":"BRAVOOOO!!!"
                    }
                case _:
                    context["result"]["message"]="Alors là.... Pas dutout....."
    

        return context
    