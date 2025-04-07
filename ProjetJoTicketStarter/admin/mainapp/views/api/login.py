from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
import json

data = False
Username = False
Password = False

class LoginAPI(View):
    def post(self, request, *args, **kwargs):
        
        
        try:
            data = json.loads(request.body)
            Username = data.get('username')
            Password = data.get('password')

            if(not Username or not Password):
                return JsonResponse({
                    'success': False,
                    'error': 'Username and password are required'
                }, status=400)
            user = authenticate(request, username=Username, password=Password, is_superuser=False)
            if user is not None:
                login(request, user)
                return JsonResponse({
                        'success': True,
                        'user': {
                            'username': user.username,
                            # Add other user info you want to return
                        }
                    })
                # Redirect to a success page.
                print('success')
            else:
                # Return an 'invalid login' error message.
                print('fail')
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid credentials'
                }, status=401)
                
        except json.JSONDecodeError:
            # This handles if the request body isn't valid JSON
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON data'
            }, status=400)
    '''
    def post(self, request):
        redirect("admin/")
        return super().post(request)
    '''