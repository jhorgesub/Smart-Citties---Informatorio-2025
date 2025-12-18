from django.db import models
from django.utils import timezone

# Create your models here.



#Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=30,null=False)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    subtitulo = models.CharField(max_length=200, null=True, blank=True)
    pie_foto = models.CharField(max_length=100, blank=True, default='')
    fecha = models.DateTimeField(auto_now=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)

    def __str__ (self):
        return self.titulo


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/post_default.png')


    def delete(self, using = None, keep_parents = False):
        self.imagen.delete()
        super().delete(using=using, keep_parents=keep_parents)