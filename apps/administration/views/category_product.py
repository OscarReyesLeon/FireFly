from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.administration.serializers import CategorySerializer
from apps.administration.forms import CategoryProductForm

PREFIX_URL = 'category_product'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': CategoryProductForm,
            'femenine': True,
            'prefix': PREFIX_URL,
            'prefix_text': 'categoría',
            'prefix_app_url': 'administration',

            #API
            'current_serializer': CategorySerializer,
            'fields_full_text_search': ['name', 'description'],
        }, **kwargs)
        


class CategoryListView(InitCurrentClassMixin, ListViewMixin):
    pass

class CategoryCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class CategoryUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class CategoryDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass