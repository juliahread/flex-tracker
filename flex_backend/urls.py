from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login')),
    path('home/', views.home, name='home'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('locations/', views.locations, name='locations'),
    path('settings/', views.settings, name='settings'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
