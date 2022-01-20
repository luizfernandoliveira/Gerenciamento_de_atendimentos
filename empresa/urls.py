from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', RedirectView.as_view(url='/empresa/home/')),
]
