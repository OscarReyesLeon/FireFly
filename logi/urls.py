from django.urls import path

from .views import leer_piusi

urlpatterns = [
    path('piusi/leer', leer_piusi, name='leer_pius'),
]