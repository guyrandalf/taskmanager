from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    task_data = ("title", "desc", "is_completed")

admin.site.register(Task, TaskAdmin)