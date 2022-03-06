from inv.models import Pedido

def pedidos_status(request):
    statusEn1 = Pedido.objects.filter(indentificador_estado=1).order_by('-id')[:999].count()
    statusEn2 = Pedido.objects.filter(indentificador_estado=2).order_by('-id')[:999].count()
    statusEn3 = Pedido.objects.filter(indentificador_estado=3).order_by('-id')[:999].count()
    statusEn4 = Pedido.objects.filter(indentificador_estado=4).order_by('-id')[:999].count()
    statusAll = statusEn1 +  statusEn2 + statusEn3 + statusEn4
    return {'pedidosstatus1':statusEn1, 'pedidosstatus2':statusEn2, 'pedidosstatus3':statusEn3, 'pedidosstatus4':statusEn4, 'pedidosstatusall': statusAll}
