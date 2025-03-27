from django.http import JsonResponse
from django.views.generic import View
from mainapp.models import Stadium, Team, Event

class TeamView(View):
    def get(self, request):
        stadiums= list(Team.objects.all().values('id','name','code', 'nickname'))
        return JsonResponse(stadiums, safe=False)