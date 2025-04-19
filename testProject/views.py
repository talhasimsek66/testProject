from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

import ollama
from ollama import Client, ResponseError

model = 'gemma3:1b'


@cache_page(60 * 10)
def home(request):
    return render(request, "base.html")


@cache_page(60 * 10)
def chat(request):
    client = Client(host='http://ollama:911')
    country = request.GET.get('country')
    response = client.chat(model=model, messages=[
        {
        'role': 'user',
        'content': 'What is the capital of ' + country + ' ?',
        },
    ])

    return render(request, template_name="result.html",
                  context={'country': country,
                           'response': response.message.content})
