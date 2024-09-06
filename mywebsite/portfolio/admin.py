from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Project)
class ProjectRegister(admin.ModelAdmin):
    list_display = ['title', 'url']
    search_fields = ['title', 'description']
    
    