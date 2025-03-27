from django import forms
from ..models import Event, Stadium, Team
from django.utils.dateparse import parse_datetime

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['stadium', 'team_home', 'team_away', 'start', 'score', 'winner']
        widgets = {
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['team_home'].required = False
        self.fields['team_away'].required = False
        self.fields['winner'].required = False
        self.fields['score'].required = False