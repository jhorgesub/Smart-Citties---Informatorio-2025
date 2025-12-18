from django.shortcuts import render
from apps.posts.models import Post 

def index(request):
    
    try:
        ultimos_posts = Post.objects.filter(activo=True).order_by('-fecha')[:3]
    except Exception as e:
       
        print(f"Error al cargar los posts: {e}")
        ultimos_posts = []

    contexto = {
        'ultimos_posts': ultimos_posts
    }
    
    return render(request, 'index.html', contexto)

def acerca_de(request):
    return render(request, 'acerca_de.html')