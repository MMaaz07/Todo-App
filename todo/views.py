from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task,user=request.user)
    return redirect('home')

@login_required(login_url='login')
def mark_as_done(request, pk): 
    task=get_object_or_404(Task,pk=pk, user=request.user)
    task.is_completed=True
    task.save()
    return redirect('home')

@login_required(login_url='login')
def edit_task(request, pk):
    get_task=get_object_or_404(Task, pk=pk, user=request.user)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
    return render(request,'edit_task.html',context )


@login_required(login_url='login')
def delete_task(request,pk):
    task=get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('home')


@login_required(login_url='login')
def mark_as_undone(request, pk):
    task=get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed=False
    task.save()
    return redirect('home')