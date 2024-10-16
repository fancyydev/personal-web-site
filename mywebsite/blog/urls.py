from django.urls import path
from .views import *
app_name = 'blog' 
urlpatterns = [
    path('writenposts/', list_written_posts, name='writen_posts'),
    path('recomendationposts/', list_recommendation_posts, name='recomendation_posts'),
    path('artposts/', list_art_posts, name='art_posts'),
    path('detail/<str:post_slug>', detail_post, name='post_detail'),
    path('artdetail/<str:post_slug>', detail_art_post, name='art_detail'),
]
