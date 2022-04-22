from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views h ere.

class OperadorPesadoView(LoginRequiredMixin, generic.ListView):
    model = OperadorPesado
    template_name = 'bita/operador_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class SolicitantesUtilitarioView(LoginRequiredMixin, generic.ListView):
    model = SolicitantesUtilitario
    template_name = 'bita/operador_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class OperadorPesadoNew(LoginRequiredMixin, generic.CreateView):
    model= OperadorPesado
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=OperadorPesadoForm
    success_url = reverse_lazy('bita:operador_pesado_list')
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)