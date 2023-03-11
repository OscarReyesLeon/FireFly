from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.users.serializers import UserSerializer
from apps.users.forms import UserForm

PREFIX_URL = 'user'
class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': UserForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'usuario',
            'prefix_app_url': 'user',

            #API
            'current_serializer': UserSerializer,
            'fields_full_text_search': ['first_name', 'last_name', 'email'],
        }, **kwargs)

class UserListView(InitCurrentClassMixin, ListViewMixin):
    pass

class UserCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class UserUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class UserDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass