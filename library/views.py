# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from library.forms import PublisherForm
from library.models import Publisher


def home(request):
    if request.method == "post":
        # create a form instance and populate it with data from the request:
        form = PublisherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            p = Publisher()
            p.name = form.cleaned_data["name"]
            p.url = form.cleaned_data["url"]
            p.save()
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PublisherForm()

    return render(request, "home.html", {"form": form})


def search(request):
    if request.GET['name']:
        name = request.GET['name']
        results = Publisher.objects.filter(name__icontains=name)
    return render(request,
                  "results.html",
                  context = {'publishers': results})

