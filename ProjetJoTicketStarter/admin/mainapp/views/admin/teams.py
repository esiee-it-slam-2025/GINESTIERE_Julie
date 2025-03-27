from django.views.generic.base import TemplateView
from ..api import EventView, TeamView, StadiumView
from django.shortcuts import render
import json, html

'''class EventsEditView(TemplateView):
    template_name = "events.html"
    def get(self,request):
        event_view = EventView()
        event_response = event_view.get(request)
        event_list = event_response.content.decode()
        event_list = json.loads(event_list)
        
        team_view = TeamView()
        team_response = team_view.get(request)
        team_list = team_response.content.decode()
        team_list = json.loads(team_list)
        
        stadium_view = StadiumView()
        stadium_response = stadium_view.get(request)
        stadium_list = stadium_response.content.decode()
        stadium_list = json.loads(stadium_list)

        print(stadium_list[0]['id'])
        stadium_select =f""#"
        # <select name="pets" id="pet-select">"""
        
        for stadium in stadium_list:
            stadium_select += f"""<option value="{stadium['id']}">{html.escape(stadium['name'])}</option>"""
        
        stadium_select +="</select>"
        
        team_select =f""#"
        # <select name="pets" id="pet-select">"""
        
        for team in team_list:
           team_select += f"""<option value="{team['id']}">{html.escape(team['name'])}</option>"""
        
        team_select +="</select>"
        print(stadium_list)
        context = {
            "events": event_list,
            "teams": team_list,
            "stadiums": stadium_list,
            
        }
        print(event_list)
        return render(request, self.template_name, context)
'''

from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from ...models import Team
from ...forms import TeamForm

class TeamsEditView(TemplateView):
    template_name = 'teams_edit.html'
    
    def get(self, request):
        if request.user.is_superuser:
            TeamFormSet = modelformset_factory(Team, form=TeamForm, extra=0)
            formset = TeamFormSet(queryset=Team.objects.all())
            return render(request, self.template_name, {'formset': formset})
        else:
            return redirect("/admin/login/")

    def post(self, request):
        if request.user.is_superuser:
            TeamFormSet = modelformset_factory(Team, form=TeamForm, extra=0)
            formset = TeamFormSet(request.POST)
            if formset.is_valid():
                formset.save()
                return redirect('events')  # Adjust the URL name as needed
            return render(request, self.template_name, {'formset': formset})
        # else: