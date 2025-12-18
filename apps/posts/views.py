from .models import Post, Categoria
from apps.comentario.models import Comentario
from .forms import PostForm, NuevaCategoriaForm
from django.views.generic import ListView, DetailView,  DeleteView, UpdateView
from apps.comentario.forms import ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        orden = self.request.GET.get('orden')
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha')
        elif orden == 'alfabetico':
            queryset = queryset.order_by('titulo')
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'pk'
    queryset = Post.objects.all()

#Post creación
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
            messages.success(self.request, 'Post creado con éxito!')
            return reverse_lazy('apps.posts:posts')


#Post modificación
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
            messages.success(self.request, 'Post modificado con éxito!')
            return reverse_lazy('apps.posts:post_individual', kwargs={'pk': self.object.pk})


#Posts borrar
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_eliminar.html'

    def get_success_url(self):
        messages.success(self.request, '¡Borrado con éxito!')
        return reverse_lazy('apps.posts:posts')

class PostPorCategoriaView(ListView):
    model = Post
    template_name = 'posts/post_por_categoria.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(categoria_id=self.kwargs['pk'])
    
#Categorías
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'posts/crear_categoria.html'

    def get_success_url(self):
        messages.success(self.request, '¡Categoría creada con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.posts:posts')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'posts/categoria_lista.html'
    context_object_name = 'categorias'

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'posts/categoria_eliminar.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Categoría eliminada')
        return reverse_lazy('apps.posts:categoria_lista')