from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth import logout

class LogoutAPI(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse(
            {
                "message": "Successfully loged out"
            },
            status=200
        )