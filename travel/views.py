from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# @login_required
def home(request):
    name = 'Andrey'
    return render(request, 'home.html', {'name': name})

def about(request):
    name = 'About us'
    return render(request, 'about.html', {'name': name})
