from django.urls import path, include

from .views import ProveedorView,ProveedorNew, ProveedorEdit, \
    proveedorInactivar, comprasALR, \
        UsoFacturaView,UsoFacturaNew, UsoFacturaEdit, \
    UsoFacturaInactivar, \
    ComprasView, ComprasViewO, ComprasViewP, ComprasViewA, ComprasViewG, ComprasViewM,\
    ComprasViewCXP,\
    comprasOficina, comprasPlanta, CompraDetDelete, \
    EnviarAutALR, EnviarAutLedsaOfi, EnviarAutLedsaPlanta,  \
    AutorizarOCALS, AutorizarOCGLS, AutorizarOCMLS, Provisionar, ComprasViewALR, \
    AutorizarOCReciclarA, AutorizarOCReciclarG, AutorizarOCReciclarM, AutorizarOCReciclarO, AutorizarOCReciclarP

from .reportes import reporte_compras, imprimir_compra, imprimir_compra2, imprimir_compra3, reporte_compras_modal

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
    path('ordencomprao/',ComprasViewO.as_view(), name="compras_listo"),
    path('ordencompraalr/',ComprasViewALR.as_view(), name="compras_listalr"),
    path('ordencomprap/',ComprasViewP.as_view(), name="compras_listp"),
    path('ordencompracxp/',ComprasViewCXP.as_view(), name="compras_listcxp"),
    
    path('ordencompraa/',ComprasViewA.as_view(), name="compras_lista"),
    path('ordencomprag/',ComprasViewG.as_view(), name="compras_listg"),
    path('ordencompram/',ComprasViewM.as_view(), name="compras_listm"),
    
    path('ordencompra/cierreofi/<int:id>',EnviarAutLedsaOfi, name="EnviarAutLedsaOfi"),
    path('ordencompra/cierrealr/<int:id>',EnviarAutALR, name="EnviarAutALR"),
    path('ordencompra/cierreplanta/<int:id>',EnviarAutLedsaPlanta, name="EnviarAutPlanta"),
    
    path('ordencompra/autorizarocals/<int:id>',AutorizarOCALS, name="autorizarocals"),
    path('ordencompra/autorizarocgls/<int:id>',AutorizarOCGLS, name="autorizarocgls"),
    path('ordencompra/autorizarocmls/<int:id>',AutorizarOCMLS, name="autorizarocmls"),

    path('ordencompra/reciclara/<int:id>',AutorizarOCReciclarA, name="reciclaroca"),
    path('ordencompra/reciclarg/<int:id>',AutorizarOCReciclarG, name="reciclarocg"),
    path('ordencompra/reciclarm/<int:id>',AutorizarOCReciclarM, name="reciclarocm"),
    path('ordencompra/reciclaro/<int:id>',AutorizarOCReciclarO, name="reciclaroco"),
    path('ordencompra/reciclarp/<int:id>',AutorizarOCReciclarP, name="reciclarocp"),

    path('ordencompra/provisionar/<int:id>',Provisionar, name="provisionar"),


    path('ordencompra/newo',comprasOficina, name="compras_newo"),
    path('ordencompra/newp',comprasPlanta, name="compras_newp"),
    path('ordencompra/newalr',comprasALR, name="compras_newalr"),
    path('ordencompra/edito/<int:compra_id>',comprasOficina, name="compras_edito"),
    path('ordencompra/editp/<int:compra_id>',comprasPlanta, name="compras_editp"),
    path('ordencompra/editalr/<int:compra_id>',comprasALR, name="compras_editalr"),
    path('ordencompra/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),

    path('ordencompra/listado', reporte_compras, name='compras_print_all'),
    path('ordencompra/<int:compra_id>/imprimir', imprimir_compra,name="compras_print_one"),
#    path('ordencompra/<slug:clienteuniqueid>/status', pedido_status,name="compras_status"),
    path('ordencompra/<slug:clienteuniqueid>/oc', imprimir_compra2,name="compras_print_client"),
    path('ordencompra/<slug:clienteuniqueid>/ocold', imprimir_compra3,name="compras_print_three"),
    path('ordencompra/modal', reporte_compras_modal,name="compras_print_modal"),
]