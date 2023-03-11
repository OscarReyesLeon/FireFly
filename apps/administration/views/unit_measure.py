from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.administration.serializers import UnitMeasureSerializer
from apps.administration.forms import UnitMeasureForm

PREFIX_URL = 'unit_measure'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': UnitMeasureForm,
            'femenine': True,
            'table_title_complete': 'unidades de medida',
            'prefix': PREFIX_URL,
            'prefix_text': 'unidad de médida',
            'prefix_app_url': 'administration',

            #API
            'current_serializer': UnitMeasureSerializer,
            'fields_full_text_search': ['name', 'description', 'symbol'],
        }, **kwargs)


class ProductListView(InitCurrentClassMixin, ListViewMixin):
    pass

class ProductCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class ProductUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class ProductDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass