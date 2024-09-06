from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class Todo_Admin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date']
