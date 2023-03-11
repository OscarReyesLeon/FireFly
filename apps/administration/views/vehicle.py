from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.administration.serializers import VehicleSerializer
from apps.administration.forms import VehicleForm

PREFIX_URL = 'vehicle'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': VehicleForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'vehículo',
            'prefix_app_url': 'administration',

            #API
            'current_serializer': VehicleSerializer,
            'fields_full_text_search': ['economic_number', 'plates', 'brand__name', 'model'],
        }, **kwargs)


class ProductListView(InitCurrentClassMixin, ListViewMixin):
    pass

class ProductCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class ProductUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class ProductDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass