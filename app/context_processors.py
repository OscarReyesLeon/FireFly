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
    
    fecha16 = fechahoy + timedelta(days=-16)
    dia16 = fecha16.strftime('%d')
    mes16 = fecha16.strftime('%m')
    ano16 = fecha16.strftime('%Y')
    
    fecha17 = fechahoy + timedelta(days=-17)
    dia17 = fecha17.strftime('%d')
    mes17 = fecha17.strftime('%m')
    ano17 = fecha17.strftime('%Y')
    
    fecha18 = fechahoy + timedelta(days=-18)
    dia18 = fecha18.strftime('%d')
    mes18 = fecha18.strftime('%m')
    ano18 = fecha18.strftime('%Y')
    
    fecha19 = fechahoy + timedelta(days=-19)
    dia19 = fecha19.strftime('%d')
    mes19 = fecha19.strftime('%m')
    ano19 = fecha19.strftime('%Y')
    
    fecha20 = fechahoy + timedelta(days=-20)
    dia20 = fecha20.strftime('%d')
    mes20 = fecha20.strftime('%m')
    ano20 = fecha20.strftime('%Y')
    
    fecha21 = fechahoy + timedelta(days=-21)
    dia21 = fecha21.strftime('%d')
    mes21 = fecha21.strftime('%m')
    ano21 = fecha21.strftime('%Y')

    fecha22 = fechahoy + timedelta(days=-22)
    dia22 = fecha22.strftime('%d')
    mes22 = fecha22.strftime('%m')
    ano22 = fecha22.strftime('%Y')
    
    fecha23 = fechahoy + timedelta(days=-23)
    dia23 = fecha23.strftime('%d')
    mes23 = fecha23.strftime('%m')
    ano23 = fecha23.strftime('%Y')
    
    fecha24 = fechahoy + timedelta(days=-24)
    dia24 = fecha24.strftime('%d')
    mes24 = fecha24.strftime('%m')
    ano24 = fecha24.strftime('%Y')
    
    fecha25 = fechahoy + timedelta(days=-25)
    dia25 = fecha25.strftime('%d')
    mes25 = fecha25.strftime('%m')
    ano25 = fecha25.strftime('%Y')
    
    fecha26 = fechahoy + timedelta(days=-26)
    dia26 = fecha26.strftime('%d')
    mes26 = fecha26.strftime('%m')
    ano26 = fecha26.strftime('%Y')
    
    fecha27 = fechahoy + timedelta(days=-27)
    dia27 = fecha27.strftime('%d')
    mes27 = fecha27.strftime('%m')
    ano27 = fecha27.strftime('%Y')
    
    fecha28 = fechahoy + timedelta(days=-28)
    dia28 = fecha28.strftime('%d')
    mes28 = fecha28.strftime('%m')
    ano28 = fecha28.strftime('%Y')
    
    fecha29 = fechahoy + timedelta(days=-29)
    dia29 = fecha29.strftime('%d')
    mes29 = fecha29.strftime('%m')
    ano29 = fecha29.strftime('%Y')
    
    fecha30 = fechahoy + timedelta(days=-30)
    dia30 = fecha30.strftime('%d')
    mes30 = fecha30.strftime('%m')
    ano30 = fecha30.strftime('%Y')
    
    fecha31 = fechahoy + timedelta(days=-31)
    dia31 = fecha31.strftime('%d')
    mes31 = fecha31.strftime('%m')
    ano31 = fecha31.strftime('%Y')

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
    
    dia16oc = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="X asignar OC").count()
    dia16xr = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="X-Revisar").count()
    dia16re = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="Revisado").count()
    dia16pe = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="Pendiente").count()
    dia16pr = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="en Proveedor").count()
    dia16di = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="Directo").count()
    dia16fn = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="Fin").count()
    dia16st = Pedido.objects.filter(fc__year=ano16,fc__month=mes16,fc__day=dia16,status="Stock").count()
    dia16ll = int(dia16oc) + int(dia16xr) + int(dia16re) + int(dia16pe) + int(dia16pr) + int(dia16di) + int(dia16fn) + int(dia16st)
    dia16ll = str(dia16ll)
    dia16ob = str(int(dia16fn) + int(dia16di) + int(dia16st))
    
    dia17oc = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="X asignar OC").count()
    dia17xr = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="X-Revisar").count()
    dia17re = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="Revisado").count()
    dia17pe = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="Pendiente").count()
    dia17pr = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="en Proveedor").count()
    dia17di = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="Directo").count()
    dia17fn = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="Fin").count()
    dia17st = Pedido.objects.filter(fc__year=ano17,fc__month=mes17,fc__day=dia17,status="Stock").count()
    dia17ll = int(dia17oc) + int(dia17xr) + int(dia17re) + int(dia17pe) + int(dia17pr) + int(dia17di) + int(dia17fn) + int(dia17st)
    dia17ll = str(dia17ll)
    dia17ob = str(int(dia17fn) + int(dia17di) + int(dia17st))
    
    dia18oc = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="X asignar OC").count()
    dia18xr = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="X-Revisar").count()
    dia18re = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="Revisado").count()
    dia18pe = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="Pendiente").count()
    dia18pr = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="en Proveedor").count()
    dia18di = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="Directo").count()
    dia18fn = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="Fin").count()
    dia18st = Pedido.objects.filter(fc__year=ano18,fc__month=mes18,fc__day=dia18,status="Stock").count()
    dia18ll = int(dia18oc) + int(dia18xr) + int(dia18re) + int(dia18pe) + int(dia18pr) + int(dia18di) + int(dia18fn) + int(dia18st)
    dia18ll = str(dia18ll)
    dia18ob = str(int(dia18fn) + int(dia18di) + int(dia18st))
    
    dia19oc = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="X asignar OC").count()
    dia19xr = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="X-Revisar").count()
    dia19re = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="Revisado").count()
    dia19pe = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="Pendiente").count()
    dia19pr = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="en Proveedor").count()
    dia19di = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="Directo").count()
    dia19fn = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="Fin").count()
    dia19st = Pedido.objects.filter(fc__year=ano19,fc__month=mes19,fc__day=dia19,status="Stock").count()
    dia19ll = int(dia19oc) + int(dia19xr) + int(dia19re) + int(dia19pe) + int(dia19pr) + int(dia19di) + int(dia19fn) + int(dia19st)
    dia19ll = str(dia19ll)
    dia19ob = str(int(dia19fn) + int(dia19di) + int(dia19st))
    
    dia20oc = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="X asignar OC").count()
    dia20xr = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="X-Revisar").count()
    dia20re = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="Revisado").count()
    dia20pe = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="Pendiente").count()
    dia20pr = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="en Proveedor").count()
    dia20di = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="Directo").count()
    dia20fn = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="Fin").count()
    dia20st = Pedido.objects.filter(fc__year=ano20,fc__month=mes20,fc__day=dia20,status="Stock").count()
    dia20ll = int(dia20oc) + int(dia20xr) + int(dia20re) + int(dia20pe) + int(dia20pr) + int(dia20di) + int(dia20fn) + int(dia20st)
    dia20ll = str(dia20ll)
    dia20ob = str(int(dia20fn) + int(dia20di) + int(dia20st))
    
    dia21oc = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="X asignar OC").count()
    dia21xr = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="X-Revisar").count()
    dia21re = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="Revisado").count()
    dia21pe = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="Pendiente").count()
    dia21pr = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="en Proveedor").count()
    dia21di = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="Directo").count()
    dia21fn = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="Fin").count()
    dia21st = Pedido.objects.filter(fc__year=ano21,fc__month=mes21,fc__day=dia21,status="Stock").count()
    dia21ll = int(dia21oc) + int(dia21xr) + int(dia21re) + int(dia21pe) + int(dia21pr) + int(dia21di) + int(dia21fn) + int(dia21st)
    dia21ll = str(dia21ll)
    dia21ob = str(int(dia21fn) + int(dia21di) + int(dia21st))
    
    dia22oc = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="X asignar OC").count()
    dia22xr = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="X-Revisar").count()
    dia22re = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="Revisado").count()
    dia22pe = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="Pendiente").count()
    dia22pr = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="en Proveedor").count()
    dia22di = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="Directo").count()
    dia22fn = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="Fin").count()
    dia22st = Pedido.objects.filter(fc__year=ano22,fc__month=mes22,fc__day=dia22,status="Stock").count()
    dia22ll = int(dia22oc) + int(dia22xr) + int(dia22re) + int(dia22pe) + int(dia22pr) + int(dia22di) + int(dia22fn) + int(dia22st)
    dia22ll = str(dia22ll)
    dia22ob = str(int(dia22fn) + int(dia22di) + int(dia22st))
    
    dia23oc = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="X asignar OC").count()
    dia23xr = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="X-Revisar").count()
    dia23re = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="Revisado").count()
    dia23pe = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="Pendiente").count()
    dia23pr = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="en Proveedor").count()
    dia23di = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="Directo").count()
    dia23fn = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="Fin").count()
    dia23st = Pedido.objects.filter(fc__year=ano23,fc__month=mes23,fc__day=dia23,status="Stock").count()
    dia23ll = int(dia23oc) + int(dia23xr) + int(dia23re) + int(dia23pe) + int(dia23pr) + int(dia23di) + int(dia23fn) + int(dia23st)
    dia23ll = str(dia23ll)
    dia23ob = str(int(dia23fn) + int(dia23di) + int(dia23st))
    
    dia24oc = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="X asignar OC").count()
    dia24xr = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="X-Revisar").count()
    dia24re = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="Revisado").count()
    dia24pe = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="Pendiente").count()
    dia24pr = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="en Proveedor").count()
    dia24di = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="Directo").count()
    dia24fn = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="Fin").count()
    dia24st = Pedido.objects.filter(fc__year=ano24,fc__month=mes24,fc__day=dia24,status="Stock").count()
    dia24ll = int(dia24oc) + int(dia24xr) + int(dia24re) + int(dia24pe) + int(dia24pr) + int(dia24di) + int(dia24fn) + int(dia24st)
    dia24ll = str(dia24ll)
    dia24ob = str(int(dia24fn) + int(dia24di) + int(dia24st))
    
    dia25oc = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="X asignar OC").count()
    dia25xr = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="X-Revisar").count()
    dia25re = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="Revisado").count()
    dia25pe = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="Pendiente").count()
    dia25pr = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="en Proveedor").count()
    dia25di = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="Directo").count()
    dia25fn = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="Fin").count()
    dia25st = Pedido.objects.filter(fc__year=ano25,fc__month=mes25,fc__day=dia25,status="Stock").count()
    dia25ll = int(dia25oc) + int(dia25xr) + int(dia25re) + int(dia25pe) + int(dia25pr) + int(dia25di) + int(dia25fn) + int(dia25st)
    dia25ll = str(dia25ll)
    dia25ob = str(int(dia25fn) + int(dia25di) + int(dia25st))
    
    dia26oc = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="X asignar OC").count()
    dia26xr = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="X-Revisar").count()
    dia26re = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="Revisado").count()
    dia26pe = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="Pendiente").count()
    dia26pr = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="en Proveedor").count()
    dia26di = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="Directo").count()
    dia26fn = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="Fin").count()
    dia26st = Pedido.objects.filter(fc__year=ano26,fc__month=mes26,fc__day=dia26,status="Stock").count()
    dia26ll = int(dia26oc) + int(dia26xr) + int(dia26re) + int(dia26pe) + int(dia26pr) + int(dia26di) + int(dia26fn) + int(dia26st)
    dia26ll = str(dia26ll)
    dia26ob = str(int(dia26fn) + int(dia26di) + int(dia26st))
    
    dia27oc = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="X asignar OC").count()
    dia27xr = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="X-Revisar").count()
    dia27re = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="Revisado").count()
    dia27pe = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="Pendiente").count()
    dia27pr = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="en Proveedor").count()
    dia27di = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="Directo").count()
    dia27fn = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="Fin").count()
    dia27st = Pedido.objects.filter(fc__year=ano27,fc__month=mes27,fc__day=dia27,status="Stock").count()
    dia27ll = int(dia27oc) + int(dia27xr) + int(dia27re) + int(dia27pe) + int(dia27pr) + int(dia27di) + int(dia27fn) + int(dia27st)
    dia27ll = str(dia27ll)
    dia27ob = str(int(dia27fn) + int(dia27di) + int(dia27st))
    
    dia28oc = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="X asignar OC").count()
    dia28xr = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="X-Revisar").count()
    dia28re = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="Revisado").count()
    dia28pe = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="Pendiente").count()
    dia28pr = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="en Proveedor").count()
    dia28di = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="Directo").count()
    dia28fn = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="Fin").count()
    dia28st = Pedido.objects.filter(fc__year=ano28,fc__month=mes28,fc__day=dia28,status="Stock").count()
    dia28ll = int(dia28oc) + int(dia28xr) + int(dia28re) + int(dia28pe) + int(dia28pr) + int(dia28di) + int(dia28fn) + int(dia28st)
    dia28ll = str(dia28ll)
    dia28ob = str(int(dia28fn) + int(dia28di) + int(dia28st))
    
    dia29oc = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="X asignar OC").count()
    dia29xr = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="X-Revisar").count()
    dia29re = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="Revisado").count()
    dia29pe = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="Pendiente").count()
    dia29pr = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="en Proveedor").count()
    dia29di = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="Directo").count()
    dia29fn = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="Fin").count()
    dia29st = Pedido.objects.filter(fc__year=ano29,fc__month=mes29,fc__day=dia29,status="Stock").count()
    dia29ll = int(dia29oc) + int(dia29xr) + int(dia29re) + int(dia29pe) + int(dia29pr) + int(dia29di) + int(dia29fn) + int(dia29st)
    dia29ll = str(dia29ll)
    dia29ob = str(int(dia29fn) + int(dia29di) + int(dia29st))
    
    dia30oc = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="X asignar OC").count()
    dia30xr = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="X-Revisar").count()
    dia30re = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="Revisado").count()
    dia30pe = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="Pendiente").count()
    dia30pr = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="en Proveedor").count()
    dia30di = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="Directo").count()
    dia30fn = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="Fin").count()
    dia30st = Pedido.objects.filter(fc__year=ano30,fc__month=mes30,fc__day=dia30,status="Stock").count()
    dia30ll = int(dia30oc) + int(dia30xr) + int(dia30re) + int(dia30pe) + int(dia30pr) + int(dia30di) + int(dia30fn) + int(dia30st)
    dia30ll = str(dia30ll)
    dia30ob = str(int(dia30fn) + int(dia30di) + int(dia30st))
    
    dia31oc = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="X asignar OC").count()
    dia31xr = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="X-Revisar").count()
    dia31re = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="Revisado").count()
    dia31pe = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="Pendiente").count()
    dia31pr = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="en Proveedor").count()
    dia31di = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="Directo").count()
    dia31fn = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="Fin").count()
    dia31st = Pedido.objects.filter(fc__year=ano31,fc__month=mes31,fc__day=dia31,status="Stock").count()
    dia31ll = int(dia31oc) + int(dia31xr) + int(dia31re) + int(dia31pe) + int(dia31pr) + int(dia31di) + int(dia31fn) + int(dia31st)
    dia31ll = str(dia31ll)
    dia31ob = str(int(dia31fn) + int(dia31di) + int(dia31st))

    
    diaoc = nan0([dia31oc, dia30oc, dia29oc, dia28oc, dia27oc, dia26oc, dia25oc, dia24oc, dia23oc, dia22oc, dia21oc, dia20oc, dia19oc, dia18oc, dia17oc, dia16oc, dia15oc, dia14oc, dia13oc, dia12oc, dia11oc, dia10oc, dia9oc, dia8oc, dia7oc, dia6oc, dia5oc, dia4oc, dia3oc, dia2oc, dia1oc, dia0oc])
    diaxr = nan0([dia31xr, dia30xr, dia29xr, dia28xr, dia27xr, dia26xr, dia25xr, dia24xr, dia23xr, dia22xr, dia21xr, dia20xr, dia19xr, dia18xr, dia17xr, dia16xr, dia15xr, dia14xr, dia13xr, dia12xr, dia11xr, dia10xr, dia9xr, dia8xr, dia7xr, dia6xr, dia5xr, dia4xr, dia3xr, dia2xr, dia1xr, dia0xr])
    diare = nan0([dia31re, dia30re, dia29re, dia28re, dia27re, dia26re, dia25re, dia24re, dia23re, dia22re, dia21re, dia20re, dia19re, dia18re, dia17re, dia16re, dia15re, dia14re, dia13re, dia12re, dia11re, dia10re, dia9re, dia8re, dia7re, dia6re, dia5re, dia4re, dia3re, dia2re, dia1re, dia0re])
    diape = nan0([dia31pe, dia30pe, dia29pe, dia28pe, dia27pe, dia26pe, dia25pe, dia24pe, dia23pe, dia22pe, dia21pe, dia20pe, dia19pe, dia18pe, dia17pe, dia16pe, dia15pe, dia14pe, dia13pe, dia12pe, dia11pe, dia10pe, dia9pe, dia8pe, dia7pe, dia6pe, dia5pe, dia4pe, dia3pe, dia2pe, dia1pe, dia0pe])
    diapr = nan0([dia31pr, dia30pr, dia29pr, dia28pr, dia27pr, dia26pr, dia25pr, dia24pr, dia23pr, dia22pr, dia21pr, dia20pr, dia19pr, dia18pr, dia17pr, dia16pr, dia15pr, dia14pr, dia13pr, dia12pr, dia11pr, dia10pr, dia9pr, dia8pr, dia7pr, dia6pr, dia5pr, dia4pr, dia3pr, dia2pr, dia1pr, dia0pr])
    diadi = nan0([dia31di, dia30di, dia29di, dia28di, dia27di, dia26di, dia25di, dia24di, dia23di, dia22di, dia21di, dia20di, dia19di, dia18di, dia17di, dia16di, dia15di, dia14di, dia13di, dia12di, dia11di, dia10di, dia9di, dia8di, dia7di, dia6di, dia5di, dia4di, dia3di, dia2di, dia1di, dia0di])
    diafn = nan0([dia31fn, dia30fn, dia29fn, dia28fn, dia27fn, dia26fn, dia25fn, dia24fn, dia23fn, dia22fn, dia21fn, dia20fn, dia19fn, dia18fn, dia17fn, dia16fn, dia15fn, dia14fn, dia13fn, dia12fn, dia11fn, dia10fn, dia9fn, dia8fn, dia7fn, dia6fn, dia5fn, dia4fn, dia3fn, dia2fn, dia1fn, dia0fn])
    diast = nan0([dia31st, dia30st, dia29st, dia28st, dia27st, dia26st, dia25st, dia24st, dia23st, dia22st, dia21st, dia20st, dia19st, dia18st, dia17st, dia16st, dia15st, dia14st, dia13st, dia12st, dia11st, dia10st, dia9st, dia8st, dia7st, dia6st, dia5st, dia4st, dia3st, dia2st, dia1st, dia0st])
    diall = nan0([dia31ll, dia30ll, dia29ll, dia28ll, dia27ll, dia26ll, dia25ll, dia24ll, dia23ll, dia22ll, dia21ll, dia20ll, dia19ll, dia18ll, dia17ll, dia16ll, dia15ll, dia14ll, dia13ll, dia12ll, dia11ll, dia10ll, dia9ll, dia8ll, dia7ll, dia6ll, dia5ll, dia4ll, dia3ll, dia2ll, dia1ll, dia0ll])
    diaob = nan0([dia31ob, dia30ob, dia29ob, dia28ob, dia27ob, dia26ob, dia25ob, dia24ob, dia23ob, dia22ob, dia21ob, dia20ob, dia19ob, dia18ob, dia17ob, dia16ob, dia15ob, dia14ob, dia13ob, dia12ob, dia11ob, dia10ob, dia9ob, dia8ob, dia7ob, dia6ob, dia5ob, dia4ob, dia3ob, dia2ob, dia1ob, dia0ob])


    fechahoydate = fechahoy.date()
    fechaa32 = fechahoy + timedelta(days=-32)
    abiertos = Pedido.objects.filter(indentificador_estado=1).order_by('-id')[:2000] | Pedido.objects.filter(indentificador_estado=2).order_by('-id')[:2000] | Pedido.objects.filter(indentificador_estado=3).order_by('-id')[:2000] | Pedido.objects.filter(indentificador_estado=4).order_by('-id')[:2000]
    todosenrango = Pedido.objects.filter(fc__range=(fechaa32, fechahoydate)).filter(status="Directo") | Pedido.objects.filter(fc__range=(fechaa32, fechahoydate)).filter(status="Fin")
    print(todosenrango.count())

    tiempospendientes = []
    for i in range(abiertos.count()):
        objetospendientes = abiertos[i]
        objetospendientes = objetospendientes.fc.date()
        objetospendientes = objetospendientes
        tiempospendientes.append(objetospendientes)

    diaspromedio = 0
    for i in range(len(tiempospendientes)):
        diaspromedio = diaspromedio + (fechahoydate - tiempospendientes[i]).days
    diaspromedio = round(diaspromedio / len(tiempospendientes),1)



    pini32 = []
    pfin32 = []
    for i in range(todosenrango.count()):
        objetospendientes = todosenrango[i]
        pinip32 = objetospendientes.fc.strftime('%d-%m-%y %H:%M')
        pfinp32 = objetospendientes.fecha_finalizado
        pinip32 = datetime.strptime(pinip32, '%d-%m-%y %H:%M')
        pfinp32 = datetime.strptime(pfinp32, '%d-%m-%y %H:%M')
        pini32.append(pinip32)
        pfin32.append(pfinp32)

    promedio32 = 0
    for i in range(len(pfin32)):
        promedio32 = promedio32 + (pfin32[i] - pini32[i]).days
    
    promedio32 = round(promedio32 / len(pfin32),1)



    if (promedio32 > 5) and (promedio32 <= 10):
        diascolor = "text-dark"
    elif promedio32 <= 5:
        diascolor = "text-info"
    else:
        diascolor = "text-danger"



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
            'diaspromedio':diaspromedio,
            'diascolor' :diascolor,
            'promedio32' : promedio32,
            }

