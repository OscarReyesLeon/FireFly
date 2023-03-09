from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
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
        }, **kwargs)
        


class CategoryListView(InitCurrentClassMixin, ListViewMixin):
    pass

class CategoryCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class CategoryUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class CategoryDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass