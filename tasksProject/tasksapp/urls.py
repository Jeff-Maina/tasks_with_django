from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name='home'),
    path("add-task/", views.add_task_view, name="add-task")
]
