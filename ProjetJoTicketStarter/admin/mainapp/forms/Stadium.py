from django import forms
from ..models import Stadium

class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = ['name', 'location']

''' def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['team_home'].required = False
        self.fields['team_away'].required = False
        self.fields['winner'].required = False
        self.fields['score'].required = False
        '''