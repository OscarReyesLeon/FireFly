from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views h ere.

class OperadorPesadoView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.view_operadorpesado"
    model = OperadorPesado
    template_name = 'bita/operador_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class OperadorPesadoNew(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.add_operadorpesado"
    model= OperadorPesado
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=OperadorPesadoForm
    success_url = reverse_lazy('bita:operador_pesado_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class OperadorPesadoEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "bita.change_operadorpesado"
    model= OperadorPesado
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=OperadorPesadoForm
    success_url = reverse_lazy('bita:operador_pesado_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.umc = self.request.user.username
        return super().form_valid(form)

class SolicitantesUtilitarioView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.view_solicitantesutilitario"
    model = SolicitantesUtilitario
    template_name = 'bita/solicitantes_utilitario_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class SolicitantesUtilitarioNew(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.add_solicitantesutilitario"
    model= SolicitantesUtilitario
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=SolicitantesUtilitarioForm
    success_url = reverse_lazy('bita:solicitante_utilitario_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class SolicitantesUtilitarioEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "bita.change_solicitantesutilitario"
    model= SolicitantesUtilitario
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=SolicitantesUtilitarioForm
    success_url = reverse_lazy('bita:solicitante_utilitario_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class VehiculoLigeroView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.view_solicitantesutilitario"
    model = VehiculoLigero
    template_name = 'bita/vehiculo_ligero_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoLigeroNew(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.add_vehiculoligero"
    model= VehiculoLigero
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=VehiculoLigeroForm
    success_url = reverse_lazy('bita:vehiculo_ligero_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class VehiculoLigeroEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "bita.change_vehiculoligero"
    model= VehiculoLigero
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=VehiculoLigeroForm
    success_url = reverse_lazy('bita:vehiculo_ligero_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
class VehiculoPesadoView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'bita.view_vehiculopesado'
    model = VehiculoPesado
    template_name = 'bita/vehiculo_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoPesadoNew(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.add_vehiculopesado"
    model= VehiculoPesado
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=VehiculoPesadoForm
    success_url = reverse_lazy('bita:vehiculo_pesado_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class VehiculoPesadoEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'bita.change_vehiculopesado'
    model= VehiculoPesado
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=VehiculoPesadoForm
    success_url = reverse_lazy('bita:vehiculo_pesado_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
class MotivoIngresoUnidadView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'bita.view_motivoingresounidad'
    model = MotivoIngresoUnidad
    template_name = 'bita/motivo_ingreso_unidad_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoIngresoUnidadNew(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.add_motivoingresounidad"
    model= MotivoIngresoUnidad
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=MotivoIngresoUnidadForm
    success_url = reverse_lazy('bita:motivo_ingreso_unidad_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class MotivoIngresoUnidadEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'bita.change_motivoingresounidad'
    model= MotivoIngresoUnidad
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=MotivoIngresoUnidadForm
    success_url = reverse_lazy('bita:motivo_ingreso_unidad_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class DestinosClientesView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.view_destinosclientes"
    model = DestinosClientes
    template_name = 'bita/destinos_clientes_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class DestinosClientesNew(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.add_destinosclientes"
    model= DestinosClientes
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=DestinosClientesForm
    success_url = reverse_lazy('bita:destinos_clientes_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class DestinosClientesEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'bita.change_destinosclientes'
    model= DestinosClientes
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=DestinosClientesForm
    success_url = reverse_lazy('bita:destinos_clientes_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class MotivoVisitaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'bita.view_motivovisita'
    model = MotivoVisita
    template_name = 'bita/motivo_visita_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoVisitaNew(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "bita.add_motivovisita"
    model= MotivoVisita
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=MotivoVisitaForm
    success_url = reverse_lazy('bita:motivo_visita_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class MotivoVisitaEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'bita.change_motivovisita'
    model= MotivoVisita
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=MotivoVisitaForm
    success_url = reverse_lazy('bita:motivo_visita_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
