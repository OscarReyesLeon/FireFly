from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from bases.views import SinPrivilegios
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views h ere.

class OperadorPesadoView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required = "bita.view_operadorpesado"
    model = OperadorPesado
    template_name = 'bita/operador_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class OperadorPesadoNew(SuccessMessageMixin, SinPrivilegios, generic.ListView):
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
class OperadorPesadoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
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

class SolicitantesUtilitarioView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required = "bita.view_solicitantesutilitario"
    model = SolicitantesUtilitario
    template_name = 'bita/solicitantes_utilitario_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class SolicitantesUtilitarioNew(SuccessMessageMixin, SinPrivilegios, generic.ListView):
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
class SolicitantesUtilitarioEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
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

class VehiculoLigeroView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required = "bita.view_solicitantesutilitario"
    model = VehiculoLigero
    template_name = 'bita/vehiculo_ligero_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoLigeroNew(SuccessMessageMixin, SinPrivilegios, generic.ListView):
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
class VehiculoLigeroEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
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
class VehiculoPesadoView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required = 'bita.view_vehiculopesado'
    model = VehiculoPesado
    template_name = 'bita/vehiculo_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoPesadoNew(SuccessMessageMixin, SinPrivilegios, generic.ListView):
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
class VehiculoPesadoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
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
class MotivoIngresoUnidadView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required = 'bita.view_motivoingresounidad'
    model = MotivoIngresoUnidad
    template_name = 'bita/motivo_ingreso_unidad_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoIngresoUnidadNew(SuccessMessageMixin, SinPrivilegios, generic.ListView):
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
class MotivoIngresoUnidadEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
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

class DestinosClientesView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required = "bita.view_destinosclientes"
    model = DestinosClientes
    template_name = 'bita/destinos_clientes_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class DestinosClientesNew(SuccessMessageMixin, SinPrivilegios, generic.ListView):
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
class DestinosClientesEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
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

class MotivoVisitaView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    permission_required = 'bita.view_motivovisita'
    model = MotivoVisita
    template_name = 'bita/motivo_visita_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoVisitaNew(SuccessMessageMixin, SinPrivilegios, generic.ListView):
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
class MotivoVisitaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
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
