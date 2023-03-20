from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DeliveryCaptureView(LoginRequiredMixin,TemplateView):
    template_name = 'delivery_form.html'
    c_title_form = 'Captura de salida de almacén (Toneladas de la báscula)'
    step = 'exit_warehouse'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args,**kwargs)
        data.update({
            'with_vue': True,
            'c_title_form': self.c_title_form,
            'step': self.step
        })
        return data
    
class DeliveryCustomerCaptureView(DeliveryCaptureView):
    c_title_form = 'Captura de toneladas entregadas al cliente'
    step = 'delivery_customer'

class DeliveryChechEndCaptureView(DeliveryCaptureView):
    c_title_form = 'Finalizar viaje (Entrada a almacén)'
    step = 'return_warehouse'

class DeliveryFuelView(DeliveryCustomerCaptureView):
    c_title_form = 'Captura de combustible'
    step = 'fuel_capture'