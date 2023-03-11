from apps.address.models import MunicipalityModel, StateModel, NeighborhoodModel, AddressModel
from apps.core.serializers import SerializerBase
from rest_framework import serializers

class StateSerializer(SerializerBase):
    class Meta:
        model = StateModel
        fields = ('id', 'name')

class MunicipalitySerializer(SerializerBase):
    class Meta:
        model = MunicipalityModel
        fields = ('id', 'name', 'state')

class NeighborhoodSerializer(SerializerBase):
    class Meta:
        model = NeighborhoodModel
        fields = ('id', 'name', 'municipality', 'postal_code')

class NeighborhoodOptionsSerializer(SerializerBase):
    # state_id = serializers.IntegerField(source='municipality__state')
    class Meta:
        model = NeighborhoodModel
        fields = ('id', 'name', 'municipality_id')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['state_id'] = instance.municipality.state.id
        return data

class AddressSerializer(SerializerBase):
    class Meta:
        model = AddressModel
        fields = ('id', 'street', 'number_ext', 'number_int', 'neighborhood', 'reference')