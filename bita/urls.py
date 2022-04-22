from django.urls import path

from .views import *

urlpatterns = [
    path('operadorespesados/',OperadorPesadoView.as_view(),name='operador_pesado_list'),
    path('operadorespesados/new/',OperadorPesadoNew.as_view(),name='operador_pesado_new'),
    path('solicitantesutilitario/',SolicitantesUtilitarioView.as_view(),name='solicitante_utilitario_list'),
]