from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CompleteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_number = models.FloatField()
    p_choices = (('',''), ('Alltel','Alltell'), ('AT&T', 'AT&T'), ('Boost Mobile', 'Boost Mobile'), ('Cricket Wireless', 'Cricket Wireless'), ('Project Fi', 'Project Fi'),
    ('Republic Wireless', 'Republic Wireless'), ('Sprint','Sprint'), ('U.S. Cellular','U.S. Cellular'), ('Verizon','Verizon'), ('Virgin Mobile', 'Virgin Mobile'), 
    ('UNKNOWN', 'UNKNOWN'))
    provider = models.CharField(choices = p_choices, max_length=100)