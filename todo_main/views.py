from django.http import HttpResponse
from django.shortcuts import render,redirect
from todo.models import Task
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')
def home(request):
    tasks=Task.objects.filter(is_completed=False, user=request.user).order_by('updated_at')

    completed_tasks=Task.objects.filter(is_completed=True, user=request.user)
    print(completed_tasks)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    } 
    return render(request, 'home-todo.html',context)


def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    return render(request, 'login.html')


def register_user(request):
    errors={}
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm-password')


        if confirm_password!=password:
            errors['confirm_password']="Passwords do not match"

        if User.objects.filter(username=username).exists():
            errors['username'] = "Username already exists, click on Login"
        
        if not errors:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    
    return render(request, 'register.html',{'errors':errors})

def logout_view(request):
    logout(request)
    return redirect('login')
