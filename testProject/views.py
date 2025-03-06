from django.http import HttpResponse
from app1.models import M

def index(request):
    return HttpResponse("Hello World !" + M.objects.first().name)