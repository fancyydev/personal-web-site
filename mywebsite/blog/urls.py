from django.urls import path
from .views import *
app_name = 'blog' 
urlpatterns = [
    path('writenposts/', list_written_posts, name='writen_posts'),
    path('recomendationposts/', list_recomendation_posts, name='recomendation_posts'),
    path('detail/<str:post_slug>', detail_post, name='post_detail'),
]
