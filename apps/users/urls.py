from apps.core.urls import get_urls_by_view
from apps.users.views import permission, group, user
list_views = [permission, group, user]
urlpatterns = get_urls_by_view(list_views)