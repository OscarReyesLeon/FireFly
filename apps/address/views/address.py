from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.address.forms import AddressForm

PREFIX_URL = 'address'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': AddressForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'dirección',
            'prefix_app_url': 'address',
        }, **kwargs)


class AddressListView(InitCurrentClassMixin, ListViewMixin):
    pass

class AddressCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class AddressUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class AddressDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass