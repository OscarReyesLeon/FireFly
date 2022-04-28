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
]