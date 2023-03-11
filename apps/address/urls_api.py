from apps.address.api.api import ListMunicipalityAPIView, ListNeighborhoodAPIView, ListStateAPIView
from django.urls import path

urlpatterns = [
    path('state/', ListStateAPIView.as_view(), name='list_states'),
    path('municipality/', ListMunicipalityAPIView.as_view(), name='list_municipalities'),
    path('neighborhood/', ListNeighborhoodAPIView.as_view(), name='list_neighborhoods'),
]