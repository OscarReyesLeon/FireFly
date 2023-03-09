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

class AddressForm(GeneralForm):
    class Meta:
        model = AddressModel
        fields = ('street', 'number_ext', 'number_int', 'neighborhood', 'reference')