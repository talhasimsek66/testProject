# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from library.models import Publisher


def home(request):
    return render(request, "home.html")

def search(request):
    return render(request,
                  "results.html",
                  context = {'publishers': Publisher.objects.all()
})

