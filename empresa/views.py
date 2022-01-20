from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from usuarios.models import Usuario
from usuarios.views import login

# Create your views here.


def home(request):
    status = request.GET.get('status')
    return render(request, 'home.html', {'status': status})

