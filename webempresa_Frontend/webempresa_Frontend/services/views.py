from django.shortcuts import render
from .models import Service, Post

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def blog(request):
    posts = Post.objects.all() # Obtenemos todos los posts
    return render(request, 'blog.html', {'posts': posts}) # Los pasamos a la plantilla