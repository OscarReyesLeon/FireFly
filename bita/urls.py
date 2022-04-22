from django.urls import path

from .views import *

urlpatterns = [
    path('operadorespesados/',OperadorPesadoView.as_view(),name='operador_pesado_list'),
    path('operadorespesados/new/',OperadorPesadoNew.as_view(),name='operador_pesad_new'),
    path('solicitantesutilitario/',SolicitantesUtilitarioView.as_view(),name='solicitante_utilitario_list'),
    path('solicitantesutilitario/mew/',SolicitantesUtilitarioNew.as_view(),name='solicitante_utilitari_new'),
    path('vechiculoligero/',VehiculoLigeroView.as_view(),name='vehiculo_ligero_list'),
    path('vechiculoligero/new/',VehiculoLigeroNew.as_view(),name='vehiculo_ligero_new'),
    path('vehiculopesado/',VehiculoPesadoView.as_view(),name='vehiculo_pesado_list'),
    path('vehiculopesado/new/',VehiculoPesadoNew.as_view(),name='vehiculo_pesado_new'),
    path('motivoingresounidad/',MotivoIngresoUnidadView.as_view(),name='motivo_ingreso_unidad_list'),
    path('motivoingresounidad/new/',MotivoIngresoUnidadNew.as_view(),name='motivo_ingreso_unidad_new'),
    path('destinosclientes/',DestinosClientesView.as_view(),name='destinos_clientes_list'),
    path('destinosclientes/new/',DestinosClientesNew.as_view(),name='destinos_clientes_new'),
    path('motivovisita/',MotivoVisitaView.as_view(),name='motivo_visita_list'),
    path('motivovisita/new/',MotivoVisitaNew.as_view(),name='motivo_visita_new'),
]