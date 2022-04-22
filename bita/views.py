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

class SolicitantesUtilitarioView(LoginRequiredMixin, generic.ListView):
    model = SolicitantesUtilitario
    template_name = 'bita/operador_ligero_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class SolicitantesUtilitarioNew(LoginRequiredMixin, generic.CreateView):
    model= SolicitantesUtilitario
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=SolicitantesUtilitarioForm
    success_url = reverse_lazy('bita:operador_ligero_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VehiculoLigeroView(LoginRequiredMixin, generic.ListView):
    model = VehiculoLigero
    template_name = 'bita/vehiculo_ligero_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoLigeroNew(LoginRequiredMixin, generic.CreateView):
    model= VehiculoLigero
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=VehiculoLigeroForm
    success_url = reverse_lazy('bita:vehiculo_ligero_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class VehiculoPesadoView(LoginRequiredMixin, generic.ListView):
    model = VehiculoPesado
    template_name = 'bita/vehiculo_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoPesadoNew(LoginRequiredMixin, generic.CreateView):
    model= VehiculoPesado
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=VehiculoPesadoForm
    success_url = reverse_lazy('bita:vehiculo_pesado_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class MotivoIngresoUnidadView(LoginRequiredMixin, generic.ListView):
    model = MotivoIngresoUnidad
    template_name = 'bita/motivo_ingreso_unidad_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoIngresoUnidadNew(LoginRequiredMixin, generic.CreateView):
    model= MotivoIngresoUnidad
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=MotivoIngresoUnidadForm
    success_url = reverse_lazy('bita:motivo_ingreso_unidad_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class DestinosClientesView(LoginRequiredMixin, generic.ListView):
    model = DestinosClientes
    template_name = 'bita/destinos_clientes_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class DestinosClientesNew(LoginRequiredMixin, generic.CreateView):
    model= DestinosClientes
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=DestinosClientesForm
    success_url = reverse_lazy('bita:destinos_cleintes_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MotivoVisitaView(LoginRequiredMixin, generic.ListView):
    model = MotivoVisita
    template_name = 'bita/motivo_visita_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoVisitaNew(LoginRequiredMixin, generic.CreateView):
    model= MotivoVisita
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=MotivoVisitaForm
    success_url = reverse_lazy('bita:motivo_visita_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
