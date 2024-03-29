from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.administration.serializers import ProductSerializer
from apps.administration.forms import ProductForm

PREFIX_URL = 'product'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': ProductForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'producto',
            'table_title_complete': 'unidades de medida',
            'prefix_app_url': 'administration',

            #API
            'current_serializer': ProductSerializer,
            'fields_full_text_search': ['name', 'description','category__name', 'unit_measure__name'],
        }, **kwargs)


class ProductListView(InitCurrentClassMixin, ListViewMixin):
    pass

class ProductCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class ProductUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class ProductDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass