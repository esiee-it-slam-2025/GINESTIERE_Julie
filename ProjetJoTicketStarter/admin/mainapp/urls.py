from django.urls import path
from .views import (api,logout_view, AdminView, LoginFormView, StadiumView, TeamView, EventView, EventsEditView, TeamsEditView, StadiumsEditView)
from django.shortcuts import redirect

# Un exemple de endpoint qui renverait les stades... Si la vue était faite :)
urlpatterns = (
    path("", lambda request: redirect("admin/")),
    path("api/", api, name="api"),
    path("api/stadiums/", StadiumView.as_view(), name="stadium"),
    path("api/teams/", TeamView.as_view(), name="team"),
    path("api/events/", EventView.as_view(), name="event"),

    path("admin/", AdminView.as_view(), name="admin"),
    path("admin/login/", LoginFormView.as_view(), name="login"),
    path("admin/logout/", logout_view, name="logout"),
    path("admin/events/", EventsEditView.as_view(), name="events"),
    path('admin/teams/', TeamsEditView.as_view(), name="teams"),
    path('admin/stadiums/', StadiumsEditView.as_view(), name="stadiums"),
)
