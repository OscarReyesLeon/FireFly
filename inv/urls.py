from django.urls import path

from .views import EquipoView, EquipoNew, EquipoEdit, \
    EquipoDel, \
    AutorizaView, AutorizaNew, AutorizaEdit, \
    AutorizaDel, \
    BancoView, BancoNew, BancoEdit, \
    BancoDel, \
    ProcesoView, ProcesoNew, ProcesoEdit, ProcesoDel, \
    CategoriaView, CategoriaNew, CategoriaEdit, categoria_inactivar, \
    UMView, UMNew, UMEdit, pedido_entregado, um_inactivar,\
    ProductoView, ProductoEdit, ProductoNew, producto_inactivar, PedidoNew, PedidoView, PedidoViewF, PedidoViewXR, PedidoEdit, pedido_aprobado, pedido_rechazado, pedido_comprando, pedido_reaut, pedido_stock,\
    PuestoView, PuestoNew, PuestoEdit,\
    EmpleadoView, EmpleadoNew, EmpleadoEdit,\
    ComputadoraView, ComputadoraNew, ComputadoraEdit, HerramientaView, HerramientaNew, HerramientaEdit, EmpresaNew, EmpresaEdit ,EquipoForm, \
    EmpresaView, EmpresaNew, EmpresaEdit
    

urlpatterns = [
    path('equipos/',EquipoView.as_view(), name='equipo_list'),
    path('equipos/new',EquipoNew.as_view(), name='equipo_new'),
    path('equipos/edit/<int:pk>',EquipoEdit.as_view(), name='equipo_edit'),
    path('equipos/delete/<int:pk>',EquipoDel.as_view(), name='equipo_del'),

    path('procesos/',ProcesoView.as_view(), name='proceso_list'),
    path('procesos/new',ProcesoNew.as_view(), name='proceso_new'),
    path('procesos/edit/<int:pk>',ProcesoEdit.as_view(), name='proceso_edit'),
    path('procesos/delete/<int:pk>',ProcesoDel.as_view(), name='proceso_del'),

    path('autoriza/',AutorizaView.as_view(), name='autoriza_list'),
    path('autoriza/new',AutorizaNew.as_view(), name='autoriza_new'),
    path('autoriza/edit/<int:pk>',AutorizaEdit.as_view(), name='autoriza_edit'),
    path('autoriza/delete/<int:pk>',AutorizaDel.as_view(), name='autoriza_del'),

    path('categorias/',CategoriaView.as_view(), name="categoria_list"),
    path('categorias/new',CategoriaNew.as_view(), name="categoria_new"),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(), name="categoria_edit"),
    path('categorias/inactivar/<int:id>',categoria_inactivar, name="categoria_inactivar"),

    path('um/',UMView.as_view(), name="um_list"),
    path('um/new',UMNew.as_view(), name="um_new"),
    path('um/edit/<int:pk>',UMEdit.as_view(), name="um_edit"),
    path('um/inactivar/<int:id>',um_inactivar, name="um_inactivar"),

    path('productos/',ProductoView.as_view(), name="producto_list"),
    path('productos/new',ProductoNew.as_view(), name="producto_new"),
    path('productos/edit/<int:pk>',ProductoEdit.as_view(), name="producto_edit"),
    path('productos/inactivar/<int:id>',producto_inactivar, name="producto_inactivar"),

    path('pedidos/',PedidoView.as_view(), name="pedido_list"),
    path('pedidosf/',PedidoViewF.as_view(), name="pedido_list_f"),
    path('pedidosxr/',PedidoViewXR.as_view(), name="pedido_list_xr"),
    path('pedidos/new',PedidoNew.as_view(), name="pedido_new"),
    path('pedidos/edit/<int:pk>',PedidoEdit.as_view(), name="pedido_edit"),
    path('pedidos/aprobado/<int:id>',pedido_aprobado, name="pedido_aprobado"),
    path('pedidos/rechazado/<int:id>',pedido_rechazado, name="pedido_rechazado"),
    path('pedidos/comprando/<int:id>',pedido_comprando, name="pedido_comprando"),
    path('pedidos/entregado/<int:id>',pedido_entregado, name="pedido_entregado"),
    path('pedidos/reaut/<int:id>',pedido_reaut, name="pedido_reaut"),
    path('pedidos/stock/<int:id>',pedido_stock, name="pedido_stock"),

    path('banco/',BancoView.as_view(), name='banco_list'),
    path('banco/new',BancoNew.as_view(), name='banco_new'),
    path('banco/edit/<int:pk>',BancoEdit.as_view(), name='banco_edit'),
    path('banco/delete/<int:pk>',BancoDel.as_view(), name='banco_del'),

    path('puesto/',PuestoView.as_view(), name="puesto_list"),
    path('puesto/new',PuestoNew.as_view(), name="puesto_new"),
    path('puesto/edit/<int:pk>',PuestoEdit.as_view(), name="puesto_edit"),

    path('empleado/',EmpleadoView.as_view(), name="empleado_list"),
    path('empleado/new',EmpleadoNew.as_view(), name="empleado_new"),
    path('empleado/edit/<int:pk>',EmpleadoEdit.as_view(), name="empleado_edit"),

    path('computadora/',ComputadoraView.as_view(), name="computadora_list"),
    path('computadora/new',ComputadoraNew.as_view(), name="computadora_new"),
    path('computadora/edit/<int:pk>',ComputadoraEdit.as_view(), name="computadora_edit"),

    path('herramienta/',HerramientaView.as_view(), name="herramienta_list"),
    path('herramienta/new',HerramientaNew.as_view(), name="herramienta_new"),
    path('herramienta/edit/<int:pk>',HerramientaEdit.as_view(), name="herramienta_edit"),

    path('empresa/',EmpresaView.as_view(), name='empresa_list'),
    path('empresa/new',EmpresaNew.as_view(), name='empresa_new'),
    path('empresa/edit/<int:pk>',EmpresaEdit.as_view(), name='empresa_edit'),

]