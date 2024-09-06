from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    list_filter = ['type']
    search_fields = ['title', 'description', 'content', 'type']
    prepopulated_fields = {'slug':('title',)}
    
@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}