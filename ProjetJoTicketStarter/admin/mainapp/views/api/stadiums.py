from django.http import JsonResponse
from django.views.generic import View
from mainapp.models import Stadium, Team, Event

class StadiumView(View):
    def get(self, request):
        stadiums= list(Stadium.objects.all().values('id','name','location'))
        return JsonResponse(stadiums, safe=False)