from django import forms


from .models import Task

PRIORITY_CHOICES = {'high': "High", "medium": "Medium", "low": "Low", }
STATUS_CHOICES = {'todo': "TODO",
                  "pending": "Pending", "completed": "Completed", "cancelled": "Cancelled"}


class AddTaskForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Task Status')
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'date'}))

    def add_task(self):
        new_task = Task(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            priority=self.cleaned_data['priority'],
            status=self.cleaned_data['status'],
            deadline=self.cleaned_data['deadline']
        )
        new_task.save()
