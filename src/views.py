from django.http import JsonResponse


# Create your views here.
def health_check(request):
    return JsonResponse({"status": "ok"})
