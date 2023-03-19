from django.urls import path
from apps.orders.api.orders import OrderOptionsInitialAPIView,OrderValidateCreateAPIView, OrderValidateGetUpdateAPIView

urlpatterns = [
    path('options/', OrderOptionsInitialAPIView.as_view(), name='order_choices'),
    path('', OrderValidateCreateAPIView.as_view(), name='order_validate_create'),
    path('<uuid:pk>/', OrderValidateGetUpdateAPIView.as_view(), name='order_validate_get_update'),
]