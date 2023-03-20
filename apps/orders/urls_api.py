from django.urls import path
from apps.orders.api.orders import OrderOptionsInitialAPIView,OrderValidateCreateAPIView, OrderValidateGetUpdateAPIView
from apps.orders.api.delivery import OrderSearchAPIView
urlpatterns = [
    path('options/', OrderOptionsInitialAPIView.as_view(), name='order_choices'),
    path('', OrderValidateCreateAPIView.as_view(), name='order_validate_create'),
    path('<uuid:pk>/', OrderValidateGetUpdateAPIView.as_view(), name='order_validate_get_update'),
    path('warehouse/', OrderSearchAPIView.as_view(), name='order_search_warehouse'),
]