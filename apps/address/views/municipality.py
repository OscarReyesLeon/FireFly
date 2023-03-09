from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.address.forms import MunicipalityForm

PREFIX_URL = 'municipality'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': MunicipalityForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'municipio',
            'prefix_app_url': 'address',
        }, **kwargs)


class MunicipalityListView(InitCurrentClassMixin, ListViewMixin):
    pass

class MunicipalityCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class MunicipalityUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class MunicipalityDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass