from django.urls import path
from apps.users.api.permissions import PermissionOrderAPIView
urlpatterns = [
    path('permissions/order_view/', PermissionOrderAPIView.as_view(), name='permissions'),
]