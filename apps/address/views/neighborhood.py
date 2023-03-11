from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.address.serializers import NeighborhoodSerializer
from apps.address.forms import NeighborhoodForm

PREFIX_URL = 'neighborhood'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': NeighborhoodForm,
            'femenine': True,
            'prefix': PREFIX_URL,
            'prefix_text': 'colonia',
            'prefix_app_url': 'address',

            #API
            'current_serializer': NeighborhoodSerializer,
            'fields_full_text_search': ['name', 'municipality__name', 'postal_code'],
        }, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('municipality')
        return queryset


class NeighborhoodListView(InitCurrentClassMixin, ListViewMixin):
    pass

class NeighborhoodCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class NeighborhoodUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class NeighborhoodDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass