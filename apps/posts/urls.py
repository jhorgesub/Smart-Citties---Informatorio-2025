from django.urls import path
from .views import *

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),#Ver todos los posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_individual"),#Ver un post individual
    path('posts/crear/', PostCreateView.as_view(), name='posteo'),#Crear un post
    path('posts/<int:pk>/actualizar/', PostUpdateView.as_view(), name='post_form'),#Modificar un post
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_eliminar'),#Eliminar un post
    path('categoria/', CategoriaListView.as_view(), name='categoria_lista'),
    path('categoria/<int:pk>/posts/', PostPorCategoriaView.as_view(), name='post_por_categoria'),
    path('posts/categoria', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_eliminar'),
]
