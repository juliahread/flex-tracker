from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Please use Harvey Mudd Email')
    phone_number = forms.FloatField(required = False, help_text='Only if you want text reminders. Please enter as 10 digit number (xxx)xxx-xxxx with only the numbers.')
    p_choices = (('',''), ('Alltel','Alltell'), ('AT&T', 'AT&T'), ('Boost Mobile', 'Boost Mobile'), ('Cricket Wireless', 'Cricket Wireless'), ('Project Fi', 'Project Fi'),
    ('Republic Wireless', 'Republic Wireless'), ('Sprint','Sprint'), ('U.S. Cellular','U.S. Cellular'), ('Verizon','Verizon'), ('Virgin Mobile', 'Virgin Mobile'), 
    ('UNKNOWN', 'UNKNOWN'))
    provider = forms.ChoiceField(choices = p_choices, required = False, help_text='Only if you want text reminders')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number', 'provider')