from django.urls import reverse
from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.administration.forms import FuelPumpForm 

PREFIX_URL = 'fuel_pump'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': FuelPumpForm,
            'femenine': True,
            'prefix': PREFIX_URL,
            'prefix_text': 'bomba de combustible',
            'prefix_app_url': 'administration',
        }, **kwargs)


class FuelPumpListView(InitCurrentClassMixin, ListViewMixin):
    pass

class FuelPumpCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class FuelPumpUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class FuelPumpDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass