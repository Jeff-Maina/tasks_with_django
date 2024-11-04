from django import forms


from .models import Task


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    priority = forms.CharField(max_length=100)
    status = forms.CharField(max_length=100)
    deadline = forms.DateTimeField()

    def add_task(self):
        new_task = Task(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            priority=self.cleaned_data['priority'],
            status=self.cleaned_data['status'],
            deadline=self.cleaned_data['deadline']
        )
        new_task.save()
