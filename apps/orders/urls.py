from apps.orders.views import orders
from apps.core.urls import get_urls_by_view
from django.urls import path
from apps.orders.views.delivery import DeliveryCaptureView, DeliveryCustomerCaptureView, DeliveryChechEndCaptureView, DeliveryFuelView
list_views = [orders]
urlpatterns = get_urls_by_view(list_views, with_uuid=True)

urlpatterns += [
    path('delivery/output/', DeliveryCaptureView.as_view(), name='delivery_output'),
    path('delivery/customer/', DeliveryCustomerCaptureView.as_view(), name='delivery_customer'),
    path('delivery/end_transfer/', DeliveryChechEndCaptureView.as_view(), name='delivery_end_transfer'),
    path('delivery/fuel/', DeliveryFuelView.as_view(), name='delivery_fuel'),
]   