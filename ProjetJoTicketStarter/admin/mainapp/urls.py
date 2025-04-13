from django.urls import path
from .views import (api, get_csrf_token, ticketChecker,validitySession, logout_view, AdminView, LoginFormView, LoginAPI, LogoutAPI, signInAPI, StadiumView, TeamView, EventView, EventsEditView, TeamsEditView, StadiumsEditView, login, TicketsView)
from django.shortcuts import redirect

# Un exemple de endpoint qui renverait les stades... Si la vue était faite :)
urlpatterns = (
    path("", lambda request: redirect("admin/")),
    path("api/", api, name="api"),
    path("api/login/", LoginAPI.as_view(), name="apiLogin"),
    path("api/logout/", LogoutAPI.as_view(), name="apiLogout"),
    path("api/signIn/", signInAPI.as_view(), name="apiSignIn"),
    path("api/stadiums/", StadiumView.as_view(), name="stadium"),
    path("api/teams/", TeamView.as_view(), name="team"),
    path("api/tickets/", TicketsView.as_view(), name="tickets"),
    path("api/events/", EventView.as_view(), name="event"),
    path("api/sessionCheck/", validitySession.as_view(), name="sessionCheck"),
    path('api/csrf/', get_csrf_token),
    path("api/checkTicket/", ticketChecker.as_view(), name="checkTicket"),

    path("admin/", AdminView.as_view(), name="admin"),
    path("admin/login/", LoginFormView.as_view(), name="login"),
    path("admin/logout/", logout_view, name="logout"),
    path("admin/events/", EventsEditView.as_view(), name="events"),
    path('admin/teams/', TeamsEditView.as_view(), name="teams"),
    path('admin/stadiums/', StadiumsEditView.as_view(), name="stadiums"),
)
