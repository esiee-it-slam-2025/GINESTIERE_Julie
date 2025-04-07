from django.http import JsonResponse
from django.views.generic import View
from mainapp.models import Stadium, Team, Event

class EventView(View):
    def get(self, request):
        events= Event.objects.select_related('stadium', 'team_home', 'team_away', 'winner')
        



        data = [
        {
            "id": event.id,

            "start": event.start,
            "score": event.score,
            "winner": event.winner.id if event.winner else None,
            
            "stadium": {
                "id": event.stadium.id,
                "name": event.stadium.name,
                "location": event.stadium.location
            } if event.stadium else None,

            "team_home": {
                "id": event.team_home.id,
                "name": event.team_home.name,
                "nickname": event.team_home.nickname,
                "code": event.team_home.code,
            } if event.team_home else None,

            "team_away": {
                "id": event.team_away.id,
                "name": event.team_away.name,
                "nickname": event.team_away.nickname,
                "code": event.team_away.code,
            } if event.team_away else None,

        }
        for event in events
    ]
        
        return JsonResponse(data, safe=False)
    
def EventRefactor(id):
    event= Event.objects.select_related('stadium', 'team_home', 'team_away', 'winner').get(id=id)
    
    return {
            "id": event.id,

            "start": event.start,
            "score": event.score,
            "winner": event.winner.id if event.winner else None,
            
            "stadium": {
                "id": event.stadium.id,
                "name": event.stadium.name,
                "location": event.stadium.location
            } if event.stadium else None,

            "team_home": {
                "id": event.team_home.id,
                "name": event.team_home.name,
                "nickname": event.team_home.nickname,
                "code": event.team_home.code,
            } if event.team_home else None,

            "team_away": {
                "id": event.team_away.id,
                "name": event.team_away.name,
                "nickname": event.team_away.nickname,
                "code": event.team_away.code,
            } if event.team_away else None,

        }