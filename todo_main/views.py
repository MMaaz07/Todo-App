from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home-todo.html')

def empty(request):
    return HttpResponse('<h1>Hola Peeps</h1>')