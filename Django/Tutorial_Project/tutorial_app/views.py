from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    diction = {}
    return render(request, 'tutorial_app/index.html', context = diction)

def form(request):
    diction = {}
    return render(request, 'tutorial_app/form.html', context = diction)