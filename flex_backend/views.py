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
        try:
            context['balance'] = "%.2f" % flex_info.objects.get(user_id=request.user.id).current_flex
            context['daysLeft'] = (5 - date.today().weekday()) % 7
            return render(request, "home.html", context)
        except:
            return render(request, "tutorial.html", context)
    else:
        return redirect('login')

def settings(request):
    if request.user.is_authenticated:
        context = {}
        context['sendEmails'] = flex_info.objects.get(user_id=request.user.id).email_notification
        context['sendTexts'] = flex_info.objects.get(user_id=request.user.id).text_notification
        return render(request, "settings.html", context)
    else:
        raise PermissionDenied
