from django.views.decorators.cache import cache_page
from django.urls import path

from .views import EquipoView, EquipoNew, EquipoEdit, ingresoalmacen, \
    EquipoDel, \
    AutorizaView, AutorizaNew, AutorizaEdit, PedidoViewALRCot, \
    AutorizaDel, \
    BancoView, BancoNew, BancoEdit, pedido_transferido, \
    BancoDel, PedidoViewPlantaCot, PedidoViewOficinaCot, \
    ProcesoView, ProcesoNew, ProcesoEdit, ProcesoDel, \
    CategoriaView, CategoriaNew, CategoriaEdit, categoria_inactivar, \
    UMView, UMNew, UMEdit, pedido_entregadoo, pedido_entregadop, um_inactivar,\
    ProductoView, ProductoEdit, ProductoNew, producto_inactivar, PedidoNew, \
    PedidoView, PedidoViewH, PedidoViewF, PedidoViewALS, PedidoViewGLSH, PedidoViewGLS, \
    PedidoViewMLS, PedidoViewF3, PedidoViewF4o, PedidoViewF4p, PedidoViewF5, PedidoEditO, PedidoEditP, \
    pedido_acancela, pedido_scancela, pedido_aprobado_als, pedido_rechazado_als, pedido_aprobado_gls, \
    pedido_rechazado_gls, pedido_aprobado_mls, pedido_rechazado_mls, pedido_comprando, \
    pedido_reaut, pedido_stock, pedido_express, pedido_oc,\
    PuestoView, PuestoNew, PuestoEdit, PedidoViewF5, PedidoViewF6,\
    EmpleadoView, EmpleadoNew, EmpleadoEdit,\
    ComputadoraView, ComputadoraNew, ComputadoraEdit, HerramientaView, HerramientaNew, HerramientaEdit, \
    EmpresaView, EmpresaNew, EmpresaEdit, GeneroView, GeneroNew, GeneroEdit, EstudiosView, EstudiosNew, EstudiosEdit, \
    EcivilView, EcivilNew, EcivilEdit, DepartamentoNew, DepartamentoView, DepartamentoEdit, PedidoSecondNew, \
    ParentescocontactoView, ParentescocontactoNew, ParentescocontactoEdit, PedidoExport, \
    pedido_enviado, ArtciulosestandarizadosNew, ArtciulosestandarizadosEdit, \
    ArtciulosestandarizadosView, NombresrelacionNew, NombresrelacionEdit, NombresrelacionView, importar_compras_excel

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

    path('pedidos/importar', importar_compras_excel,name="pedidos_importar"),
    path('pedidostodos/', cache_page(60 * 1440)(PedidoView.as_view()), name="pedido_list"),
    path('pedidosexport/',PedidoExport.as_view(), name="pedido_export"),
    path('pedidos/',PedidoViewF.as_view(), name="pedido_list_f"),
    path('pedidosh/',PedidoViewH.as_view(), name="pedido_list_h"),
    path('pedidosCotOficina/',PedidoViewOficinaCot.as_view(), name="cotiza_oficina"),
    path('pedidosCotPlanta/',PedidoViewPlantaCot.as_view(), name="cotiza_planta"),
    path('pedidosCotALR/',PedidoViewALRCot.as_view(), name="cotiza_alr"),
    path('pedidosf3/',PedidoViewF3.as_view(), name="pedido_list_f3"),
    path('pedidosf4o/',PedidoViewF4o.as_view(), name="pedido_list_f4o"),
    path('pedidosf4p/',PedidoViewF4p.as_view(), name="pedido_list_f4p"),
    path('pedidosf5/',PedidoViewF5.as_view(), name="pedido_list_f5"),
    path('pedidosf6/',PedidoViewF6.as_view(), name="pedido_list_f6"),
    path('pedidos/new',PedidoNew.as_view(), name="pedido_new"),
    #path('pedido/news', PedidoSecondNew.as_view(), name="pedido_news"),
    path('pedidos/edito/<int:pk>',PedidoEditO.as_view(), name="pedido_edito"),
    path('pedidos/editp/<int:pk>',PedidoEditP.as_view(), name="pedido_editp"),
    path('pedidos/rechazadosc/<int:id>',pedido_scancela, name="scancela"),
    path('pedidos/rechazadoac/<int:id>',pedido_acancela, name="acancela"),
    path('pedidos/aprobadoals/<int:id>',pedido_aprobado_als, name="pedido_aprobado_als"),
    path('pedidos/rechazadoals/<int:id>',pedido_rechazado_als, name="pedido_rechazado_als"),
    path('pedidos/aprobadogls/<int:id>',pedido_aprobado_gls, name="pedido_aprobado_gls"),
    path('pedidos/rechazadogls/<int:id>',pedido_rechazado_gls, name="pedido_rechazado_gls"),
    path('pedidos/aprobadomls/<int:id>',pedido_aprobado_mls, name="pedido_aprobado_mls"),
    path('pedidos/rechazadomls/<int:id>',pedido_rechazado_mls, name="pedido_rechazado_mls"),
    path('pedidos/comprando/<int:id>',pedido_comprando, name="pedido_comprando"),
    path('pedidos/entregadoo/<int:id>',pedido_entregadoo, name="pedido_entregadoo"),
    path('pedidos/entregadop/<int:id>',pedido_entregadop, name="pedido_entregadop"),
    path('pedidos/reaut/<int:id>',pedido_reaut, name="pedido_reaut"),
    path('pedidos/stock/<int:id>',pedido_stock, name="pedido_stock"),
    path('pedidos/enviado/<int:id>',pedido_enviado, name="pedido_enviado"),
    path('pedidos/express/<int:id>',pedido_express, name="pedido_express"),
    path('pedidos/traslado/<int:id>',pedido_transferido, name="pedido_traslado"),
    path('pedidos/oc/<int:id>',pedido_oc, name="pedido_oc"),

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

    path('genero/', GeneroView.as_view(), name='genero_list'),
    path('genero/new', GeneroNew.as_view(), name='genero_new'),
    path('genero/edit/<int:pk>', GeneroEdit.as_view(), name='genero_edit'),

    path('estudios/', EstudiosView.as_view(), name='estudios_list'),
    path('estudios/new', EstudiosNew.as_view(), name='estudios_new'),
    path('estudios/edit/<int:pk>', EstudiosEdit.as_view(), name='estudios_edit'),

    path('ecivil/', EcivilView.as_view(), name='ecivil_list'),
    path('ecivil/new', EcivilNew.as_view(), name='ecivil_new'),
    path('ecivil/edit/<int:pk>', EcivilEdit.as_view(), name='ecivil_edit'),

    path('departamento/', DepartamentoView.as_view(), name='departamento_list'),
    path('departamento/new', DepartamentoNew.as_view(), name='departamento_new'),
    path('departamento/edit/<int:pk>', DepartamentoEdit.as_view(), name='departamento_edit'),

    path('pcontacto/', ParentescocontactoView.as_view(), name='parentescocontacto_list'),
    path('pcontacto/new', ParentescocontactoNew.as_view(), name='parentescocontacto_new'),
    path('pcontacto/edit/<int:pk>', ParentescocontactoEdit.as_view(), name='parentescocontacto_edit'),

    path('articulosestandarizados/',ArtciulosestandarizadosView.as_view(), name='articuloes_list'),
    path('articulosestandarizados/new',ArtciulosestandarizadosNew.as_view(), name='articuloes_new'),
    path('articulosestandarizados/edit/<int:pk>',ArtciulosestandarizadosEdit.as_view(), name='articuloes_edit'),

    path('nombresrelacion/',NombresrelacionView.as_view(), name='nombrerelacion_list'),
    path('nombresrelacion/new',NombresrelacionNew.as_view(), name='nombrerelacion_new'),
    path('nombresrelacion/edit/<int:pk>',NombresrelacionEdit.as_view(), name='nombrerelacion_edit'),

    path('almacen/nuevoingreso',ingresoalmacen, name="ingreso_new"),
    path('almacen/ingreso/<int:oc>',ingresoalmacen, name="ingreso_edit"),

]
