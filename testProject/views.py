from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from ollama import Client
from testProject.settings import OLLAMA

@cache_page(60 * 10)
def home(request):
    return render(request, "base.html")


@cache_page(60 * 10)
def chat(request):
    client = Client(host=OLLAMA['LOCATION'])
    country = request.GET.get('country')
    response = client.chat(model=OLLAMA['MODEL'], messages=[
        {
        'role': 'user',
        'content': 'What is the capital of ' + country + ' ?',
        },
    ])

    return render(request, template_name="result.html", context= {
                                                        'country': country,
                                                        'response': response.message.content
    })
