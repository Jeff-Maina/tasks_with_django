# Generated by Django 5.1.2 on 2024-11-05 09:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasksapp", "0003_rename_user_task_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="user_id",
            new_name="user",
        ),
    ]
