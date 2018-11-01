from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    flex= u'\U0001F4AA'
    return HttpResponse("Hello, world. You're at the " + str(flex) + " index!")
