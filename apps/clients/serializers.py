from apps.core.serializers import SerializerBase
from apps.clients.models import ClientModel, AddressModel, CreditModel, ClientAddressModel
from rest_framework import serializers
from django.db import transaction
from crum import get_current_user
class CreditSerializer(serializers.ModelSerializer):
    limit_date = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
    class Meta:
        model = CreditModel
        fields= (
            'id','description', 'amount', 'limit_date', 'client'
        )
        extra_kwargs = {
            'client': {'required': False}
        }

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = (
            'id', 'street', 'number_ext', 'number_int', 'neighborhood', 'reference')
        
    def to_representation(self, instance):
        from apps.address.serializers import NeighborhoodOptionsSerializer
        data = super().to_representation(instance)
        data['neighborhood'] = NeighborhoodOptionsSerializer(instance.neighborhood).data
        return data
        
class ClientSerializer(SerializerBase):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    class Meta:
        model = ClientModel
        fields = ('id','business_name', 'rfc',
                'email', 'phone', 'first_name',
                 'last_name', 'last_name_mother', 'full_name')
        
class ClientCompleteSerializer(serializers.ModelSerializer):
    credit = CreditSerializer(many=True, required=False)
    address = AddressSerializer(many=True, required=False)

    def create(self, validated_data):
        with transaction.atomic():
            credit_data = validated_data.pop('credit')
            address_data = validated_data.pop('address')
            client = super().create(validated_data)
            current_user = get_current_user()

            list_data = [CreditModel(**credit, client=client, 
                            user_create=current_user) for credit in credit_data]
            if list_data:
                CreditModel.objects.bulk_create(list_data)
            list_data = [AddressModel(**address, user_create=current_user) 
                         for address in address_data]
            if list_data:
                addresses = AddressModel.objects.bulk_create(list_data)
                client.address.set(addresses)
        return client
    
    def save_bulk_update_and_create(self,instance, key, validated_data, Model, array_fields,
            save_address=False, with_many=False):
        id_arrays = []
        to_create = []
        to_update = []
        initial_data = self.initial_data.get(key, [])
        for index, data in enumerate(validated_data):
            id_initial = initial_data[index].get('id', None)
            if id_initial:
                to_update.append(Model(id=id_initial, **data, user_update=self.current_user))
                id_arrays.append(id_initial)
            else:
                if not with_many and 'client' not in data:
                    data['client'] = instance
                to_create.append(Model(**data, user_create=self.current_user))
        data_create = Model.objects.bulk_create(to_create)
        Model.objects.bulk_update(to_update, array_fields)
        id_arrays.extend([data.id for data in data_create])
        if with_many and save_address:
            instance.address.set(Model.objects.filter(id__in=id_arrays))
        else:
            Model.objects.filter(client=instance).exclude(id__in=id_arrays).delete()
        
    
    def update(self, instance, validated_data):
        with transaction.atomic():
            credit_data = validated_data.pop('credit')
            address_data = validated_data.pop('address')
            instance = super().update(instance, validated_data)
            self.current_user = get_current_user()

            self.save_bulk_update_and_create(
                instance, 'credit', credit_data, CreditModel, 
                ['description','amount', 'limit_date','user_update']
            )
            self.save_bulk_update_and_create(
                instance, 'address', address_data, AddressModel, 
                ['street', 'number_ext', 'number_int', 'neighborhood', 'reference','user_update'], 
                save_address=True, with_many=True
            )
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(instance.credit_set.all())
        print(CreditModel.objects.all())
        data['credit'] = CreditSerializer(instance.credit_set.all(), many=True).data
        return data
    
    class Meta(ClientSerializer.Meta):
        model = ClientModel
        fields = ('id','business_name', 'rfc',
                'email', 'phone', 'first_name',
                 'last_name', 'last_name_mother', 'credit', 'address')
        


class ClientOptionsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='business_name', read_only=True)
    class Meta:
        model = ClientModel
        fields = ('id', 'name')

class ClientAddressOptionsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="address.get_full_address", read_only=True)
    class Meta:
        model = ClientAddressModel
        fields = ('id', 'name')