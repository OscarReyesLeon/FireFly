from apps.core.forms import GeneralFormVue
from apps.orders.models import OrderModel
from apps.clients.models import ClientAddressModel
from django import forms
class OrderForm(GeneralFormVue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address"].queryset = ClientAddressModel.objects.none()

        attrs_with_date = {
            'type': 'date',
            'class': 'form-control',
            'col_default': 6,
            'required': True,
            'v-model': 'form.delivery_date_estimated'
        }
        self.fields["delivery_date_estimated"].widget = forms.DateInput(attrs=attrs_with_date)
        attrs_with_date.update({'required': False, 'disabled': True, 'v-model': 'form.delivery_date'})
        self.fields["delivery_date"].widget = forms.DateInput(attrs=attrs_with_date)
    class Meta:
        model = OrderModel
        fields = (
            'key_order', 'invoice_status', 'status',
            'autorization','client', 'address',
            'delivery_date_estimated', 'delivery_date'
        )
        # fields = (
        #     'client', 'order_date', 'order_number',
        #     'order_status', 'order_type', 'order_payment',
        #     'order_payment_date', 'order_payment_amount',
        #     'order_payment_reference',
        # )