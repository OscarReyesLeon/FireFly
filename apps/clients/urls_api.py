from django.urls import path
from apps.clients.api.clients import (
    ClientCreateCompleteAPIView, ClientGetUpdateCompleteAPIView,
    ClientOptionsAPIVIew, ClientAddressOptionsAPIView
)
urlpatterns = [
    path('complete/', ClientCreateCompleteAPIView.as_view(), name='client_create_complete'),
    path('<uuid:pk>/complete/', ClientGetUpdateCompleteAPIView.as_view(), name='client_get_update_complete'),
    path('options/', ClientOptionsAPIVIew.as_view(), name='client_options'),
    path('<uuid:pk>/address/options/', ClientAddressOptionsAPIView.as_view(), name='client_address_options'),
]