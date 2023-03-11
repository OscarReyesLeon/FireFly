from django import forms
from apps.address.models import (
    StateModel, MunicipalityModel, NeighborhoodModel, AddressModel
)
from apps.core.forms import GeneralForm
"""
-----------------PRODUCTOS-----------------
"""
class StateForm(GeneralForm):
    class Meta:
        model = StateModel
        fields = ('name',)

class MunicipalityForm(GeneralForm):
    class Meta:
        model = MunicipalityModel
        fields = ('name', 'state')

class NeighborhoodForm(GeneralForm):
    class Meta:
        model = NeighborhoodModel
        fields = ('name', 'municipality', 'postal_code')

class SelectAddressForm(GeneralForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        state = None
        if 'data' in kwargs:
            state = kwargs.get("data", {}).get("direction-state", None)
        elif 'instance' in kwargs:
            state = kwargs.get("instance", None)
            if state:
                state = state.state
        else:
            self.fields['neighborhood'].queryset = NeighborhoodModel.objects.none()

        if state:
            self.fields['municipality'].queryset = MunicipalityModel.objects.filter(state=state)
            self.fields['neighborhood'].queryset = NeighborhoodModel.objects.filter(municipality__state=state)



    state = forms.ModelChoiceField(queryset=StateModel.objects.all(), required=True, label='Estado de la República',
            help_text="Seleccione el estado de la república para cargar los municipios",
            widget=forms.Select(attrs={
                'id': 'id_state',
            }))
    municipality = forms.ModelChoiceField(queryset=MunicipalityModel.objects.none(), required=True, label='Municipio',
            help_text="Seleccione el municipio para cargar las colonias",
            widget=forms.Select(attrs={
                'id': 'id_municipality',
            }))
    neighborhood = forms.ModelChoiceField(queryset=NeighborhoodModel.objects.none(), required=True, label='Colonia',
            help_text="Seleccione la colonia",
            widget=forms.Select(attrs={
                'id': 'id_neighborhood',
            }))

class AddressForm(SelectAddressForm):
    class Meta:
        model = AddressModel
        fields = ('street', 'number_ext', 'number_int', 'state', 'municipality', 'neighborhood', 'reference')