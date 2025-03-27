from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, "base.html")

def hello(request, category, id):
    if category == 'funky':
        raise Http404("Sorry !")
    else:
        return render(request, "hello.html",
                  context={'request': request.META, 'id': id, 'category': category})
    #return HttpResponse("A more friendly hello back to you =)")