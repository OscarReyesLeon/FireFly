from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.address.forms import StateForm

PREFIX_URL = 'state'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': StateForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'estado',
            'prefix_app_url': 'address',
        }, **kwargs)


class StateListView(InitCurrentClassMixin, ListViewMixin):
    pass

class StateCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class StateUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class StateDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass