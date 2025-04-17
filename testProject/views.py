from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60*10)
def home(request):
    return render(request, "base.html")

@cache_page(60*10)
def testview(request, category, id):
    if category == 'funky':
        raise Http404("Sorry !")
    else:
        return render(request,
                      "testview.html",
                      context={'remote': request.META['REMOTE_ADDR'],
                           'id': id,
                           'category': category})
