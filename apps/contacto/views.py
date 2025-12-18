from .forms import ContactoForm

from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ContactoUsuario(CreateView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('index')
    

    def form_valid(self, form):
        messages.success(self.request, 'Mensaje enviado!')
        return super().form_valid(form)
    

# Create your views here.
