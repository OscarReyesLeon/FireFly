from django.urls import reverse
from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.users.forms import PermissionForm, Permission

PREFIX_URL = 'permission'
class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': PermissionForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'permiso',
            'prefix_app_url': 'user',
        }, **kwargs)

class PermissionListView(InitCurrentClassMixin, ListViewMixin):
    pass

class PermissionCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class PermissionUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class PermissionDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass