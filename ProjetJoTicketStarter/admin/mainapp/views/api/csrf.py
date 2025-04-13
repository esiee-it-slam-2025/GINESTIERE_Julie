from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET

@require_GET
@ensure_csrf_cookie
def get_csrf_token(request):
    """
    View that simply returns a 200 OK response and sets the CSRF cookie.
    This is used to obtain a CSRF token before making POST requests.
    """
    return JsonResponse({'success': True})