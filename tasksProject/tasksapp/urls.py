from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name='home'),
    path("add-task/", views.add_task_view, name="add-task"),
    path("delete-task/<int:id>/", views.deleteTask, name='delete-task'),
    path("update-task/<int:id>/", views.updateTask, name='update-task'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
