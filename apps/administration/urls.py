from apps.administration.views import (
    category_product, fuel_pump, product, unit_measure, vehicle, brand_vehicle, truck_vehicle
)
from apps.core.urls import get_urls_by_view

list_views = [category_product, fuel_pump, product, unit_measure, vehicle, brand_vehicle, truck_vehicle]
urlpatterns = get_urls_by_view(list_views, with_uuid=True)