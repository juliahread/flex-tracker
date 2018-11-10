from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('/home', view.home, name='home'),
=======
    path('', RedirectView.as_view(url='/accounts/login')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')), 
>>>>>>> origin/login
]
