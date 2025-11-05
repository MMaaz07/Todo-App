from django.contrib import admin
from .models import Task
# Register your models here.
class taskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','created_at')

admin.site.register(Task, taskAdmin)