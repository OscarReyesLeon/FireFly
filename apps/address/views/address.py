from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.address.serializers import AddressSerializer
from apps.address.forms import AddressForm

PREFIX_URL = 'direction'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': AddressForm,
            'femenine': True,
            'prefix': PREFIX_URL,
            'prefix_text': 'dirección',
            'table_title_complete': ' direcciones',
            'prefix_app_url': 'address',
            'form_with_address': True,
            
            #API
            'current_serializer': AddressSerializer,
            'fields_full_text_search': ['name'],

        }, **kwargs)


class AddressListView(InitCurrentClassMixin, ListViewMixin):
    pass

class AddressCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class AddressUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class AddressDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass