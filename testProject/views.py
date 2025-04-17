from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60)
def index(request):
    return render(request, "base.html")

@cache_page(60)
def hello(request, category, id):
    if category == 'funky':
        raise Http404("Sorry !")
    else:
        return render(request, "hello.html",
                  context={'request': request.META, 'id': id, 'category': category})
    #return HttpResponse("A more friendly hello back to you =)")