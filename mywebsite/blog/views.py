from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def render_posts(request):
    
    posts = Post.objects.filter(type='escritos')
    return render(request, 'posts.html', {'posts': posts})

def list_written_posts(request):
    written = True
    
    post_list = Post.objects.filter(type='escritos')
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)    
    
    return render(request, 'posts.html', {'posts': posts, 'written': written})

def list_recommendation_posts(request):
    recommendation = True
    
    post_list = Post.objects.filter(type='recomendaciones')
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    
    return render(request, 'posts.html', {'posts': posts, 'recommendation':recommendation})

def list_art_posts(request):
    art = True
    
    post_list = Art.objects.all()
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
        
    return render(request, 'posts.html', {'posts': posts, 'art':art})
    

def detail_post(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug)
    
    if post.type== 'escritos':
        redirect_url = 'blog:writen_posts'
    elif post.type== 'recomendaciones':
        redirect_url = 'blog:recomendation_posts'
  
    return render(request, 'post_detail.html', {
        'post': post,
        'redirect_url': redirect_url  # Pasamos la URL a la plantilla
    })

def detail_art_post(request, post_slug):
    
    post = get_object_or_404(Art, slug = post_slug)
    
    redirect_url = 'blog:art_posts'
  
    return render(request, 'art_detail.html', {
        'post': post,
        'redirect_url': redirect_url  # Pasamos la URL a la plantilla
    })
  