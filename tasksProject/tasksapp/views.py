from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .form import TaskForm, RegisterForm

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(
                username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error_message = None
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get(
                'next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            if User.objects.filter(username=username).exists():
                error_message = "Incorrect credentials. Please try again."
            else:
                error_message = "No account found with that username. Please register."

    return render(request, 'accounts/login.html', {'error': error_message})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')


@login_required
def home_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskapp/home.html', {'tasks': tasks})


@login_required
def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.add_task()
            return redirect("home")
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'taskapp/add_task.html', context)


@login_required
def deleteTask(request, id):

    task = get_object_or_404(Task, id=id)
    if task.user != request.user:
        return redirect("home")
    task.delete()
    return redirect("home")


@login_required
def updateTask(request, id):
    task = get_object_or_404(Task, id=id)

    if task.user != request.user:
        return redirect("home")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'taskapp/add_task.html', context)
