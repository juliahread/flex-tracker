from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    #flex= u'\U0001F4AA'
    #return HttpResponse("Hello, world. You're at the " + str(flex) + " index!")
    #template = loader.get_template("templates/login.html")
    #context = {}
    return render(request, "home.html")
    #return render(request, '/templates/login.html', {})
