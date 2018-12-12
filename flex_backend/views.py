from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import PermissionDenied
from flex_backend.models import flex_info
from datetime import date
from accounts.forms import SignUpForm
from uploading.alg import *
from django.contrib.auth.models import User


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
        try:
            flex_amount = flex_info.objects.get(user_id=request.user.id).current_flex
            suggestions_list = []
            suggestions_list.append(optimize(flex_amount))  
            suggestions_list.append(optimize(flex_amount))  
            suggestions_list.append(optimize(flex_amount))  
            context['suggestions'] = suggestions_list
        except Exception as e: 
            print(e)
            context['error'] = ['No flex information found']
        return render(request, "main.html", context)
    else:
        return redirect('login')

def locations(request):
    if request.user.is_authenticated:
        context = {}
        context['title'] = 'Locations & Availability'
        return render(request, "main.html", context)

def settings(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                data = myform.clean_data
                if "old" in data:

                    user = authenticate(username=request.user.username, password=data["old"])
                    if user is not None:
                        # Need to add check for good password
                        if True:
                            user = User.objects.get(username=user.username)
                            user.set_password(data["new"])
                        ## Old pass word was correct
                    else:
                        ## Old Pass was not correct
                        pass
                if "sendEmails" in data:
                    flex = flex_info.objects.get(user_id=request.user.id)
                    flex.text_notification = None
                    pass
                if "sendTexts" in data:
                    flex = flex_info.objects.get(user_id=request.user.id)
                    flex.text_notification
                    pass
                if "current" in data and "new" in data :
                    user = User.objects.get(username=request.user.username)
                    user.email = data['new']

                

        context = {}
        context['title'] = 'Settings'
        try:
            context['sendEmails'] = flex_info.objects.get(user_id=request.user.id).email_notification
            context['sendTexts'] = flex_info.objects.get(user_id=request.user.id).text_notification
        except:
            context['sendEmails'] = None
            context['sendTexts'] = None
        return render(request, "main.html", context)
    else:
        raise PermissionDenied
