from django.urls import path, include

from .views import ProveedorView,ProveedorNew, ProveedorEdit, \
    proveedorInactivar, \
        UsoFacturaView,UsoFacturaNew, UsoFacturaEdit, \
    UsoFacturaInactivar, \
    ComprasView, compras, CompraDetDelete, OC_autoALS, Cierre_OC

from .reportes import reporte_compras, imprimir_compra, imprimir_compra2, imprimir_compra3

urlpatterns = [
    path('proveedores/',ProveedorView.as_view(), name="proveedor_list"),
    path('proveedores/new',ProveedorNew.as_view(), name="proveedor_new"),
    path('proveedores/edit/<int:pk>',ProveedorEdit.as_view(), name="proveedor_edit"),
    path('proveedores/inactivar/<int:id>',proveedorInactivar, name="proveedor_inactivar"),

    path('usofactura/',UsoFacturaView.as_view(), name="usofactura_list"),
    path('usofactura/new',UsoFacturaNew.as_view(), name="usofactura_new"),
    path('usofactura/edit/<int:pk>',UsoFacturaEdit.as_view(), name="usofactura_edit"),
    path('usofactura/inactivar/<int:id>',UsoFacturaInactivar, name="usofactura_inactivar"),


    path('ordencompra/',ComprasView.as_view(), name="compras_list"),
    path('ordencompra/autals/<int:id>',OC_autoALS, name="autoALS"),
    path('ordencompra/cierreoc/<int:id>',Cierre_OC, name="Cierre_OC"),
    path('ordencompra/new',compras, name="compras_new"),
    path('ordencompra/edit/<int:compra_id>',compras, name="compras_edit"),
    path('ordencompra/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),

    path('ordencompra/listado', reporte_compras, name='compras_print_all'),
    path('ordencompra/<int:compra_id>/imprimir', imprimir_compra,name="compras_print_one"),
    path('ordencompra/<slug:clienteuniqueid>/oc', imprimir_compra2,name="compras_print_client"),
    path('ordencompra/<slug:clienteuniqueid>/ocold', imprimir_compra3,name="compras_print_three"),

]