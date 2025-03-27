from django.http import JsonResponse

def api(request):
    return JsonResponse({'status' : 'UP'})
