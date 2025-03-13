from django.http import HttpResponse
from django.shortcuts import render

from app1.models import M

def index(request):
    return HttpResponse("Hello World !")

def hello(request):
    return render(request, "hello.html", context={'request': request.META})
    #return HttpResponse("A more friendly hello back to you =)")