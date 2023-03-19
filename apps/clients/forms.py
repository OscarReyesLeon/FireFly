from apps.core.forms import GeneralFormVue
from apps.clients.models import ClientModel

class ClientForm(GeneralFormVue):
    class Meta:
        model = ClientModel
        fields = '__all__'
        fields = (
            'business_name', 'rfc', 'email',
            'phone', 'first_name', 'last_name',
            'last_name_mother',
        )