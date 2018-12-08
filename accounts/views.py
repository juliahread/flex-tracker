from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.phone_number = form.cleaned_data.get("phone_number")
            user.provider = form.cleaned_data.get("provider")
            user.save()            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
<<<<<<< HEAD
            return redirect('tutorial')
=======
            return redirect('home')
>>>>>>> 434556aa6e8e1680914b7230694a20440d93ef9a
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'error': 'test'})
