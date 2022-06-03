from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
import datetime
from django.http import HttpResponse, JsonResponse

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json
from django.db.models import Sum

from django.contrib.humanize.templatetags.humanize import intcomma


from .models import Proveedor, ComprasEnc, ComprasDet, Empresa, UsoFactura
from cmp.forms import ProveedorForm,ComprasEncForm, UsoFacturaForm
from bases.views import SinPrivilegios
from inv.models import Pedido
import string
import random

def id_generator(size=40, chars=string.ascii_letters + string.digits):
    verificadorid = ''.join(random.choice(chars) for _ in range(size))
    repetidocheck = ComprasEnc.objects.filter(clienteuniqueid=verificadorid).exists()
    while repetidocheck == True:
        verificadorid = ''.join(random.choice(chars) for _ in range(size))
        repetidocheck = ComprasEnc.objects.filter(clienteuniqueid=verificadorid).exists()
    return verificadorid




class ProveedorView(SinPrivilegios, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    permission_required="cmp.view_proveedor"

class ProveedorNew(SuccessMessageMixin, SinPrivilegios,\
                   generic.CreateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    success_message="Proveedor Nuevo"
    permission_required="cmp.add_proveedor"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)


class ProveedorEdit(SuccessMessageMixin, SinPrivilegios,\
                   generic.UpdateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    success_message="Proveedor Editado"
    permission_required="cmp.change_proveedor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("cmp.change_proveedor",login_url="/login/")
def proveedorInactivar(request,id):
    template_name='cmp/inactivar_prv.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))

    if request.method=='GET':
        contexto={'obj':prv}

    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request,template_name,contexto)

class UsoFacturaView(SinPrivilegios, generic.ListView):
    model = UsoFactura
    template_name = "cmp/usofactura_list.html"
    context_object_name = "obj"
    permission_required="cmp.view_UsoFactura"

class UsoFacturaNew(SuccessMessageMixin, SinPrivilegios,\
                generic.CreateView):
    model=UsoFactura
    template_name="cmp/usofactura_form.html"
    context_object_name = 'obj'
    form_class=UsoFacturaForm
    success_url= reverse_lazy("cmp:usofactura_list")
    success_message="Clave de sat agregada"
    permission_required="cmp.add_UsoFactura"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)


class UsoFacturaEdit(SuccessMessageMixin, SinPrivilegios,\
                generic.UpdateView):
    model=UsoFactura
    template_name="cmp/usofactura_form.html"
    context_object_name = 'obj'
    form_class=UsoFacturaForm
    success_url= reverse_lazy("cmp:usofactura_list")
    success_message="Clave de sat editada Editado"
    permission_required="cmp.change_UsoFactura"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("cmp.change_UsoFactura",login_url="/login/")
def UsoFacturaInactivar(request,id):
    template_name='cmp/inactivar_prv.html'
    contexto={}
    prv = UsoFactura.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Clave del SAT no existe ' + str(id))

    if request.method=='GET':
        contexto={'obj':prv}

    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Clave de SAT Inactivado')

    return render(request,template_name,contexto)

class ComprasView(SinPrivilegios, generic.ListView):
    model = ComprasEnc
    template_name = "cmp/compras_list.html"
    context_object_name = "obj"
    permission_required="cmp.view_comprasenc"


@login_required(login_url='/login/')
@permission_required('cmp.edit_comprasenc', login_url='bases:sin_privilegios')
def compras(request,compra_id=None):
    template_name="cmp/compras.html"
    prod=Pedido.objects.filter(indentificador_estado=3)
    form_compras={}
    contexto={}

    if request.method=='GET':
        form_compras=ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            e = {
                'fecha_compra':fecha_compra,
                'proveedor': enc.proveedor,
                'empresaoc': enc.empresaoc,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total':enc.total
            }
            form_compras = ComprasEncForm(e)
        else:
            det=None
        contexto={'pedidos':prod,'encabezado':enc,'detalle':det,'form_enc':form_compras}

    if request.method=='POST':
        fecha_compra = request.POST.get("fecha_compra")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        proveedor = request.POST.get("proveedor")
        empresaoc = request.POST.get("empresaoc")
        sub_total = 0
        descuento = 0
        total = 0

        if not compra_id:
            prov=Proveedor.objects.get(pk=proveedor)
            emproc=Empresa.objects.get(pk=empresaoc)
            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                empresaoc=emproc,
                proveedor=prov,
                uc = request.user,
            )
            if enc:
                enc.clienteuniqueid = id_generator()
                enc.save()
                compra_id=enc.id
        else:
            enc=ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_compra = fecha_compra
                enc.observacion = observacion
                enc.no_factura=no_factura
                enc.um=request.user.id
                enc.clienteuniqueid = id_generator()
                enc.save()

        if not compra_id:
            return redirect("cmp:compras_list")
        pedido = request.POST.get("id_id_pedido")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle  = request.POST.get("id_descuento_detalle")
        total_detalle  = request.POST.get("id_total_detalle")

        prod = Pedido.objects.get(pk=pedido)

        det = ComprasDet(
            compra=enc,
            pedido=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
            uc = request.user,
        )

        if det:
            if ComprasDet.objects.filter(pedido_id=pedido).exists() == True:
                antiduplicado = ComprasDet.objects.filter(pedido_id=pedido).get()
                return redirect("cmp:compras_edit",compra_id=antiduplicado.compra_id)
            det.save()

            sub_total=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento=descuento["descuento__sum"]
            enc.save()

        return redirect("cmp:compras_edit",compra_id=compra_id)


    return render(request, template_name, contexto)


class CompraDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "cmp.delete_comprasdet"
    model = ComprasDet
    template_name = "cmp/compras_det_del.html"
    context_object_name = 'obj'
    def get_success_url(self):
        compra_id=self.kwargs['compra_id']
        return reverse_lazy('cmp:compras_edit', kwargs={'compra_id': compra_id})