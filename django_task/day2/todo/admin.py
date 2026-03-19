from django.contrib import admin

from todo.models import Todos


# Register your models here.

@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    ...