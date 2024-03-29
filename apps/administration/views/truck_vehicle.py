from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.administration.serializers import TruckVehicleSerializer
from apps.administration.forms import TruckVehicleForm

PREFIX_URL = 'truck_vehicle'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': TruckVehicleForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'remolque',
            'prefix_app_url': 'administration',

            #API
            'current_serializer': TruckVehicleSerializer,
            'fields_full_text_search': ['economic_number', 'plates'],
        }, **kwargs)

class TruckVehicleListView(InitCurrentClassMixin, ListViewMixin):
    pass

class TruckVehicleCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class TruckVehicleUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class TruckVehicleDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass