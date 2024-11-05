
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff',
                    'is_superuser')  # Customize as needed
    search_fields = ('email', 'username')  # Add search capability
    ordering = ('email',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status',
                    'deadline')  # Add fields to display
    list_filter = ('status', 'priority')  # Add filters for easier navigation
    # Enable searching by title and description
    search_fields = ('title', 'description')
    ordering = ('-deadline',)  # Order by deadline, latest first

    # You can define custom actions here if needed
    actions = ['mark_as_done', 'mark_as_in_progress',
               'mark_as_cancelled', 'approve']

    def mark_as_done(self, request, queryset):
        queryset.update(status='Done')  # Update status to Done
        self.message_user(request, "Selected tasks have been marked as Done.")

    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='In-progress')  # Update status to In-progress
        self.message_user(
            request, "Selected tasks have been marked as In-progress.")

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='Cancelled')  # Update status to Cancelled
        self.message_user(
            request, "Selected tasks have been marked as Cancelled.")

    def approve(self, request, queryset):
        queryset.update(status='Cancelled')  # Update status to Cancelled
        self.message_user(
            request, "Selected tasks have been marked as Cancelled.")

    mark_as_done.short_description = "Mark selected tasks as Done"
    mark_as_in_progress.short_description = "Mark selected tasks as In-progress"
    mark_as_cancelled.short_description = "Mark selected tasks as Cancelled"


# Register the TaskAdmin with the Task model
admin.site.register(Task, TaskAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
