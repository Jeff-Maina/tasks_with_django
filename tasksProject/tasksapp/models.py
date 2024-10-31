from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    deadline = models.DateTimeField()

    def __str__(self):
        return (f"{self.title},{self.description}")
