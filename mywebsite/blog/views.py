from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def render_posts(request):
    posts = Post.objects.filter(type='escritos')
    return render(request, 'posts.html', {'posts': posts})

def list_written_posts(request):
    posts = Post.objects.filter(type='escritos')
    return render(request, 'posts.html', {'posts': posts})

def list_recomendation_posts(request):
    posts = Post.objects.filter(type='recomendaciones')
    return render(request, 'posts.html', {'posts': posts})

def list_art_posts(request):
    return

def detail_post(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug)
    return render(request, 'post_detail.html', {'post': post})

def detail_art_post(request, post_id):
    return