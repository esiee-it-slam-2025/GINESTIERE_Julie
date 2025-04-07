from django.http import JsonResponse
from django.views.generic import View
from mainapp.models import Stadium, Team, Event, Ticket
from .events import EventRefactor 
import uuid
import json

class TicketsView(View):
    def get(self, request):
        if(request.user.is_authenticated):
        
            if(request.user.is_staff or request.user.is_superuser):
                tickets= list(Ticket.objects.all().values('uuid','category','event_id', 'user_id'))
                
                data = [
                    {
                        "uuid":ticket['uuid'],
                        "category":ticket['category'],
                        "event":EventRefactor(ticket['event_id']),
                        "user_id":ticket['user_id']
                    }
                    for ticket in tickets
                ]
                return JsonResponse(data, safe=False)
            
            else:
                tickets = list(Ticket.objects.filter(user_id=request.user.id).values('uuid','category','event_id', 'user_id'))
                
                data = [
                    {
                        "uuid":ticket['uuid'],
                        "category":ticket['category'],
                        "event":EventRefactor(ticket['event_id']),
                    }
                    for ticket in tickets
                ]
                return JsonResponse(data, safe=False)
        else:
            return JsonResponse({}, safe=False)
    
    def post(self, request):
        response = {}
        try:
            data = json.loads(request.body)
            PM = int(data.get('platinium'))
            GD = int(data.get('gold'))
            SR = int(data.get('silver'))
            eventId = data.get('eventId')
            
            event= Event.objects.get(id=eventId)
            
            for i in range(PM):
                Ticket.objects.create(
                    uuid=uuid.uuid4(),
                    user=request.user,
                    event=event,
                    category="PM"
                )
            for i in range(GD):
                Ticket.objects.create(
                    uuid=uuid.uuid4(),
                    user=request.user,
                    event=event,
                    category="GD"
                )
            for i in range(SR):
                Ticket.objects.create(
                    uuid=uuid.uuid4(),
                    user=request.user,
                    event=event,
                    category="SR"
                )
        
        except:
            response = {
                "error":'Erreur de création de billet'
            }
        return JsonResponse(response)