from django.urls import path, include

from .views import ProveedorView,ProveedorNew, ProveedorEdit, \
    proveedorInactivar, \
    ComprasView, compras, CompraDetDelete

from .reportes import reporte_compras, imprimir_compra

urlpatterns = [
    path('proveedores/',ProveedorView.as_view(), name="proveedor_list"),
    path('proveedores/new',ProveedorNew.as_view(), name="proveedor_new"),
    path('proveedores/edit/<int:pk>',ProveedorEdit.as_view(), name="proveedor_edit"),
    path('proveedores/inactivar/<int:id>',proveedorInactivar, name="proveedor_inactivar"),

    path('ordencompra/',ComprasView.as_view(), name="compras_list"),
    path('ordencompra/new',compras, name="compras_new"),
    path('ordencompra/edit/<int:compra_id>',compras, name="compras_edit"),
    path('ordencompra/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),

    path('ordencompra/listado', reporte_compras, name='compras_print_all'),
    path('ordencompra/<int:compra_id>/imprimir', imprimir_compra,name="compras_print_one"),
]