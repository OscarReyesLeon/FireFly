from django.views.generic import TemplateView
from apps.core.views  import ListViewMixin, DeleteViewMixin, GenericFormMixin
from apps.clients.serializers import ClientSerializer
from apps.clients.forms import ClientForm

PREFIX_URL = 'client'
PREFIX_EMPTY = True

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'form_class': ClientForm,
            'model': ClientSerializer.Meta.model,
            'prefix': PREFIX_URL,
            'prefix_text': 'cliente',
            'prefix_app_url': 'client',
            
            #API
            'current_serializer': ClientSerializer,
            'fields_full_text_search': ['first_name', 'last_name', 'business_name', 'rfc', 'email', 'phone'],
            'order_complex_fields' : {
                'full_name': ['first_name', 'last_name'],
            }

        }, **kwargs)


class ClientListView(InitCurrentClassMixin, ListViewMixin):
    pass

class ClientCreateView(InitCurrentClassMixin, GenericFormMixin, TemplateView):
    template_name = 'form_client.html'
    tipo_vista = 'create'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args,**kwargs)
        data.update({
            'form': ClientForm(),
            'with_vue': True,
        })
        return data
    
class ClientUpdateView(ClientCreateView):
    tipo_vista = 'update'
    
class ClientDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass