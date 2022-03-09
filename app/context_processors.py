from inv.models import Pedido
from datetime import datetime, timedelta

def nan0(v):
    for i in range(len(v)):
        if v[i] == 0:
            v[i] = "NaN"
    return v

def pedidos_status(request):
    statusEn1 = Pedido.objects.filter(indentificador_estado=1).order_by('-id')[:999].count()
    statusEn2 = Pedido.objects.filter(indentificador_estado=2).order_by('-id')[:999].count()
    statusEn3 = Pedido.objects.filter(indentificador_estado=3).order_by('-id')[:999].count()
    statusEn4 = Pedido.objects.filter(indentificador_estado=4).order_by('-id')[:999].count()
    statusAll = statusEn1 +  statusEn2 + statusEn3 + statusEn4
    
    XRevisar = Pedido.objects.filter(status="X-Revisar").order_by('-id')[:999].count()
    Revisado = Pedido.objects.filter(status="Revisado").order_by('-id')[:999].count()
    Pendiente = Pedido.objects.filter(status="Pendiente").order_by('-id')[:999].count()
    enProveedor = Pedido.objects.filter(status="en Proveedor").order_by('-id')[:999].count()
    XasignarOC = Pedido.objects.filter(status="X asignar OC").order_by('-id')[:999].count()
    datagraph = [XasignarOC, XRevisar, Revisado, Pendiente, enProveedor,]
    
    fechahoy = datetime.today()
    diahoy = fechahoy.strftime('%d')
    meshoy = fechahoy.strftime('%m')
    anohoy = fechahoy.strftime('%Y')
    
    fecha1 = fechahoy + timedelta(days=-1)
    dia1 = fecha1.strftime('%d')
    mes1 = fecha1.strftime('%m')
    ano1 = fecha1.strftime('%Y')
    
    fecha2 = fechahoy + timedelta(days=-2)
    dia2 = fecha2.strftime('%d')
    mes2 = fecha2.strftime('%m')
    ano2 = fecha2.strftime('%Y')
    
    fecha3 = fechahoy + timedelta(days=-3)
    dia3 = fecha3.strftime('%d')
    mes3 = fecha3.strftime('%m')
    ano3 = fecha3.strftime('%Y')
    
    fecha4 = fechahoy + timedelta(days=-4)
    dia4 = fecha4.strftime('%d')
    mes4 = fecha4.strftime('%m')
    ano4 = fecha4.strftime('%Y')
    
    fecha5 = fechahoy + timedelta(days=-5)
    dia5 = fecha5.strftime('%d')
    mes5 = fecha5.strftime('%m')
    ano5 = fecha5.strftime('%Y')
    
    fecha6 = fechahoy + timedelta(days=-6)
    dia6 = fecha6.strftime('%d')
    mes6 = fecha6.strftime('%m')
    ano6 = fecha6.strftime('%Y')
    
    fecha7 = fechahoy + timedelta(days=-7)
    dia7 = fecha7.strftime('%d')
    mes7 = fecha7.strftime('%m')
    ano7 = fecha7.strftime('%Y')
    
    fecha8 = fechahoy + timedelta(days=-8)
    dia8 = fecha8.strftime('%d')
    mes8 = fecha8.strftime('%m')
    ano8 = fecha8.strftime('%Y')
    dia0oc = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="X asignar OC").count()
    dia0xr = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="X-Revisar").count()
    dia0re = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Revisado").count()
    dia0pe = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Pendiente").count()
    dia0pr = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="en Proveedor").count()
    dia0di = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Directa").count()
    dia0fn = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Fin").count()
    dia0st = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Stock").count()
    dia0ll = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy).count()
    
    dia1oc = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="X asignar OC").count()
    dia1xr = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="X-Revisar").count()
    dia1re = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Revisado").count()
    dia1pe = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Pendiente").count()
    dia1pr = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="en Proveedor").count()
    dia1di = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Directa").count()
    dia1fn = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Fin").count()
    dia1st = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Stock").count()
    dia1ll = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1).count()
    
    dia2oc = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="X asignar OC").count()
    dia2xr = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="X-Revisar").count()
    dia2re = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Revisado").count()
    dia2pe = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Pendiente").count()
    dia2pr = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="en Proveedor").count()
    dia2di = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Directa").count()
    dia2fn = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Fin").count()
    dia2st = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Stock").count()
    dia2ll = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2).count()
    
    dia3oc = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="X asignar OC").count()
    dia3xr = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="X-Revisar").count()
    dia3re = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Revisado").count()
    dia3pe = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Pendiente").count()
    dia3pr = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="en Proveedor").count()
    dia3di = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Directa").count()
    dia3fn = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Fin").count()
    dia3st = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Stock").count()
    dia3ll = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3).count()
    
    dia4oc = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="X asignar OC").count()
    dia4xr = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="X-Revisar").count()
    dia4re = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Revisado").count()
    dia4pe = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Pendiente").count()
    dia4pr = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="en Proveedor").count()
    dia4di = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Directa").count()
    dia4fn = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Fin").count()
    dia4st = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Stock").count()
    dia4ll = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4).count()
    
    dia5oc = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="X asignar OC").count()
    dia5xr = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="X-Revisar").count()
    dia5re = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Revisado").count()
    dia5pe = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Pendiente").count()
    dia5pr = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="en Proveedor").count()
    dia5di= Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Directa").count()
    dia5fn = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Fin").count()
    dia5st = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Stock").count()
    dia5ll = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5).count()
    
    dia6oc = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="X asignar OC").count()
    dia6xr = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="X-Revisar").count()
    dia6re = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Revisado").count()
    dia6pe = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Pendiente").count()
    dia6pr = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="en Proveedor").count()
    dia6di = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Directa").count()
    dia6fn = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Fin").count()
    dia6st = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Stock").count()
    dia6ll = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6).count()
    
    dia7oc = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="X asignar OC").count()
    dia7xr = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="X-Revisar").count()
    dia7re = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Revisado").count()
    dia7pe = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Pendiente").count()
    dia7pr = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="en Proveedor").count()
    dia7di = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Directa").count()
    dia7fn = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Fin").count()
    dia7st = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Stock").count()
    dia7ll = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7).count()
    
    dia8oc = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="X asignar OC").count()
    dia8xr = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="X-Revisar").count()
    dia8re = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Revisado").count()
    dia8pe = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Pendiente").count()
    dia8pr = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="en Proveedor").count()
    dia8di = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Directa").count()
    dia8fn = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Fin").count()
    dia8st = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Stock").count()
    dia8ll = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8).count()

    diaoc = nan0([dia8oc, dia7oc, dia6oc, dia5oc, dia4oc, dia3oc, dia2oc, dia1oc, dia0oc])
    diaxr = nan0([dia8xr, dia7xr, dia6xr, dia5xr, dia4xr, dia3xr, dia2xr, dia1xr, dia0xr])
    diare = nan0([dia8re, dia7re, dia6re, dia5re, dia4re, dia3re, dia2re, dia1re, dia0re])
    diape = nan0([dia8pe, dia7pe, dia6pe, dia5pe, dia4pe, dia3pe, dia2pe, dia1pe, dia0pe])
    diapr = nan0([dia8pr, dia7pr, dia6pr, dia5pr, dia4pr, dia3pr, dia2pr, dia1pr, dia0pr])
    diadi = nan0([dia8di, dia7di, dia6di, dia5di, dia4di, dia3di, dia2di, dia1di, dia0di])
    diafn = nan0([dia8fn, dia7fn, dia6fn, dia5fn, dia4fn, dia3fn, dia2fn, dia1fn, dia0fn])
    diast = nan0([dia8st, dia7st, dia6st, dia5st, dia4st, dia3st, dia2st, dia1st, dia0st])
    diall = nan0([dia8ll, dia7ll, dia6ll, dia5ll, dia4ll, dia3ll, dia2ll, dia1ll, dia0ll])

    return {'pedidosstatus1':statusEn1,
            'pedidosstatus2':statusEn2,
            'pedidosstatus3':statusEn3,
            'pedidosstatus4':statusEn4,
            'pedidosstatusall': statusAll,
            'datagraph':datagraph,
            'diaoc' :diaoc,
            'diaxr' :diaxr,
            'diare' :diare,
            'diape' :diape,
            'diapr' :diapr,
            'diadi' :diadi,
            'diafn' :diafn,
            'diall' :diall,
            'diast' :diast,
            }

