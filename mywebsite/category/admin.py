from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'type']
    prepopulated_fields = {'slug':('name',)}