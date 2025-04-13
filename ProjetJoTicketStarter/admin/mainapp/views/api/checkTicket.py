from django.http import JsonResponse
from django.views.generic import View
from mainapp.models import Stadium, Team, Event, Ticket

import json

class ticketChecker(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        ticketId = data.get('ticketId')
        eventId = data.get('eventId')
        
        validity='pending'
        try:
            tickets = Ticket.objects.get(uuid=ticketId) #.values('uuid','category','event_id', 'user_id')
        
            if tickets:
                if(tickets.event.id == eventId):
                    validity = 'valid'
                else:
                    validity = 'wrong'
            else:
                validity ='invalid'
        except:
            validity="invalid"
        
        data = {
            'validity':validity
        }
        return JsonResponse(data, safe=False)