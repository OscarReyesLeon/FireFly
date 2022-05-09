from django.urls import path

from .views import *

urlpatterns = [
    path('operadorespesados/',OperadorPesadoView.as_view(),name='operador_pesado_list'),
    path('operadorespesados/new/',OperadorPesadoNew.as_view(),name='operador_pesado_new'),
    path('operadorespesados/edit/<int:pk>',OperadorPesadoEdit.as_view(),name='operador_pesado_edit'),
    path('solicitantesutilitario/',SolicitantesUtilitarioView.as_view(),name='solicitante_utilitario_list'),
    path('solicitantesutilitario/new/',SolicitantesUtilitarioNew.as_view(),name='solicitante_utilitario_new'),
    path('solicitantesutilitario/edit/<int:pk>',SolicitantesUtilitarioEdit.as_view(),name='solicitante_utilitario_edit'),
    path('vechiculoligero/',VehiculoLigeroView.as_view(),name='vehiculo_ligero_list'),
    path('vechiculoligero/new/',VehiculoLigeroNew.as_view(),name='vehiculo_ligero_new'),
    path('vechiculoligero/edit/<int:pk>',VehiculoLigeroEdit.as_view(),name='vehiculo_ligero_edit'),
    path('vehiculopesado/',VehiculoPesadoView.as_view(),name='vehiculo_pesado_list'),
    path('vehiculopesado/new/',VehiculoPesadoNew.as_view(),name='vehiculo_pesado_new'),
    path('vehiculopesado/edit/<int:pk>',VehiculoPesadoEdit.as_view(),name='vehiculo_pesado_edit'),
    path('motivoingresounidad/',MotivoIngresoUnidadView.as_view(),name='motivo_ingreso_unidad_list'),
    path('motivoingresounidad/new/',MotivoIngresoUnidadNew.as_view(),name='motivo_ingreso_unidad_new'),
    path('motivoingresounidad/edit/<int:pk>',MotivoIngresoUnidadEdit.as_view(),name='motivo_ingreso_unidad_edit'),
    path('destinosclientes/',DestinosClientesView.as_view(),name='destinos_clientes_list'),
    path('destinosclientes/new/',DestinosClientesNew.as_view(),name='destinos_clientes_new'),
    path('destinosclientes/edit/<int:pk>',DestinosClientesEdit.as_view(),name='destinos_clientes_edit'),
    path('motivovisita/',MotivoVisitaView.as_view(),name='motivo_visita_list'),
    path('motivovisita/new/',MotivoVisitaNew.as_view(),name='motivo_visita_new'),
    path('motivovisita/edit/<int:pk>',MotivoVisitaEdit.as_view(),name='motivo_visita_edit'),
    path('cargadeurea/',CargaUreaView.as_view(),name='carga_urea_list'),
    path('cargadeurea/new/',CargaUreaNew.as_view(),name='carga_urea_new'),
    path('cargadeurea/edit/<int:pk>',CargaUreaEdit.as_view(),name='carga_urea_edit'),
    path('descargadiesel/',DescargaDeDieselView.as_view(),name='descarga_diesel_list'),
    path('descargadiesel/new/',DescargaDeDieselNew.as_view(),name='descarga_diesel_new'),
    path('descargadiesel/edit/<int:pk>',DescargaDeDieselEdit.as_view(),name='descarga_diesel_edit'),
    path('tanquesdiesel/',TanquesDieselView.as_view(),name='tanques_diesel_list'),
    path('tanquesdiesel/new/',TanquesDieselNew.as_view(),name='tanques_diesel_new'),
    path('tanquesdiesel/edit/<int:pk>',TanquesDieselEdit.as_view(),name='tanques_diesel_edit'),
    path('cargadiesel/',CargaDeDieselView.as_view(),name='carga_diesel_list'),
    path('cargadiesel/new/',CargaDeDieselNew.as_view(),name='carga_diesel_new'),
    path('cargadiesel/edit/<int:pk>',DescargaDeDieselEdit.as_view(),name='carga_diesel_edit'),
    path('ingresounidadpesada/',IngresoUnidadPesadaView.as_view(),name='ingreso_unidad_pesada_list'),
    path('ingresounidadall/',IngresoUnidadPesadaExport.as_view(),name='ingreso_unidad_pesada_all'),
    path('ingresounidadpesada/new/',IngresoUnidadPesadaNew.as_view(),name='ingreso_unidad_pesada_new'),
    path('ingresounidadpesada/edit/<int:pk>',IngresoUnidadPesadaEdit.as_view(),name='ingreso_unidad_pesada_edit'),
    path('ingresounidadpesada/salida/<int:id>',salida_pesado, name='salida_pesado')
]