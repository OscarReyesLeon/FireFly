from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime

from cmp.forms import ComprasEncForm
from .models import Autoriza, Equipo, Pedido,Proceso, Categoria, UnidadMedida, \
    Producto, Pedido, Banco, Puesto, Empleado, Computadora, Herramienta, Empresa, \
    Genero, Estudios, Ecivil, Departamento, Puesto, Parentescocontacto, Artciulosestandarizados, Nombresrelacion, normalize
from .forms import EquipoForm, ProcesoForm, CategoriaForm, PedidoSecondForm, \
    UMForm, ProductoForm, PedidoForm, AutorizaForm, BancoForm, \
    EmpleadoForm, ComputadoraForm, HerramientaForm, \
    EmpresaForm, GeneroForm, EstudiosForm, PedidoComprasForm,\
    EcivilForm, DepartamentoForm, PuestoForm, ParentescocontactoForm, ArtciulosestandarizadosForm, NombresrelacionForm
from cmp.models import ComprasDet, ComprasEnc
from django.db.models import OuterRef, Exists
from inv.serializers import PedidoSerializer
from bases.views import SinPrivilegios



class EquipoView(SinPrivilegios,generic.ListView):
    permission_required = "inv.view_equipo"
    model = Equipo
    template_name = "inv/equipo_list.html"
    context_object_name = "obj"
    


class EquipoNew(SuccessMessageMixin,SinPrivilegios,\
    generic.CreateView):
    permission_required="inv.add_equipo"
    model=Equipo
    template_name="inv/equipo_form.html"
    context_object_name = "obj"
    form_class=EquipoForm
    success_url=reverse_lazy("inv:equipo_list")
    success_message="Equipo Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EquipoEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    permission_required="inv.change_equipo"
    model=Equipo
    template_name="inv/equipo_form.html"
    context_object_name = "obj"
    form_class=EquipoForm
    success_url=reverse_lazy("inv:equipo_list")
    success_message="Equipo Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class EquipoDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    permission_required="inv.delete_equipo"
    model=Equipo
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:equipo_list")
    success_message="Equipo Eliminada Satisfactoriamente"


class ProcesoView(SinPrivilegios, \
    generic.ListView):
    permission_required = "inv.view_proceso"
    model = Proceso
    template_name = "inv/proceso_list.html"
    context_object_name = "obj"


class ProcesoNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    model=Proceso
    template_name="inv/proceso_form.html"
    context_object_name = "obj"
    form_class=ProcesoForm
    success_url=reverse_lazy("inv:proceso_list")
    success_message="Proceso Creada Satisfactoriamente"
    permission_required="inv.add_proceso"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProcesoEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    model=Proceso
    template_name="inv/proceso_form.html"
    context_object_name = "obj"
    form_class=ProcesoForm
    success_url=reverse_lazy("inv:proceso_list")
    success_message="Proceso Actualizada Satisfactoriamente"
    permission_required="inv.change_subcatetoria"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ProcesoDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    model=Proceso
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:proceso_list")
    success_message="Proceso Eliminada"
    permission_required="inv.delete_proceso"

class AutorizaView(SinPrivilegios, \
    generic.ListView):
    permission_required = "inv.view_autoriza"
    model = Autoriza
    template_name = "inv/autoriza_list.html"
    context_object_name = "obj"
    


class AutorizaNew(SuccessMessageMixin,SinPrivilegios,\
    generic.CreateView):
    permission_required="inv.add_autoriza"
    model=Autoriza
    template_name="inv/autoriza_form.html"
    context_object_name = "obj"
    form_class=AutorizaForm
    success_url=reverse_lazy("inv:autoriza_list")
    success_message="Autorizante registrado"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class AutorizaEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    permission_required="inv.change_autoriza"
    model=Autoriza
    template_name="inv/autoriza_form.html"
    context_object_name = "obj"
    form_class=AutorizaForm
    success_url=reverse_lazy("inv:autoriza_list")
    success_message="Autoriza Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class AutorizaDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    permission_required="inv.delete_autoriza"
    model=Autoriza
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:autoriza_list")
    success_message="Autoriza Eliminada Satisfactoriamente"


class CategoriaView(SinPrivilegios,\
     generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"


class CategoriaNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("inv:categoria_list")
    success_message="Categoria Creada"
    permission_required="inv.add_categoria"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("inv:categoria_list")
    success_message="Categoria Editada"
    permission_required="inv.change_categoria"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_categoria', login_url='bases:sin_privilegios')
def categoria_inactivar(request, id):
    categoria = Categoria.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"


    if not categoria:
        return redirect("inv:categoria_list")
    
    if request.method=='GET':
        contexto={'obj':categoria}
    
    if request.method=='POST':
        categoria.estado=False
        categoria.save()
        messages.success(request, 'Categoria Inactivada')
        return redirect("inv:categoria_list")

    return render(request,template_name,contexto)


class UMView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    permission_required="inv.view_unidadmedida"


class UMNew(SuccessMessageMixin,SinPrivilegios,generic.CreateView):
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inv:um_list")
    success_message="Unidad Medida Creada"
    permission_required="inv.add_unidadmedida"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UMEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inv:um_list")
    success_message="Unidad Medida Editada"
    permission_required="inv.change_unidadmedida"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("inv.change_unidadmedida",login_url="/login/")
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not um:
        return redirect("inv:um_list")
    
    if request.method=='GET':
        contexto={'obj':um}
    
    if request.method=='POST':
        um.estado=False
        um.save()
        return redirect("inv:um_list")

    return render(request,template_name,contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/pedido_list_inverso.html"
    context_object_name = "obj"
    permission_required="inv.view_producto"


class ProductoNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    success_message="Producto Creado"
    permission_required="inv.add_producto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["equipos"] = Equipo.objects.all()
        context["procesos"] = Proceso.objects.all()
        return context



class ProductoEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    success_message="Producto Editado"
    permission_required="inv.change_producto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(ProductoEdit, self).get_context_data(**kwargs)
        context["equipos"] = Equipo.objects.all()
        context["procesos"] = Proceso.objects.all()
        context["obj"] = Producto.objects.filter(pk=pk).first()

        return context

@login_required(login_url="/login/")
@permission_required("inv.change_producto",login_url="/login/")
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")
    
    if request.method=='GET':
        contexto={'obj':prod}
    
    if request.method=='POST':
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")

    return render(request,template_name,contexto)



class PedidoView(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_export.html"
    context_object_name = "obj"
    permission_required="inv.view_pedido"
    def get_queryset(self):
        qs = Pedido.objects.order_by('-id')[:4000]
        return qs

class PedidoExport(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_export.html"
    context_object_name = "obj"
    permission_required="inv.view_pedido"

    def obtener_informacion_reporte(self):
        fecha_inicial = self.request.GET.get('fecha_inicial', None)
        fecha_final = self.request.GET.get('fecha_final', None)
        estado = self.request.GET.get('estado', None)
        estandarizado = self.request.GET.get('estandarizado', None)
        pedido = Pedido.objects.all().annotate(
            estandarizado=Exists(Artciulosestandarizados.objects.filter(descripcion__icontains=OuterRef('articulo')))
        )
        if fecha_inicial: pedido = pedido.filter(fc__gte=fecha_inicial)
        if fecha_final: pedido = pedido.filter(fc__lte=fecha_final)
        if estado: pedido = pedido.filter(indentificador_estado__in=estado.split(",",1))
        if estandarizado and estandarizado in ["0", "1"]:
            pedido = pedido.filter(estandarizado=bool(int(estandarizado)))
        return pedido
    
    def obtener_archivo_xlsx(self, pedido):
        import pandas as pd
        from io import BytesIO
        with BytesIO() as b:
            data = pd.DataFrame(
                data=PedidoSerializer(pedido, many=True).data,
            )
            data.columns = PedidoSerializer.Meta.nombre_columnas
            with pd.ExcelWriter(b) as writer:
                data.to_excel(writer, sheet_name="Data", index=False)
            hoy = datetime.now()
            filename = "reporte_pedidos-{}.xlsx".format(hoy.strftime("%d-%m-%Y"))
            res = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            res['Content-Disposition'] = f'attachment; filename={filename}'
            return res

    def get(self, request, *args, **kwargs):
        reporte = request.GET.get('reporte', None)
        if request.is_ajax() or reporte:
            pedido = self.obtener_informacion_reporte()
            return self.obtener_archivo_xlsx(pedido)
        return super().get(request, *args, **kwargs)
        
    def get_queryset(self):
        qs = Pedido.objects.order_by('-id')[:40000]
        return qs


class PedidoViewF(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f.html"
    context_object_name = "obj"
    permission_required="inv.view_pedido"

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(uc=user).exclude(indentificador_estado=5).order_by('-id')[:100]
        return qs

class PedidoViewH(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_h.html"
    context_object_name = "obj"
    permission_required="inv.view_pedido"

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(uc=user).order_by('-id')[:500]
        return qs

class PedidoViewALS(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_als.html"
    context_object_name = "obj"
    permission_required="inv.change_pedido"

    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=1).order_by('-id')[:200] | Pedido.objects.filter(indentificador_estado=2).order_by('-id')[:100] | Pedido.objects.filter(indentificador_estado=3).order_by('-id')[:300] | Pedido.objects.filter(indentificador_estado=4).order_by('-id')[:100] | Pedido.objects.filter(indentificador_estado=6).order_by('-id')[:100]
        return qs

class PedidoViewGLS(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_gls.html"
    context_object_name = "obj"
    permission_required="prf.view_autorizantegls"

    def get_queryset(self):
        qs = Pedido.objects.filter(autpor=2).filter(indentificador_estado=1).order_by('-id')[:500]
        return qs
class PedidoViewGLSH(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_glsh.html"
    context_object_name = "obj"
    permission_required="prf.view_autorizantegls"

    def get_queryset(self):
        qs = Pedido.objects.filter(autpor=2).filter(indentificador_estado=2).order_by('-id')[:500] | Pedido.objects.filter(autpor=2).filter(indentificador_estado=3).order_by('-id')[:500] |  Pedido.objects.filter(autpor=2).filter(indentificador_estado=4).order_by('-id')[:500]
        return qs

class PedidoViewMLS(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_mls.html"
    context_object_name = "obj"
    permission_required="prf.view_autorizantemls"

    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=1).filter(autpor=3).order_by('-id')[:500] | Pedido.objects.filter(indentificador_estado=2).filter(autpor=3).order_by('-id')[:100] | Pedido.objects.filter(indentificador_estado=3).filter(autpor=3).order_by('-id')[:100] | Pedido.objects.filter(indentificador_estado=4).filter(autpor=3).order_by('-id')[:100] | Pedido.objects.filter(indentificador_estado=5).filter(autpor=3).order_by('-id')[:100]
        return qs
class PedidoViewOficinaCot(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f2.html"
    context_object_name = "obj"
    permission_required="prf.change_comprasoficinas"
    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=1).filter(autpor=1).order_by('-id')[:200]
        return qs
class PedidoViewALRCot(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f2.html"
    context_object_name = "obj"
    permission_required="prf.change_comprasalr"
    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=1).filter(autpor=3).order_by('-id')[:200]
        return qs
class PedidoViewPlantaCot(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f2.html"
    context_object_name = "obj"
    permission_required="prf.change_comprasplanta"

    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=1).filter(autpor=2).order_by('-id')[:200]
        return qs

class PedidoViewF3(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f3.html"
    context_object_name = "obj"
    permission_required="inv.change_change_pedido"

    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=3).order_by('-id')[:200]
        return qs

class PedidoViewF4o(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f4.html"
    context_object_name = "obj"
    permission_required="prf.change_almacenistaoficina"

    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=4).exclude(autpor=2).order_by('-id')[:200]
        return qs
class PedidoViewF4p(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f4.html"
    context_object_name = "obj"
    permission_required="prf.change_almacenistaplanta"

    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=4).filter(autpor=2).order_by('-id')[:200]
        return qs

class PedidoViewF5(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f5.html"
    context_object_name = "obj"
    permission_required="inv.change_pedido"

    def get_queryset(self):
        qs = Pedido.objects.filter(status='Recibido').order_by('-id')[:200] | Pedido.objects.filter(status="Directo").order_by('-id')[:200] | Pedido.objects.filter(status="Stock").order_by('-id')[:200]
        return qs
class PedidoViewF6(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_f6.html"
    context_object_name = "obj"
    permission_required="prf.change_almacenista"

    def get_queryset(self):
        qs = Pedido.objects.filter(indentificador_estado=6).order_by('-id')[:200]
        return qs
class PedidoViewAll(SinPrivilegios, generic.ListView):
    model = Pedido
    template_name = "inv/pedido_list_inverso.html"
    context_object_name = "obj"
    permission_required="inv.view_pedido"

class PedidoNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Pedido
    template_name="inv/pedido_form.html"
    context_object_name = 'obj'
    form_class=PedidoForm
    success_url= reverse_lazy("inv:pedido_list_f")
    success_message="Pedido Solicitado"
    permission_required="inv.add_pedido"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(PedidoNew, self).get_context_data(**kwargs)
        context["equipos"] = Equipo.objects.all()
        context["procesos"] = Proceso.objects.all()
        context["articulos"] = Artciulosestandarizados.objects.all() 
        return context
"""revisar equipo y proceso"""


class PedidoSecondNew(SuccessMessageMixin, SinPrivilegios,
                generic.CreateView):
    model = Pedido
    template_name = "inv/form_generico.html"
    context_object_name = 'obj'
    form_class = PedidoSecondForm
    success_url = reverse_lazy("inv:pedido_list_f")
    success_message = "Pedido Solicitado"
    permission_required = "inv.add_pedido"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PedidoSecondNew, self).get_context_data(**kwargs)
        return context


class PedidoEditO(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Pedido
    template_name="inv/pedido_form_compraso.html"
    context_object_name = 'obj'
    form_class=PedidoComprasForm
    success_url= reverse_lazy("inv:cotiza_oficina")
    permission_required="prf.change_comprasoficinas"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(PedidoEditO, self).get_context_data(**kwargs)
        context["equipos"] = Equipo.objects.all()
        context["procesos"] = Proceso.objects.all()
        context["obj"] = Pedido.objects.filter(pk=pk).first()

        return context
class PedidoEditP(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Pedido
    template_name="inv/pedido_form_comprasp.html"
    context_object_name = 'obj'
    form_class=PedidoComprasForm
    success_url= reverse_lazy("inv:cotiza_planta")
    permission_required="prf.change_comprasplanta"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(PedidoEditP, self).get_context_data(**kwargs)
        context["equipos"] = Equipo.objects.all()
        context["procesos"] = Proceso.objects.all()
        context["obj"] = Pedido.objects.filter(pk=pk).first()

        return context


@login_required(login_url="/login/")
@permission_required("prf.change_autorizador",login_url="/login/")
def pedido_aprobado_als(request, id):
    pedi = Pedido.objects.filter(pk=id).first()

    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list_als")
    
    if request.method=='GET':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_aprobado = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='Si'
            pedi.status='Cotizando'
            pedi.indentificador_estado='2'
            pedi.save()
            return redirect("inv:pedido_list_als")
        else:
            return HttpResponse("el pedido no esta en condición de ser re-autorizado")
    if request.method=='POST':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_aprobado = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='Si'
            pedi.status='Cotizando'
            pedi.indentificador_estado='2'
            pedi.save()
            return redirect("inv:pedido_list_als")
        else:
            return HttpResponse("el pedido no esta en condición de ser re-autorizado")
    return render(request,template_name,contexto)


@login_required(login_url="/login/")
@permission_required("prf.change_autorizador",login_url="/login/")
def pedido_rechazado_als(request, id):
    pedi = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list_als")
    
    if request.method=='GET':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='No'
            pedi.status='Rechazo'
            pedi.indentificador_estado='5'
            pedi.save()
            return redirect("inv:pedido_list_als")
        else:
            return HttpResponse("el pedido ya fue autorizado")
    
    if request.method=='POST':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='No'
            pedi.status='Rechazo'
            pedi.indentificador_estado='5'
            pedi.save()
            return redirect("inv:pedido_list_als")
        else:
            return HttpResponse("el pedido ya fue autorizado")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("prf.view_autorizantegls",login_url="/login/")
def pedido_aprobado_gls(request, id):
    pedi = Pedido.objects.filter(pk=id).first()

    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list_gls")
    
    if request.method=='GET':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':

            pedi.fecha_aprobado = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='Si'
            pedi.status='Cotizando'
            pedi.indentificador_estado='2'
            pedi.save()
            return redirect("inv:pedido_list_gls")
        else:
            return HttpResponse("el pedido no esta en condición de ser re-autorizado")
    if request.method=='POST':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_aprobado = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='Si'
            pedi.status='Cotizando'
            pedi.indentificador_estado='2'
            pedi.save()
            return redirect("inv:pedido_list_gls")
        else:
            return HttpResponse("el pedido no esta en condición de ser re-autorizado")
    return render(request,template_name,contexto)



@login_required(login_url="/login/")
@permission_required("prf.view_autorizantegls",login_url="/login/")
def pedido_rechazado_gls(request, id):
    pedi = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list_gls")
    
    if request.method=='GET':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='No'
            pedi.status='Rechazo'
            pedi.indentificador_estado='5'
            pedi.save()
            return redirect("inv:pedido_list_gls")
        else:
            return HttpResponse("el pedido ya fue autorizado")
    
    if request.method=='POST':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='No'
            pedi.status='Rechazo'
            pedi.indentificador_estado='5'
            pedi.save()
            return redirect("inv:pedido_list_gls")
        else:
            return HttpResponse("el pedido ya fue autorizado")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("prf.view_autorizantemls",login_url="/login/")
def pedido_aprobado_mls(request, id):
    pedi = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list_mls")
    
    if request.method=='GET':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':

            pedi.fecha_aprobado = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='Si'
            pedi.status='Cotizando'
            pedi.indentificador_estado='2'
            pedi.save()
            return redirect("inv:pedido_list_mls")
        else:
            return HttpResponse("el pedido no esta en condición de ser re-autorizado")
    if request.method=='POST':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_aprobado = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='Si'
            pedi.status='Cotizando'
            pedi.indentificador_estado='2'
            pedi.save()
            return redirect("inv:pedido_list_mls")
        else:
            return HttpResponse("el pedido no esta en condición de ser re-autorizado")
    return render(request,template_name,contexto)


@login_required(login_url="/login/")
@permission_required("prf.view_autorizantemls",login_url="/login/")
def pedido_rechazado_mls(request, id):
    pedi = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list_mls")
    
    if request.method=='GET':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='No'
            pedi.status='Rechazo'
            pedi.indentificador_estado='5'
            pedi.save()
            return redirect("inv:pedido_list_mls")
        else:
            return HttpResponse("el pedido ya fue autorizado")
    
    if request.method=='POST':
        if pedi.status2=='Proximo' and pedi.status=='X-Autorizar':
            pedi.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pedi.status2='No'
            pedi.status='Rechazo'
            pedi.indentificador_estado='5'
            pedi.save()
            return redirect("inv:pedido_list_mls")
        else:
            return HttpResponse("el pedido ya fue autorizado")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("prf.change_comprador",login_url="/login/")
def pedido_comprando(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list_f3")
    
    if request.method=='GET':
        if pede.status2=='Si' and pede.status=='Pendiente':
            pede.fecha_requerido = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Proveedor'
            pede.indentificador_estado='4'
            pede.save()
            return redirect("inv:pedido_list_f3")
        else:
            return HttpResponse("el articulo no está aprobado o ya está terminado")
    
    if request.method=='POST':
        if pede.status2=='Si' and pede.status=='Pendiente':
            pede.fecha_requerido = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Proveedor'
            pede.indentificador_estado='4'
            pede.save()
            return redirect("inv:pedido_list_f3")
        else:
            return HttpResponse("el articulo no está aprobado o ya está terminado")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("prf.change_almacenistaoficina" or "prf.change_almacenistaplanta",login_url="/login/")
def pedido_entregadoo(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list_f4o")
    
    if request.method=='GET':
        if pede.indentificador_estado=='4':
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Recibido'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f4o")
        else:
            return HttpResponse("el pedido aun no está en atención o ya está terminado")
    if request.method=='POST':
        if pede.indentificador_estado=='4':
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Recibido'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f4o")
        else:
            return HttpResponse("el pedido aun no está en atención o ya está terminado")
def pedido_entregadop(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list_f4p")
    
    if request.method=='GET':
        if pede.indentificador_estado=='4':
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Recibido'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f4p")
        else:
            return HttpResponse("el pedido aun no está en atención o ya está terminado")
    
    if request.method=='POST':
        if pede.indentificador_estado=='4':
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Recibido'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f4p")
        else:
            return HttpResponse("el pedido aun no está en atención o ya está terminado")
    return render(request,template_name,contexto)


@login_required(login_url="/login/")
@permission_required("prf.change_comprador",login_url="/login/")
def pedido_reaut(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list_f2")
    if request.method=='GET':
        if pede.precio_uni<=0 or pede.cantidad<=0:
            return HttpResponse("Ingresa un precio positivo primero y revisar la cantidad")
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Esperando OC'
            pede.indentificador_estado='3'
            pede.save()
            return redirect("inv:pedido_list_f2")
        else:
            return HttpResponse("no se puede mandar a orden de compra")
    if request.method=='POST':
        if pede.precio_uni==0 or pede.cantidad==0 or pede.estandarizadorq=="no":
            return HttpResponse("Ingresa el precio primero")
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Esperando OC'
            pede.indentificador_estado='3'
            pede.save()
            return redirect("inv:pedido_list_f2")
        else:
            return HttpResponse("no se puede mandar a orden de compra")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("inv.add_pedido",login_url="/login/")
def pedido_scancela(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list_f2")
    if request.method=='GET':
        if pede.status=='Cotizando':
            pede.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status2='sc'
            pede.status='S-Cancela'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f")
        else:
            return HttpResponse("El pedido ya fue revisado por compras y no lo puedes cancelar desde aquí. comunicate con compras")
    if request.method=='POST':
        if pede.status=='Cotizando':
            pede.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status2='SC'
            pede.status='S-Cancela'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f")
        else:
            return HttpResponse("El pedido ya fue revisado y no lo puedes cancelar. comunicate con compras")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("prf.change_universal",login_url="/login/")
def pedido_acancela(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("cmp:compras_list")
    if request.method=='GET':
        if pede.indentificador_estado=='1':
            pede.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status2='sc'
            pede.status='Rechazado'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("cmp:compras_list")
        else:
            return HttpResponse("El pedido no puede ser finalizado de forma anormal")
    if request.method=='POST':
        if pede.indentificador_estado=='1':
            pede.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status2='SC'
            pede.status='Rechazado'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("cmp:compras_list")
        else:
            return HttpResponse("El pedido no puede ser finalizado de forma anormal")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("prf.change_almacenista",login_url="/login/")
def pedido_stock(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"
    if not pede:
        return redirect("inv:pedido_list")
    if request.method=='GET':
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Stock'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f2")
        else:
            return HttpResponse("Esta opción no está disponible")
    if request.method=='POST':
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Stock'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list")
        else:
            return HttpResponse("Esta opción no está disponible")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("prf.change_almacenista",login_url="/login/")
def pedido_enviado(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"
    if not pede:
        return redirect("inv:pedido_list")
    if request.method=='GET':
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='X-Trasladar'
            pede.indentificador_estado='6'
            pede.save()
            return redirect("inv:pedido_list_f2")
        else:
            return HttpResponse("Esta opción no está disponible")
    if request.method=='POST':
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='X-Trasladar'
            pede.indentificador_estado='6'
            pede.save()
            return redirect("inv:pedido_list")
        else:
            return HttpResponse("Esta opción no está disponible")
    return render(request,template_name,contexto)
@login_required(login_url="/login/")
@permission_required("prf.change_almacenista",login_url="/login/")
def pedido_transferido(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"
    if not pede:
        return redirect("inv:pedido_list")
    if request.method=='GET':
        if pede.status2=='Si' and pede.status=='X-Trasladar':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Enviado-Fin'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list_f2")
        else:
            return HttpResponse("Esta opción no está disponible")
    if request.method=='POST':
        if pede.status2=='Si' and pede.status=='X-Trasladar':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Enviado-Fin'
            pede.indentificador_estado='5'
            pede.save()
            return redirect("inv:pedido_list")
        else:
            return HttpResponse("Esta opción no está disponible")
    return render(request,template_name,contexto)
@login_required(login_url="/login/")
@permission_required("prf.change_auxcompras",login_url="/login/")
def pedido_express(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    precios = Artciulosestandarizados.objects.filter(pk=pede.idestandarizado)
    precios = precios.get()
    contexto={}
    template_name="inv/pedidos_brinco.html"
    if not pede:
        return redirect("inv:pedido_list")
    if request.method=='GET':
        if pede.precio_uni==0 or pede.cantidad==0 or pede.folio_ingreso=="--":
            return HttpResponse("Primero ingresa el monto $ de la compra Directo y/o el Proveedor C Directo")
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status2='na'
            pede.status='Directo'
            pede.indentificador_estado='5'
            precios.precio4 = precios.precio3
            precios.precio3 = precios.precio2
            precios.precio2 = precios.preciosugerido
            precios.preciosugerido = pede.precio_uni
            precios.fecha4 = precios.fecha3
            precios.fecha3 = precios.fecha2
            precios.fecha2 = precios.fechapreciosugerido
            precios.fechapreciosugerido = datetime.now()
            precios.save()

            pede.save()
            return redirect("inv:pedido_list_f2")
        else:
            return HttpResponse("Esta opción no está disponible")
    if request.method=='POST':
        if pede.precio_uni==0 or pede.cantidad==0:
            return HttpResponse("Primero ingresa el monto $ de la compra Directo")
        if pede.status2=='Si' and pede.status=='Cotizando':
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status2='na'
            pede.status='Directo'
            pede.indentificador_estado='5'
            precios.precio4 = precios.precio3
            precios.precio3 = precios.precio2
            precios.precio2 = precios.preciosugerido
            precios.preciosugerido = pede.precio_uni
            precios.fecha4 = precios.fecha3
            precios.fecha3 = precios.fecha2
            precios.fecha2 = precios.fechapreciosugerido
            precios.fechapreciosugerido = datetime.now()
            precios.save()

            pede.save()
            return redirect("inv:pedido_list")
        else:
            return HttpResponse("Esta opción no está disponible")
    return render(request,template_name,contexto)

def pedido_oc(request, id):
    pede = Pedido.objects.filter(pk=id).get()
    pede = pede.id
    if request.method=='GET':
        if ComprasDet.objects.filter(pedido_id=pede).exists() == True:
            triplebusqueda = ComprasDet.objects.filter(pedido_id=pede).get()
            triplebusqueda = ComprasEnc.objects.filter(id=triplebusqueda.compra_id).get()
            return redirect("cmp:compras_print_public",clienteuniqueid=triplebusqueda.clienteuniqueid)
        else:
            return HttpResponse("Esta pedido no esta en ninguna orden de compra. Pudo ser oc-cancela, Pedido Directo, ó Stock")
    return redirect("inv:pedidos_list")


"""RH EDIT Aqui"""


class BancoView(SinPrivilegios, \
    generic.ListView):
    permission_required = "inv.view_banco"
    model = Banco
    template_name = "inv/banco_list.html"
    context_object_name = "obj"



class BancoNew(SuccessMessageMixin,SinPrivilegios,\
    generic.CreateView):
    permission_required="inv.add_banco"
    model=Banco
    template_name="inv/banco_form.html"
    context_object_name = "obj"
    form_class=BancoForm
    success_url=reverse_lazy("inv:banco_list")
    success_message="Banconte registrado"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class BancoEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    permission_required="inv.change_banco"
    model=Banco
    template_name="inv/banco_form.html"
    context_object_name = "obj"
    form_class=BancoForm
    success_url=reverse_lazy("inv:banco_list")
    success_message="Banco Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class BancoDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    permission_required="inv.delete_banco"
    model=Banco
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:banco_list")
    success_message="Banco Eliminada Satisfactoriamente"

class PuestoView(SinPrivilegios,\
     generic.ListView):
    permission_required = "inv.view_puesto"
    model = Puesto
    template_name = "inv/puesto_list.html"
    context_object_name = "obj"


class PuestoNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Puesto
    template_name="inv/puesto_form.html"
    context_object_name = 'obj'
    form_class=PuestoForm
    success_url= reverse_lazy("inv:puesto_list")
    success_message="Puesto Creada"
    permission_required="inv.add_puesto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class PuestoEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Puesto
    template_name="inv/puesto_form.html"
    context_object_name = 'obj'
    form_class=PuestoForm
    success_url= reverse_lazy("inv:puesto_list")
    success_message="Puesto Editada"
    permission_required="inv.change_puesto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class EmpleadoView(SinPrivilegios,\
     generic.ListView):
    permission_required = "inv.view_empleado"
    model = Empleado
    template_name = "inv/empleado_list.html"
    context_object_name = "obj"

class ParentescocontactoNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Parentescocontacto
    template_name="inv/parentescocontacto_form.html"
    context_object_name = 'obj'
    form_class=ParentescocontactoForm
    success_url= reverse_lazy("inv:parentescocontacto_list")
    success_message="Parentesco Creado"
    permission_required="inv.add_parentescocontacto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ParentescocontactoEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Parentescocontacto
    template_name="inv/puesto_parentescocontacto.html"
    context_object_name = 'obj'
    form_class=ParentescocontactoForm
    success_url= reverse_lazy("inv:parentescocontacto_list")
    success_message="Parentesco Editado"
    permission_required="inv.change_parentescocontacto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ParentescocontactoView(SinPrivilegios,\
     generic.ListView):
    permission_required = "inv.view_parentescocontacto"
    model = Parentescocontacto
    template_name = "inv/parentescocontacto_list.html"
    context_object_name = "obj"


class EmpleadoNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Empleado
    template_name="inv/empleado_form.html"
    context_object_name = 'obj'
    form_class=EmpleadoForm
    success_url= reverse_lazy("inv:empleado_list")
    success_message="Empleado Registrado"
    permission_required="inv.add_empleado"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EmpleadoEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Empleado
    template_name="inv/empleado_form.html"
    context_object_name = 'obj'
    form_class=EmpleadoForm
    success_url= reverse_lazy("inv:empleado_list")
    success_message="Empleado Editada"
    permission_required="inv.change_empleado"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

"""computadora"""
class ComputadoraView(SinPrivilegios,\
     generic.ListView):
    permission_required = "inv.view_computadora"
    model = Computadora
    template_name = "inv/computadora_list.html"
    context_object_name = "obj"


class ComputadoraNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Computadora
    template_name="inv/computadora_form.html"
    context_object_name = 'obj'
    form_class=ComputadoraForm
    success_url= reverse_lazy("inv:computadora_list")
    success_message="Computadora Registrado"
    permission_required="inv.add_computadora"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ComputadoraEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Computadora
    template_name="inv/computadora_form.html"
    context_object_name = 'obj'
    form_class=ComputadoraForm
    success_url= reverse_lazy("inv:computadora_list")
    success_message="Computadora Editada"
    permission_required="inv.change_computadora"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

"""herramienta"""
class HerramientaView(SinPrivilegios,\
     generic.ListView):
    permission_required = "inv.view_herramienta"
    model = Herramienta
    template_name = "inv/herramienta_list.html"
    context_object_name = "obj"


class HerramientaNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Herramienta
    template_name="inv/herramienta_form.html"
    context_object_name = 'obj'
    form_class=HerramientaForm
    success_url= reverse_lazy("inv:herramienta_list")
    success_message="Herramienta Registrado"
    permission_required="inv.add_herramienta"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class HerramientaEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Herramienta
    template_name="inv/herramienta_form.html"
    context_object_name = 'obj'
    form_class=HerramientaForm
    success_url= reverse_lazy("inv:herramienta_list")
    success_message="Herramienta Editada"
    permission_required="inv.change_herramienta"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

"""empresas"""

class EmpresaView(SinPrivilegios, \
    generic.ListView):
    permission_required = "inv.view_empresa"
    model = Empresa
    template_name = "inv/empresa_list.html"
    context_object_name = "obj"
    


class EmpresaNew(SuccessMessageMixin,SinPrivilegios,\
    generic.CreateView):
    permission_required="inv.add_empresa"
    model=Empresa
    template_name="inv/empresa_form.html"
    context_object_name = "obj"
    form_class=EmpresaForm
    success_url=reverse_lazy("inv:empresa_list")
    success_message="Empresante registrado"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EmpresaEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    permission_required="inv.change_empresa"
    model=Empresa
    template_name="inv/empresa_form.html"
    context_object_name = "obj"
    form_class=EmpresaForm
    success_url=reverse_lazy("inv:empresa_list")
    success_message="Empresa Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


"""Genero"""


class GeneroView(SinPrivilegios, \
                  generic.ListView):
    permission_required = "inv.view_genero"
    model = Genero
    template_name = "inv/genero_list.html"
    context_object_name = "obj"


class GeneroNew(SuccessMessageMixin, SinPrivilegios, \
                 generic.CreateView):
    permission_required = "inv.add_genero"
    model = Genero
    template_name = "inv/genero_form.html"
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("inv:genero_list")
    success_message = "Genero registrado"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class GeneroEdit(SuccessMessageMixin, SinPrivilegios, \
                  generic.UpdateView):
    permission_required = "inv.change_genero"
    model = Genero
    template_name = "inv/genero_form.html"
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("inv:genero_list")
    success_message = "Genero Actualizado"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


"""Estudios"""

class EstudiosView(SinPrivilegios, \
                  generic.ListView):
    permission_required = "inv.view_estudios"
    model = Estudios
    template_name = "inv/estudios_list.html"
    context_object_name = "obj"


class EstudiosNew(SuccessMessageMixin, SinPrivilegios, \
                 generic.CreateView):
    permission_required = "inv.add_estudios"
    model = Estudios
    template_name = "inv/estudios_form.html"
    context_object_name = "obj"
    form_class = EstudiosForm
    success_url = reverse_lazy("inv:estudios_list")
    success_message = "Nivel escolar registrado"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EstudiosEdit(SuccessMessageMixin, SinPrivilegios, \
                  generic.UpdateView):
    permission_required = "inv.change_estudios"
    model = Estudios
    template_name = "inv/estudios_form.html"
    context_object_name = "obj"
    form_class = EstudiosForm
    success_url = reverse_lazy("inv:estudios_list")
    success_message = "Nivel escolar Actualizado"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

"""Estudios Fin"""
"""Ecivil"""

class EcivilView(SinPrivilegios, \
                  generic.ListView):
    permission_required = "inv.view_ecivil"
    model = Ecivil
    template_name = "inv/ecivil_list.html"
    context_object_name = "obj"


class EcivilNew(SuccessMessageMixin, SinPrivilegios, \
                 generic.CreateView):
    permission_required = "inv.add_ecivil"
    model = Ecivil
    template_name = "inv/ecivil_form.html"
    context_object_name = "obj"
    form_class = EcivilForm
    success_url = reverse_lazy("inv:ecivil_list")
    success_message = "Estado Civil Registrado"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EcivilEdit(SuccessMessageMixin, SinPrivilegios, \
                  generic.UpdateView):
    permission_required = "inv.change_ecivil"
    model = Ecivil
    template_name = "inv/ecivil_form.html"
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("inv:ecivil_list")
    success_message = "Estado Civil Modificado"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

"""Ecivil Fin"""
"""Departamento"""

class DepartamentoView(SinPrivilegios, \
                  generic.ListView):
    permission_required = "inv.view_departamento"
    model = Departamento
    template_name = "inv/departamento_list.html"
    context_object_name = "obj"


class DepartamentoNew(SuccessMessageMixin, SinPrivilegios, \
                 generic.CreateView):
    permission_required = "inv.add_departamento"
    model = Departamento
    template_name = "inv/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("inv:departamento_list")
    success_message = "Departamento dado de alta"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class DepartamentoEdit(SuccessMessageMixin, SinPrivilegios, \
                  generic.UpdateView):
    permission_required = "inv.change_departamento"
    model = Genero
    template_name = "inv/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("inv:departamento_list")
    success_message = "departamento Actualizado"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

"""Departamento Fin"""

class ArtciulosestandarizadosView(SinPrivilegios,generic.ListView):
    permission_required = "inv.view_artciulosestandarizados"
    model = Artciulosestandarizados
    template_name = "inv/articuloes_list_all.html"
    context_object_name = "obj"
    


class ArtciulosestandarizadosNew(SuccessMessageMixin,SinPrivilegios,\
    generic.CreateView):
    permission_required="inv.add_artciulosestandarizados"
    model= Artciulosestandarizados
    template_name="inv/form_ae_estandar.html"
    context_object_name = "obj"
    form_class=ArtciulosestandarizadosForm
    success_url=reverse_lazy("inv:articuloes_new")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ArtciulosestandarizadosEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    permission_required="inv.change_artciulosestandarizados"
    model= Artciulosestandarizados
    template_name="inv/form_ae_estandar.html"
    context_object_name = "obj"
    form_class=ArtciulosestandarizadosForm
    success_url=reverse_lazy("inv:articuloes_list")
    success_message="Articulo estandarizado Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class NombresrelacionView(SinPrivilegios,generic.ListView):
    permission_required = "inv.view_nombresrelacion"
    model = Nombresrelacion
    template_name = "inv/nombresrelacion_list.html"
    context_object_name = "obj"
    


class NombresrelacionNew(SuccessMessageMixin,SinPrivilegios,\
    generic.CreateView):
    permission_required="inv.add_nombresrelacion"
    model=Nombresrelacion
    template_name="inv/relacioncorregida_form.html"
    context_object_name = "obj"
    form_class=NombresrelacionForm
    success_message="Relacion Registada"
    success_url=reverse_lazy("inv:nombrerelacion_new")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class NombresrelacionEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    permission_required="inv.change_nombresrelacion"
    model=Nombresrelacion
    template_name="inv/relacioncorregida_form.html"
    context_object_name = "obj"
    form_class=NombresrelacionForm
    success_url=reverse_lazy("inv:nombrerelacion_list")
    success_message="Nombre Relación Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
"""Almacen"""


@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases:sin_privilegios')
def ingresoalmacen(request, oc=None):
    template_name = "inv/ingresoalmacen.html"
    prod = ComprasDet.objects.filter(compra_id=6)
    form_compras = {}
    contexto = {}

    if request.method == 'GET':
        form_compras = ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=oc).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            e = {
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }
            form_compras = ComprasEncForm(e)
        else:
            det = None

        contexto = {'productos': prod, 'encabezado': enc, 'detalle': det, 'form_enc': form_compras}

    if request.method == 'POST':
        fecha_compra = request.POST.get("fecha_compra")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        proveedor = request.POST.get("proveedor")
        sub_total = 0
        descuento = 0
        total = 0

        if not oc:
            prov = Proveedor.objects.get(pk=proveedor)

            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc=request.user
            )
            if enc:
                enc.save()
                oc = enc.id
        else:
            enc = ComprasEnc.objects.filter(pk=oc).first()
            if enc:
                enc.fecha_compra = fecha_compra
                enc.observacion = observacion
                enc.no_factura = no_factura
                enc.fecha_factura = fecha_factura
                enc.um = request.user.id
                enc.save()

        if not oc:
            return redirect("cmp:compras_list")

        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle = request.POST.get("id_descuento_detalle")
        total_detalle = request.POST.get("id_total_detalle")

        prod = Producto.objects.get(pk=producto)

        det = ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
            uc=request.user
        )

        if det:
            det.save()

            sub_total = ComprasDet.objects.filter(compra=oc).aggregate(Sum('sub_total'))
            descuento = ComprasDet.objects.filter(compra=oc).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento = descuento["descuento__sum"]
            enc.save()

        return redirect("cmp:compras_edit", oc=oc)

    return render(request, template_name, contexto)

import pandas as pd
from django.db import transaction
def importar_compras_excel(request):
    if request.method == 'POST':
        file = request.FILES.get('excel')
        array_pedidos = []
        if file:
            read = pd.read_excel(file)
            articuloQ =  Artciulosestandarizados.objects.all()
            with transaction.atomic():
                for i in range(len(read)):
                    fila_actual = read.iloc[i]
                    pedido_actual = Pedido()
                    pedido_actual.cantidad = fila_actual.iloc[0]
                    pedido_actual.articulo = fila_actual.iloc[1].upper()
                    pedido_actual.UniMed_id = fila_actual.iloc[2]
                    pedido_actual.comentario = fila_actual.iloc[3]
                    pedido_actual.autpor_id = fila_actual.iloc[4]
                    pedido_actual.precio_uni = fila_actual.iloc[5]
                    pedido_actual.proceso = fila_actual.iloc[6].upper()
                    pedido_actual.status2 = ""
                    pedido_actual.uc_id = request.user.id

                    #Si lo que quieres hacer es un guardado másivo, puedes hacerlo con un array y luego hacer un bulk_create,
                    #pero esto no entrará al save, asi que tendrás que hacer la lógica del save aquí mismo
                    # # pedido_actual.proceso = pedido_actual.proceso.replace("'","")
                    # # pedido_actual.preciotransaccion =  float(float(pedido_actual.cantidad)) * float(pedido_actual.precio_uni)
                    # print(request.user.id, fila_actual.iloc[2] )
                    # # articulo_actual = articuloQ.filter(descripcion=pedido_actual.articulo).first()
                    # # if articulo_actual:
                    # #     pedido_actual.estandarizadoprodu = articulo_actual
                    # #     pedido_actual.motivo_peticion = articulo_actual.descripcion
                    # #     pedido_actual.articulo = articulo_actual.descripcion
                    # # elif pedido_actual.articulo != 'NA' and pedido_actual.motivo_peticion == 'NA':
                    # #     pedido_actual.articulo = pedido_actual.articulo.upper()
                    # #     pedido_actual.articulo = pedido_actual.articulo.replace("'", "")
                    # #     pedido_actual.articulo = normalize(pedido_actual.articulo)
                    # #     pedido_actual.motivo_peticion = pedido_actual.articulo
                    # # array_pedidos.append(pedido_actual)
                    
                    pedido_actual.save()
            # Pedido.objects.bulk_create(array_pedidos)
    return render(request, 'inv/importar_excel.html',{})
