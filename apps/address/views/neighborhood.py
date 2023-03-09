from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.address.forms import NeighborhoodForm

PREFIX_URL = 'neighborhood'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': NeighborhoodForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'colonia',
            'prefix_app_url': 'address',
        }, **kwargs)


class NeighborhoodListView(InitCurrentClassMixin, ListViewMixin):
    pass

class NeighborhoodCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class NeighborhoodUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class NeighborhoodDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass