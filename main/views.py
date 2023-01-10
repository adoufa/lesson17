from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Главная страница', 'task': tasks})


def about(request):
    return render(request, 'main/about.html')
