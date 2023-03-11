from apps.core.views  import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from apps.users.serializers import GroupSerializer
from apps.users.forms import GroupForm

PREFIX_URL = 'group'

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': GroupForm,
            'prefix': PREFIX_URL,
            'prefix_text': 'grupo',
            'prefix_app_url': 'user',

            #API
            'current_serializer': GroupSerializer,
            'fields_full_text_search': ['name'],
        }, **kwargs)


class GroupListView(InitCurrentClassMixin, ListViewMixin):
    pass

class GroupCreateView(InitCurrentClassMixin, CreateViewMixin):
    pass

class GroupUpdateView(InitCurrentClassMixin,UpdateViewMixin):
    pass

class GroupDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass