from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from datetime import datetime

from .models import *
from .forms import *
# Create your views h ere.

class OperadorPesadoView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "prf.change_editorbitacoras"
    model = OperadorPesado
    template_name = 'bita/operador_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class OperadorPesadoNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
    model = SolicitantesUtilitario
    template_name = 'bita/solicitantes_utilitario_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class SolicitantesUtilitarioNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
    model = VehiculoLigero
    template_name = 'bita/vehiculo_ligero_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoLigeroNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
    model = VehiculoPesado
    template_name = 'bita/vehiculo_pesado_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class VehiculoPesadoNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "change_editorbitacoras"
    model = MotivoIngresoUnidad
    template_name = 'bita/motivo_ingreso_unidad_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoIngresoUnidadNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
    model = DestinosClientes
    template_name = 'bita/destinos_clientes_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class DestinosClientesNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
    model = MotivoVisita
    template_name = 'bita/motivo_visita_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class MotivoVisitaNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_editorbitacoras"
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
    permission_required = "prf.change_editorbitacoras"
    model= MotivoVisita
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=MotivoVisitaForm
    success_url = reverse_lazy('bita:motivo_visita_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
class CargaUreaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "prf.change_vigilante"
    model = CargaDeUrea
    template_name = 'bita/carga_urea_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class CargaUreaNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_vigilante"
    model= CargaDeUrea
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=CargaDeUreaForm
    success_url = reverse_lazy('bita:carga_urea_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class CargaUreaEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "prf.change_vigilante"
    model= CargaDeUrea
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=CargaDeUreaForm
    success_url = reverse_lazy('bita:carga_urea_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
class TanquesDieselView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "prf.change_vigilante"
    model = TanquesDiesel
    template_name = 'bita/tanques_diesel_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class TanquesDieselNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_vigilante"
    model= TanquesDiesel
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=TanquesDieselForm
    success_url = reverse_lazy('bita:tanques_diesel_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class TanquesDieselEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "prf.change_vigilante"
    model= TanquesDiesel
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=TanquesDieselForm
    success_url = reverse_lazy('bita:tanques_diesel_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
class DescargaDeDieselView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "prf.change_vigilante"
    model = DescargaDeDiesel
    template_name = 'bita/descarga_diesel_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class DescargaDeDieselNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_vigilante"
    model= DescargaDeDiesel
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=DescargaDeDieselForm
    success_url = reverse_lazy('bita:descarga_diesel_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class DescargaDeDieselEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "prf.change_vigilante"
    model= DescargaDeDiesel
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=DescargaDeDieselForm
    success_url = reverse_lazy('bita:descarga_diesel_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
""
class CargaDeDieselView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "prf.change_vigilante"
    model = CargaDeDiesel
    template_name = 'bita/carga_diesel_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
class CargaDeDieselNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_vigilante"
    model= CargaDeDiesel
    template_name = 'bita/diesel_form.html'
    context_object_name='obj'
    form_class=CargaDeDieselForm
    success_url = reverse_lazy('bita:carga_diesel_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class CargaDeDieselEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "prf.change_vigilante"
    model= CargaDeDiesel
    template_name = 'bita/diesel_form.html'
    context_object_name='obj'
    form_class=CargaDeDieselForm
    success_url = reverse_lazy('bita:carga_diesel_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
"""Ingreso unidad (diferente a motivos"""
class IngresoUnidadPesadaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "prf.change_vigilante"
    model = IngresoUnidadPesada
    template_name = 'bita/ingreso_unidad_pesada_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_queryset(self):
        qs = IngresoUnidadPesada.objects.filter(estado=True).order_by('-id')[:100] | IngresoUnidadPesada.objects.filter(estado=False).order_by('-id')[:100]
        return qs
class IngresoUnidadPesadaExport(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "prf.change_vigilante"
    model = IngresoUnidadPesada
    template_name = 'bita/ingreso_pesada_export.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_queryset(self):
        qs = IngresoUnidadPesada.objects.filter(estado=True).order_by('-id')[:5000] | IngresoUnidadPesada.objects.filter(estado=False).order_by('-id')[:5000]
        return qs
class IngresoUnidadPesadaNew(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = "prf.change_vigilante"
    model= IngresoUnidadPesada
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=IngresoUnidadPesadaForm
    success_url = reverse_lazy('bita:ingreso_unidad_pesada_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
class IngresoUnidadPesadaEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = "prf.change_editorbitacoras"
    model= IngresoUnidadPesada
    template_name = 'bita/form_generico.html'
    context_object_name='obj'
    form_class=IngresoUnidadPesadaForm
    success_url = reverse_lazy('bita:ingreso_unidad_pesada_list')
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
""""""
@login_required(login_url="/login/")
@permission_required("prf.change_vigilante",login_url="/login/")
def salida_pesado(request, id):
    pede = IngresoUnidadPesada.objects.filter(pk=id).first()
    contexto={}
    """template_name="inv/pedidos_brinco.html"-"""
    if not pede:
        return redirect("bita:ingreso_unidad_pesada_list")
    if request.method=='GET':
        if pede.estado==True:
            pede.fsalida = datetime.now()
            pede.estado=False
            pede.save()
            return redirect("bita:ingreso_unidad_pesada_list")
        else:
            return HttpResponse("Ya se tiene un registro de salida. No se le puede volver a asignar hora de salida.")
    if request.method=='POST':
        if pede.estado==True:
            pede.fsalida = datetime.now()
            pede.estado=False
            pede.save()
            return redirect("bita:ingreso_unidad_pesada_list")
        else:
            return HttpResponse("Ya se tiene un registro de salida. No se le puede volver a asignar hora de salida.")
    return render(request,contexto)
""",template_name"""