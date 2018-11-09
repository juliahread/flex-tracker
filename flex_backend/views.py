from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import LogInForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'home.html')
    else:
        form = LogInForm()

    return render(request, 'login.html', {'form': form})
