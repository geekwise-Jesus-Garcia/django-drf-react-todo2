from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admimn.ModelsAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)