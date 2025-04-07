from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
import json
from django.contrib.auth import logout

data = False
Username = False
Password = False

class validitySession(View):

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return JsonResponse({
                "sessionValid" : True
            })
        else:
            logout(request)
            return JsonResponse({
                "sessionValid" : False
            })