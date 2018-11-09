from django.db import models
from django import forms

# Create your models here.

class LogInForm(forms.Form):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    email = models.CharField(max_length=100, help_text='Enter your email')
    password = models.CharField(max_length=100, help_text='Enter your password')

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.email
    
    def is_valid(self):
        return False