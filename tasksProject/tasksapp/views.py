from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

from .form import AddTaskForm

# Create your views here.


def home_view(request):
    tasks = Task.objects.all()
    return render(request, 'taskapp/home.html', {'tasks': tasks})


def add_task_view(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.add_task()
            return redirect("home")
    else:
        form = AddTaskForm()
    context = {'form': form}
    return render(request, 'taskapp/add_task.html', context)
