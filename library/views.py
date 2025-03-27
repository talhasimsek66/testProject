# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def search(request):
    return render(request, "results.html")

