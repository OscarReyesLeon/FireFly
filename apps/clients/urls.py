from apps.clients.views import clients
from apps.core.urls import get_urls_by_view

list_views = [clients]
urlpatterns = get_urls_by_view(list_views, with_uuid=True)