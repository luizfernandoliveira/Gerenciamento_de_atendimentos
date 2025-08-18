from django.shortcuts import render


def home(request):
    status = request.GET.get('status')
    return render(request, 'home.html', {'status': status})


def dashboard(request):
    return render(request, 'dashboard.html')
