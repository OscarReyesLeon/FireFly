from apps.core.forms import GeneralForm
from apps.clients.models import ClientModel

class ClientForm(GeneralForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'v-model': 'form.' + field,
            })

    class Meta:
        model = ClientModel
        fields = '__all__'
        fields = (
            'business_name', 'rfc', 'email',
            'phone', 'first_name', 'last_name',
            'last_name_mother',
        )