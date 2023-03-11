from apps.address.views import (
    state, municipality, neighborhood, address
)
from apps.core.urls import get_urls_by_view
list_views = [state, municipality, neighborhood, address]
urlpatterns = get_urls_by_view(list_views, with_uuid=True)