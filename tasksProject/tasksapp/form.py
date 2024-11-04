from django import forms
from .models import Task

PRIORITY_CHOICES = [
    ("high", "High"),
    ("medium", "Medium"),
    ("low", "Low"),
]
STATUS_CHOICES = [
    ("todo", "TODO"),
    ("pending", "Pending"),
    ("completed", "Completed"),
    ("cancelled", "Cancelled"),
]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority',
                  'status', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'priority': forms.Select(choices=PRIORITY_CHOICES),
            'status': forms.Select(choices=STATUS_CHOICES),
        }

    def add_task(self):
        if self.is_valid():
            new_task = self.save()
            return new_task

