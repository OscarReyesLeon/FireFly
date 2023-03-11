from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.administration.serializers import BrandVehicleSerializer
from apps.administration.forms import BrandVehicleForm

PREFIX_URL = 'brand_vehicle'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': BrandVehicleForm,
            'femenine': True,
            'prefix': PREFIX_URL,
            'table_title_complete': 'marcas de vehículos',
            'prefix_text': 'marca de vehículo',
            'prefix_app_url': 'administration',

            #API
            'current_serializer': BrandVehicleSerializer,
            'fields_full_text_search': ['name', 'description'],
        }, **kwargs)


class BrandVehicleListView(InitCurrentClassMixin, ListViewMixin):
    pass

class BrandVehicleCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class BrandVehicleUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class BrandVehicleDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass