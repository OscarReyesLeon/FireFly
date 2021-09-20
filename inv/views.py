from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime


from .models import Autoriza, Equipo, Pedido,Proceso, Categoria, UnidadMedida, \
    Producto, Pedido, Banco, Puesto, Empleado, Computadora, Herramienta, Empresa
from .forms import EquipoForm, ProcesoForm, CategoriaForm, \
    UMForm, ProductoForm, PedidoForm, AutorizaForm, BancoForm, PuestoForm, \
    EmpleadoForm, ComputadoraForm, HerramientaForm, \
    EmpresaForm

from bases.views import SinPrivilegios



class EquipoView(SinPrivilegios, \
    generic.ListView):
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


class UMNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inv:um_list")
    success_message="Unidad Medida Creada"
    permission_required="inv.add_unidadmedida"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
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
        print(self.request.user.id)
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
    template_name = "inv/prducto_list.html"
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
    template_name = "inv/prducto_list.html"
    context_object_name = "obj"
    permission_required="inv.view_pedido"


class PedidoNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Pedido
    template_name="inv/pedido_form.html"
    context_object_name = 'obj'
    form_class=PedidoForm
    success_url= reverse_lazy("inv:pedido_list")
    success_message="Pedido Creado"
    permission_required="inv.add_pedido"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(PedidoNew, self).get_context_data(**kwargs)
        context["equipos"] = Equipo.objects.all()
        context["procesos"] = Proceso.objects.all()
        return context
"""revisar equipo y proceso"""


class PedidoEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Pedido
    template_name="inv/pedido_form.html"
    context_object_name = 'obj'
    form_class=PedidoForm
    success_url= reverse_lazy("inv:pedido_list")
    success_message="Pedido Editado"
    permission_required="inv.change_pedido"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(PedidoEdit, self).get_context_data(**kwargs)
        context["equipos"] = Equipo.objects.all()
        context["procesos"] = Proceso.objects.all()
        context["obj"] = Pedido.objects.filter(pk=pk).first()

        return context


@login_required(login_url="/login/")
@permission_required("inv.view_autoriza",login_url="/login/")
def pedido_aprobado(request, id):
    pedi = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list")
    
    if request.method=='GET':
        contexto={'obj':pedi}
    
    if request.method=='POST':
        pedi.fecha_aprobado = datetime.now().strftime('%d-%m-%y %H:%M')
        pedi.status2='Si'
        pedi.save()
        return redirect("inv:pedido_list")

    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("inv.view_autoriza",login_url="/login/")
def pedido_rechazado(request, id):
    pedi = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pedi:
        return redirect("inv:pedido_list")
    
    if request.method=='GET':
        contexto={'obj':pedi}
    
    if request.method=='POST':
        pedi.fecha_rechazo = datetime.now().strftime('%d-%m-%y %H:%M')
        pedi.status2='No'
        pedi.save()
        return redirect("inv:pedido_list")

    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("inv.change_producto",login_url="/login/")
def pedido_comprando(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list")
    
    if request.method=='GET':
        contexto={'obj':pede}
    
    if request.method=='POST':
        if pede.status2=='Si' and pede.status=='--':
            pede.fecha_requerido = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Si'
            pede.save()
            return redirect("inv:pedido_list")
        else:
            return HttpResponse("el articulo no está aprobado o ya está terminado")
    return render(request,template_name,contexto)

@login_required(login_url="/login/")
@permission_required("inv.change_producto",login_url="/login/")
def pedido_entregado(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list")
    
    if request.method=='GET':
        contexto={'obj':pede}
    
    if request.method=='POST':
        if pede.status=='Si':
            pede.fecha_finalizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='Fin'
            pede.save()
            return redirect("inv:pedido_list")
        else:
            return HttpResponse("el pedido aun no está en atención o ya está terminado")
    return render(request,template_name,contexto)


@login_required(login_url="/login/")
@permission_required("inv.change_producto",login_url="/login/")
def pedido_reaut(request, id):
    pede = Pedido.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/pedidos_brinco.html"

    if not pede:
        return redirect("inv:pedido_list")
    
    if request.method=='GET':
        contexto={'obj':pede}
    
    if request.method=='POST':
        if pede.status2=='Si' and pede.status=='--':
            pede.fecha_recotizado = datetime.now().strftime('%d-%m-%y %H:%M')
            pede.status='--'
            pede.status2='ReCotizado'
            pede.save()
            return redirect("inv:pedido_list")
        else:
            return HttpResponse("el pedido no esta en condición de ser re-autorizado")


    return render(request,template_name,contexto)


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


"""fin de la edición"""