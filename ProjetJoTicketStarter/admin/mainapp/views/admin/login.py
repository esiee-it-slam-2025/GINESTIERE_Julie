from django import forms
from django.contrib.auth.models import User

#user = User.objects.create_user('admin')
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.shortcuts import redirect


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label="Nom d'utilisateur")
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True, label="Mot de passe")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not username or not password:
            raise forms.ValidationError("Tous les champs sont obligatoires.")

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError("Le nom d'utilisateur ou le mot de passe est incorrect.")
        except User.DoesNotExist:
            raise forms.ValidationError("Le nom d'utilisateur ou le mot de passe est incorrect.")

        return cleaned_data

    def get_user(self):
        username = self.cleaned_data.get("username")
        try:
            # We're getting the user instance by his pseudo
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None

class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = "/admin/"
    def form_valid(self, form):
        Username = self.request.POST["username"]
        Password = self.request.POST["password"]
        user = authenticate(form, username=Username, password=Password)
        if user is not None:
            login(self.request, user)
            # Redirect to a success page.
            print('success')
        else:
            # Return an 'invalid login' error message.
            print('fail')
        return super().form_valid(form)
    def post(self, request):
        redirect("admin/")
        return super().post(request)
        
    # def post(self, request):
    #     Username = request.POST["username"]
    #     Password = request.POST["password"]
    #     user = authenticate(request, username=Username, password=Password)
    #     if user is not None:
    #         login(request, user)
    #         # Redirect to a success page.
    #         print('success')
    #     else:
    #         # Return an 'invalid login' error message.
    #         print('fail')