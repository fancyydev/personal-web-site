from django.urls import path
from .views import *
app_name = 'blog' 
urlpatterns = [
    path('', render_posts, name='post'),
    path('detail/<str:post_slug>', detail_post, name='post_detail'),
    path('detail/art/<int:post_id>', detail_post, name='post')
]
