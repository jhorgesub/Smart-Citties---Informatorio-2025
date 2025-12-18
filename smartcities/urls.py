from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import index, acerca_de
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('acerca-de/', acerca_de, name='acerca_de'),
    path('', index, name='index'),
    path('', include('apps.posts.urls')),
    path('', include('apps.contacto.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('apps.comentario.urls')),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
