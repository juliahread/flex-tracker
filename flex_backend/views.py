from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import PermissionDenied
from flex_backend.models import flex_info
from datetime import date
from accounts.models import SignUpForm

#TODO: Comments!
def index(request):
    flex= u'\U0001F4AA'
    return HttpResponse("Hello, world. You're at the " + str(flex) + " index!")

def home(request):
    if request.user.is_authenticated:
        context = {}
        context['title'] = 'Flex Tracker'
        context['daysLeft'] = (5 - date.today().weekday()) % 7
        try:
            context['balance'] = "%.2f" % flex_info.objects.get(user_id=request.user.id).current_flex
            return render(request, "main.html", context)
        except:
            context['balance'] = -1
            return render(request, "main.html", context)
    else:
        return redirect('login')

def suggestions(request):
    if request.user.is_authenticated:
        context = {}
        context['title'] = 'Spending Suggestions'
        return render(request, "main.html", context)

def locations(request):
    if request.user.is_authenticated:
        context = {}
        context['title'] = 'Locations & Availability'
        return render(request, "main.html", context)

def settings(request):
    if request.user.is_authenticated:
        context = {}
        context['title'] = 'Settings'
        context['sendEmails'] = flex_info.objects.get(user_id=request.user.id).email_notification
        context['sendTexts'] = flex_info.objects.get(user_id=request.user.id).text_notification
        return render(request, "main.html", context)
    else:
        raise PermissionDenied
