from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json

data = False
Username = False
Password = False

class signInAPI(View):
    def post(self, request, *args, **kwargs):
        
        
        try:
            data = json.loads(request.body)
            #Username = data.get('username')
            Password = data.get('password')
            Password_Confirm = data.get('password_confirm')
            Email = data.get('email')
            First_Name = data.get('first_name')
            Last_Name = data.get('last_name')

            #print(Username)
            print(Password)
            print(Password_Confirm)
            print(Email)
            print(First_Name)
            print(Last_Name)

            if(Password != Password_Confirm):
                return JsonResponse({
                    'success': False,
                    'error':"Both password and password confirmation must be the same",
                }, status=400)


            if(not Password or not Email or not First_Name or not Last_Name):
                return JsonResponse({
                    'success': False,
                    'error': 'Username, password, email, first and last name are required'
                }, status=400)




            ### USER CREATION ###
            User(
                
            )
            user, created = User.objects.get_or_create(
                username=Email,
                email=Email,
                first_name=First_Name,
                last_name=Last_Name,
                )
            print(user)
            if(created):
                user.set_password(Password)
                user.save()
                return JsonResponse({
                    "success": True,
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Email already used"
                })
            
                
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