from django.views.generic import TemplateView
from apps.core.views  import ListViewMixin, DeleteViewMixin, GenericFormMixin
from apps.orders.serializers import OrderSerializer

PREFIX_URL = 'order'
PREFIX_EMPTY = True

class InitCurrentClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(**{
            'model': OrderSerializer.Meta.model,
            'prefix': PREFIX_URL,
            'prefix_text': ' pedido',
            'prefix_app_url': 'order',
            
            #API
            'current_serializer': OrderSerializer,
            'fields_full_text_search': ["client__business_name", 'key_order', 'driver__first_name', 'driver__last_name', 'vehicle__plate']
        }, **kwargs)


class OrderListView(InitCurrentClassMixin, ListViewMixin):
    pass

class OrderCreateView(InitCurrentClassMixin, GenericFormMixin, TemplateView):
    template_name = 'order_form.html'
    view_type = 'create'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args,**kwargs)
        data.update({
            'with_vue': True,
        })
        return data
    
class OrderUpdateView(OrderCreateView):
    view_type = 'update'

    def get_object(self):
        self.object = self.model.objects.get(pk=self.kwargs['pk'])
        return self.object
    
class OrderDeleteView(InitCurrentClassMixin, DeleteViewMixin):
    pass