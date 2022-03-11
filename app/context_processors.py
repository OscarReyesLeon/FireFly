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
    
    fecha9 = fechahoy + timedelta(days=-9)
    dia9 = fecha9.strftime('%d')
    mes9 = fecha9.strftime('%m')
    ano9 = fecha9.strftime('%Y')
    
    fecha10 = fechahoy + timedelta(days=-10)
    dia10 = fecha10.strftime('%d')
    mes10 = fecha10.strftime('%m')
    ano10 = fecha10.strftime('%Y')
    
    fecha11 = fechahoy + timedelta(days=-11)
    dia11 = fecha11.strftime('%d')
    mes11 = fecha11.strftime('%m')
    ano11 = fecha11.strftime('%Y')
    
    fecha12 = fechahoy + timedelta(days=-12)
    dia12 = fecha12.strftime('%d')
    mes12 = fecha12.strftime('%m')
    ano12 = fecha12.strftime('%Y')
    
    fecha13 = fechahoy + timedelta(days=-13)
    dia13 = fecha13.strftime('%d')
    mes13 = fecha13.strftime('%m')
    ano13 = fecha13.strftime('%Y')
    
    fecha14 = fechahoy + timedelta(days=-14)
    dia14 = fecha14.strftime('%d')
    mes14 = fecha14.strftime('%m')
    ano14 = fecha14.strftime('%Y')
    
    fecha15 = fechahoy + timedelta(days=-15)
    dia15 = fecha15.strftime('%d')
    mes15 = fecha15.strftime('%m')
    ano15 = fecha15.strftime('%Y')
    
    dia0oc = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="X asignar OC").count()
    dia0xr = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="X-Revisar").count()
    dia0re = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Revisado").count()
    dia0pe = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Pendiente").count()
    dia0pr = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="en Proveedor").count()
    dia0di = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Directo").count()
    dia0fn = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Fin").count()
    dia0st = Pedido.objects.filter(fc__year=anohoy,fc__month=meshoy,fc__day=diahoy,status="Stock").count()
    dia0ll = str(int(dia0oc) + int(dia0xr) + int(dia0re) + int(dia0pe) + int(dia0pr) + int(dia0di) + int(dia0fn) + int(dia0st))
    dia0ob = str(int(dia0fn) + int(dia0di) + int(dia0st))
    
    dia1oc = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="X asignar OC").count()
    dia1xr = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="X-Revisar").count()
    dia1re = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Revisado").count()
    dia1pe = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Pendiente").count()
    dia1pr = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="en Proveedor").count()
    dia1di = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Directo").count()
    dia1fn = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Fin").count()
    dia1st = Pedido.objects.filter(fc__year=ano1,fc__month=mes1,fc__day=dia1,status="Stock").count()
    dia1ll = int(dia1oc) + int(dia1xr) + int(dia1re) + int(dia1pe) + int(dia1pr) + int(dia1di) + int(dia1fn) + int(dia1st)
    dia1ll = str(dia1ll)
    dia1ob = str(int(dia1fn) + int(dia1di) + int(dia1st))
    
    dia2oc = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="X asignar OC").count()
    dia2xr = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="X-Revisar").count()
    dia2re = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Revisado").count()
    dia2pe = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Pendiente").count()
    dia2pr = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="en Proveedor").count()
    dia2di = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Directo").count()
    dia2fn = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Fin").count()
    dia2st = Pedido.objects.filter(fc__year=ano2,fc__month=mes2,fc__day=dia2,status="Stock").count()
    dia2ll = int(dia2oc) + int(dia2xr) + int(dia2re) + int(dia2pe) + int(dia2pr) + int(dia2di) + int(dia2fn) + int(dia2st)
    dia2ll = str(dia2ll)
    dia2ob = str(int(dia2fn) + int(dia2di) + int(dia2st))
    
    
    dia3oc = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="X asignar OC").count()
    dia3xr = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="X-Revisar").count()
    dia3re = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Revisado").count()
    dia3pe = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Pendiente").count()
    dia3pr = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="en Proveedor").count()
    dia3di = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Directo").count()
    dia3fn = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Fin").count()
    dia3st = Pedido.objects.filter(fc__year=ano3,fc__month=mes3,fc__day=dia3,status="Stock").count()
    dia3ll = int(dia3oc) + int(dia3xr) + int(dia3re) + int(dia3pe) + int(dia3pr) + int(dia3di) + int(dia3fn) + int(dia3st)
    dia3ll = str(dia3ll)
    dia3ob = str(int(dia3fn) + int(dia3di) + int(dia3st))
    
    dia4oc = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="X asignar OC").count()
    dia4xr = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="X-Revisar").count()
    dia4re = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Revisado").count()
    dia4pe = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Pendiente").count()
    dia4pr = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="en Proveedor").count()
    dia4di = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Directo").count()
    dia4fn = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Fin").count()
    dia4st = Pedido.objects.filter(fc__year=ano4,fc__month=mes4,fc__day=dia4,status="Stock").count()
    dia4ll = int(dia4oc) + int(dia4xr) + int(dia4re) + int(dia4pe) + int(dia4pr) + int(dia4di) + int(dia4fn) + int(dia4st)
    dia4ll = str(dia4ll)
    dia4ob = str(int(dia4fn) + int(dia4di) + int(dia4st))
    
    dia5oc = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="X asignar OC").count()
    dia5xr = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="X-Revisar").count()
    dia5re = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Revisado").count()
    dia5pe = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Pendiente").count()
    dia5pr = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="en Proveedor").count()
    dia5di= Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Directo").count()
    dia5fn = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Fin").count()
    dia5st = Pedido.objects.filter(fc__year=ano5,fc__month=mes5,fc__day=dia5,status="Stock").count()
    dia5ll = int(dia5oc) + int(dia5xr) + int(dia5re) + int(dia5pe) + int(dia5pr) + int(dia5di) + int(dia5fn) + int(dia5st)
    dia5ll = str(dia5ll)
    dia5ob = str(int(dia5fn) + int(dia5di) + int(dia5st))
    
    dia6oc = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="X asignar OC").count()
    dia6xr = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="X-Revisar").count()
    dia6re = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Revisado").count()
    dia6pe = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Pendiente").count()
    dia6pr = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="en Proveedor").count()
    dia6di = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Directo").count()
    dia6fn = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Fin").count()
    dia6st = Pedido.objects.filter(fc__year=ano6,fc__month=mes6,fc__day=dia6,status="Stock").count()
    dia6ll = int(dia6oc) + int(dia6xr) + int(dia6re) + int(dia6pe) + int(dia6pr) + int(dia6di) + int(dia6fn) + int(dia6st)
    dia6ll = str(dia6ll)
    dia6ob = str(int(dia6fn) + int(dia6di) + int(dia6st))
    
    dia7oc = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="X asignar OC").count()
    dia7xr = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="X-Revisar").count()
    dia7re = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Revisado").count()
    dia7pe = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Pendiente").count()
    dia7pr = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="en Proveedor").count()
    dia7di = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Directo").count()
    dia7fn = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Fin").count()
    dia7st = Pedido.objects.filter(fc__year=ano7,fc__month=mes7,fc__day=dia7,status="Stock").count()
    dia7ll = int(dia7oc) + int(dia7xr) + int(dia7re) + int(dia7pe) + int(dia7pr) + int(dia7di) + int(dia7fn) + int(dia7st)
    dia7ll = str(dia7ll)
    dia7ob = str(int(dia7fn) + int(dia7di) + int(dia7st))
    
    dia8oc = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="X asignar OC").count()
    dia8xr = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="X-Revisar").count()
    dia8re = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Revisado").count()
    dia8pe = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Pendiente").count()
    dia8pr = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="en Proveedor").count()
    dia8di = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Directo").count()
    dia8fn = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Fin").count()
    dia8st = Pedido.objects.filter(fc__year=ano8,fc__month=mes8,fc__day=dia8,status="Stock").count()
    dia8ll = int(dia8oc) + int(dia8xr) + int(dia8re) + int(dia8pe) + int(dia8pr) + int(dia8di) + int(dia8fn) + int(dia8st)
    dia8ll = str(dia8ll)
    dia8ob = str(int(dia8fn) + int(dia8di) + int(dia8st))
    
    dia9oc = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="X asignar OC").count()
    dia9xr = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="X-Revisar").count()
    dia9re = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="Revisado").count()
    dia9pe = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="Pendiente").count()
    dia9pr = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="en Proveedor").count()
    dia9di = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="Directo").count()
    dia9fn = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="Fin").count()
    dia9st = Pedido.objects.filter(fc__year=ano9,fc__month=mes9,fc__day=dia9,status="Stock").count()
    dia9ll = int(dia9oc) + int(dia9xr) + int(dia9re) + int(dia9pe) + int(dia9pr) + int(dia9di) + int(dia9fn) + int(dia9st)
    dia9ll = str(dia9ll)
    dia9ob = str(int(dia9fn) + int(dia9di) + int(dia9st))
    
    dia10oc = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="X asignar OC").count()
    dia10xr = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="X-Revisar").count()
    dia10re = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="Revisado").count()
    dia10pe = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="Pendiente").count()
    dia10pr = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="en Proveedor").count()
    dia10di = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="Directo").count()
    dia10fn = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="Fin").count()
    dia10st = Pedido.objects.filter(fc__year=ano10,fc__month=mes10,fc__day=dia10,status="Stock").count()
    dia10ll = int(dia10oc) + int(dia10xr) + int(dia10re) + int(dia10pe) + int(dia10pr) + int(dia10di) + int(dia10fn) + int(dia10st)
    dia10ll = str(dia10ll)
    dia10ob = str(int(dia10fn) + int(dia10di) + int(dia10st))
    
    dia11oc = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="X asignar OC").count()
    dia11xr = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="X-Revisar").count()
    dia11re = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="Revisado").count()
    dia11pe = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="Pendiente").count()
    dia11pr = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="en Proveedor").count()
    dia11di = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="Directo").count()
    dia11fn = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="Fin").count()
    dia11st = Pedido.objects.filter(fc__year=ano11,fc__month=mes11,fc__day=dia11,status="Stock").count()
    dia11ll = int(dia11oc) + int(dia11xr) + int(dia11re) + int(dia11pe) + int(dia11pr) + int(dia11di) + int(dia11fn) + int(dia11st)
    dia11ll = str(dia11ll)
    dia11ob = str(int(dia11fn) + int(dia11di) + int(dia11st))
    
    dia12oc = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="X asignar OC").count()
    dia12xr = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="X-Revisar").count()
    dia12re = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="Revisado").count()
    dia12pe = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="Pendiente").count()
    dia12pr = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="en Proveedor").count()
    dia12di = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="Directo").count()
    dia12fn = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="Fin").count()
    dia12st = Pedido.objects.filter(fc__year=ano12,fc__month=mes12,fc__day=dia12,status="Stock").count()
    dia12ll = int(dia12oc) + int(dia12xr) + int(dia12re) + int(dia12pe) + int(dia12pr) + int(dia12di) + int(dia12fn) + int(dia12st)
    dia12ll = str(dia12ll)
    dia12ob = str(int(dia12fn) + int(dia12di) + int(dia12st))
    
    dia13oc = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="X asignar OC").count()
    dia13xr = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="X-Revisar").count()
    dia13re = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="Revisado").count()
    dia13pe = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="Pendiente").count()
    dia13pr = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="en Proveedor").count()
    dia13di = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="Directo").count()
    dia13fn = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="Fin").count()
    dia13st = Pedido.objects.filter(fc__year=ano13,fc__month=mes13,fc__day=dia13,status="Stock").count()
    dia13ll = int(dia13oc) + int(dia13xr) + int(dia13re) + int(dia13pe) + int(dia13pr) + int(dia13di) + int(dia13fn) + int(dia13st)
    dia13ll = str(dia13ll)
    dia13ob = str(int(dia13fn) + int(dia13di) + int(dia13st))
    
    dia14oc = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="X asignar OC").count()
    dia14xr = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="X-Revisar").count()
    dia14re = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="Revisado").count()
    dia14pe = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="Pendiente").count()
    dia14pr = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="en Proveedor").count()
    dia14di = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="Directo").count()
    dia14fn = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="Fin").count()
    dia14st = Pedido.objects.filter(fc__year=ano14,fc__month=mes14,fc__day=dia14,status="Stock").count()
    dia14ll = int(dia14oc) + int(dia14xr) + int(dia14re) + int(dia14pe) + int(dia14pr) + int(dia14di) + int(dia14fn) + int(dia14st)
    dia14ll = str(dia14ll)
    dia14ob = str(int(dia14fn) + int(dia14di) + int(dia14st))
    
    dia15oc = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="X asignar OC").count()
    dia15xr = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="X-Revisar").count()
    dia15re = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="Revisado").count()
    dia15pe = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="Pendiente").count()
    dia15pr = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="en Proveedor").count()
    dia15di = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="Directo").count()
    dia15fn = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="Fin").count()
    dia15st = Pedido.objects.filter(fc__year=ano15,fc__month=mes15,fc__day=dia15,status="Stock").count()
    dia15ll = int(dia15oc) + int(dia15xr) + int(dia15re) + int(dia15pe) + int(dia15pr) + int(dia15di) + int(dia15fn) + int(dia15st)
    dia15ll = str(dia15ll)
    dia15ob = str(int(dia15fn) + int(dia15di) + int(dia15st))
    
    diaoc = nan0([dia15oc, dia14oc, dia13oc, dia12oc, dia11oc, dia10oc, dia9oc, dia8oc, dia7oc, dia6oc, dia5oc, dia4oc, dia3oc, dia2oc, dia1oc, dia0oc])
    diaxr = nan0([dia15xr, dia14xr, dia13xr, dia12xr, dia11xr, dia10xr, dia9xr, dia8xr, dia7xr, dia6xr, dia5xr, dia4xr, dia3xr, dia2xr, dia1xr, dia0xr])
    diare = nan0([dia15re, dia14re, dia13re, dia12re, dia11re, dia10re, dia9re, dia8re, dia7re, dia6re, dia5re, dia4re, dia3re, dia2re, dia1re, dia0re])
    diape = nan0([dia15pe, dia14pe, dia13pe, dia12pe, dia11pe, dia10pe, dia9pe, dia8pe, dia7pe, dia6pe, dia5pe, dia4pe, dia3pe, dia2pe, dia1pe, dia0pe])
    diapr = nan0([dia15pr, dia14pr, dia13pr, dia12pr, dia11pr, dia10pr, dia9pr, dia8pr, dia7pr, dia6pr, dia5pr, dia4pr, dia3pr, dia2pr, dia1pr, dia0pr])
    diadi = nan0([dia15di, dia14di, dia13di, dia12di, dia11di, dia10di, dia9di, dia8di, dia7di, dia6di, dia5di, dia4di, dia3di, dia2di, dia1di, dia0di])
    diafn = nan0([dia15fn, dia14fn, dia13fn, dia12fn, dia11fn, dia10fn, dia9fn, dia8fn, dia7fn, dia6fn, dia5fn, dia4fn, dia3fn, dia2fn, dia1fn, dia0fn])
    diast = nan0([dia15st, dia14st, dia13st, dia12st, dia11st, dia10st, dia9st, dia8st, dia7st, dia6st, dia5st, dia4st, dia3st, dia2st, dia1st, dia0st])
    diall = nan0([dia15ll, dia14ll, dia13ll, dia12ll, dia11ll, dia10ll, dia9ll, dia8ll, dia7ll, dia6ll, dia5ll, dia4ll, dia3ll, dia2ll, dia1ll, dia0ll])
    diaob = nan0([dia15ob, dia14ob, dia13ob, dia12ob, dia11ob, dia10ob, dia9ob, dia8ob, dia7ob, dia6ob, dia5ob, dia4ob, dia3ob, dia2ob, dia1ob, dia0ob])

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
            'diaob' :diaob,
            }

