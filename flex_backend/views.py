from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import PermissionDenied
from flex_backend.models import flex_info
from datetime import date

def index(request):
    flex= u'\U0001F4AA'
    return HttpResponse("Hello, world. You're at the " + str(flex) + " index!")

def home(request):
    if request.user.is_authenticated:
        context = {}
        context['balance'] = "%.2f" % flex_info.objects.get(user_id=request.user.id).current_flex
        context['daysLeft'] = (5 - date.today().weekday()) % 7
        return render(request, "home.html", context)
    else:
        raise PermissionDenied

def settings(request):
    if request.user.is_authenticated:
        context = {}
        context
    else:
        raise PermissionDenied
