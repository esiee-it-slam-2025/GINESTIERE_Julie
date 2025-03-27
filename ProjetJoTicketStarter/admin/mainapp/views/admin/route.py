from django import forms
from django.contrib.auth.models import User

#user = User.objects.create_user('admin')
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect




class AdminView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse("""
            <h1>Admin</h1>
            <a href="/admin/logout/">
                <button>Logout</button>
            </a>
            <a href="/admin/teams/">
                <button>Teams</button>
            </a>
            <a href="/admin/events/">
                <button>Events</button>
            </a>
            <a href="/admin/stadiums/">
                <button>Stadiums</button>
            </a>
                                """)
        else:
            return redirect("/admin/login/")