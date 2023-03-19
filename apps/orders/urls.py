from apps.orders.views import orders
from apps.core.urls import get_urls_by_view

list_views = [orders]
urlpatterns = get_urls_by_view(list_views, with_uuid=True)