from django.http import HttpResponse
from django.views.generic import FormView
from django import forms
from django.urls import reverse_lazy




class QuizzForm(forms.Form):
    
    rep = forms.CharField(label="Comment ça s'appel?")


class QuizzView(FormView):
    form_class= QuizzForm

    template_name="Quizz.html"

    success_url = reverse_lazy('result')


    def form_valid(self, form):
        rep = form.cleaned_data["rep"]
        self.request.session["answer"] = rep

        return super().form_valid(form)