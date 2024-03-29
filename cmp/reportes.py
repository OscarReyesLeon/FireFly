import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.loader import render_to_string
from .models import ComprasEnc, ComprasDet

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def reporte_compras(request):
    template_path = 'cmp/compras_print_all.html'
    today = timezone.now()

    compras = ComprasEnc.objects.all()
    context = {
        'obj': compras,
        'today': today,
        'request': request
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def reporte_compras_modal(request):
    template_path = "cmp/details.html"
    id = request.GET.get('id')
    compra = ComprasEnc.objects.get(id=id)
    details = ComprasDet.objects.filter(compra__id=id)
    #render template 
    context = {
        'obj': compra,
        'detalle': details,
        }
    html = render_to_string(template_name=template_path, context=context)
    return HttpResponse(html)
    
@login_required(login_url="/login/")
@permission_required("cmp.view_comprasenc",login_url="/login/")
def imprimir_compra(request, compra_id):
    template_path = 'cmp/compras_print_one.html'
    today = timezone.now()
    paraborrarvacios = ComprasEnc.objects.filter(total="0")
    paraborrarvacios.delete()

    
    enc = ComprasEnc.objects.filter(id=compra_id).first()
    if enc:
        detalle = ComprasDet.objects.filter(compra__id=compra_id)
    else:
        detalle={}

    
    context = {
        'detalle': detalle,
        'encabezado':enc,
        'today':today,
        'request': request
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def imprimir_compra2(request, clienteuniqueid):
    template_path = 'cmp/compras_print_one.html'
    today = timezone.now()
    paraborrarvacios = ComprasEnc.objects.filter(total="0")
    paraborrarvacios.delete()
    if ComprasEnc.objects.filter(clienteuniqueid=clienteuniqueid).exists() == True:
        compra_id = ComprasEnc.objects.filter(clienteuniqueid=clienteuniqueid).get()
        compra_id = compra_id.id
    else:
        return redirect("inv:pedido_list_f4p")
    
    enc = ComprasEnc.objects.filter(id=compra_id).first()
    if enc:
        detalle = ComprasDet.objects.filter(compra__id=compra_id)
    else:
        detalle={}

    
    context = {
        'detalle': detalle,
        'encabezado':enc,
        'today':today,
        'request': request
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="OC-%s.pdf"'%(compra_id)
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def imprimir_compra3(request, clienteuniqueid):
    template_path = 'cmp/compras_print_three.html'
    today = timezone.now()
    paraborrarvacios = ComprasEnc.objects.filter(total="0")
    paraborrarvacios.delete()
    if ComprasEnc.objects.filter(clienteuniqueid=clienteuniqueid).exists() == True:
        compra_id = ComprasEnc.objects.filter(clienteuniqueid=clienteuniqueid).get()
        compra_id = compra_id.id
    else:
        return redirect("inv:pedido_list_f4p")
    
    enc = ComprasEnc.objects.filter(id=compra_id).first()
    if enc:
        detalle = ComprasDet.objects.filter(compra__id=compra_id)
    else:
        detalle={}

    
    context = {
        'detalle': detalle,
        'encabezado':enc,
        'today':today,
        'request': request
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="OrdenEstandarizada.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
