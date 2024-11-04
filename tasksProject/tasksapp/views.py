from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Task

from .form import TaskForm

# Create your views here.


def home_view(request):
    tasks = Task.objects.all()
    return render(request, 'taskapp/home.html', {'tasks': tasks})


def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.add_task()
            return redirect("home")
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'taskapp/add_task.html', context)


def deleteTask(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("home")


def updateTask(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'taskapp/add_task.html', context)

