from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.users.forms import UserForm

PREFIX_URL = 'user'
class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': UserForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'usuario',
            'prefix_app_url': 'user',
        }, **kwargs)

class UserListView(InitCurrentClassMixin, ListViewMixin):
    pass

class UserCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class UserUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    def get_title_form_update(self):
        texto = super().get_title_form_update()
        return texto + ': ' + self.get_object().get_full_name()

class UserDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass