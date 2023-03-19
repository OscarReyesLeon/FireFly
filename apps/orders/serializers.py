from apps.core.serializers import SerializerBase
from apps.orders.models import OrderModel, DetailOrderModel
from rest_framework import serializers
from crum import get_current_user
from datetime import datetime
class OrderSerializer(SerializerBase):
    class Meta:
        model = OrderModel
        fields = (
            'id', 'key_order', 'status', 'get_status_display',
            'autorization', 'client', 'address',
            'vehicle', 'driver'
        )


class DetailOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailOrderModel
        fields = (
            'id','product', 'quantity_order',
            'quantity_transfer', 'truck',
            'ton_out', 'ton_receiver'
        )

    def validate(self, data, *args, **kwargs):
        super().validate(data, *args, **kwargs)
        print("Validando", data, data.get('quantity_order'), data.get('quantity_transfer'))
        if data.get('quantity_order') < data.get('quantity_transfer'):
            raise serializers.ValidationError({
                "quantity_transfer": 'La cantidad de traslado no puede ser mayor a la cantidad de la orden'
            })
        return data

class OrderSaveSerializer(serializers.ModelSerializer):
    products = DetailOrderSerializer(many=True, write_only=True, required=True)
    detail = DetailOrderSerializer(many=True, read_only=True, source='order_detail')

    class Meta:
        model = OrderModel
        fields = (
            'id', 'key_order', 'status', 'invoice_status',
            'autorization', 'delivery_date_estimated', 'delivery_date',
            'client', 'address', 'vehicle', 'driver',
            'fuel_liters', 'fuel_pump', 'products', 'detail',
        )
    
    def create(self, validated_data):
        products = validated_data.pop('products')
        order = super().create(validated_data)
        for product in products:
            DetailOrderModel.objects.create(order=order, **product)
        return order
    
    def update(self, instance, validated_data):
        user = get_current_user()
        today = datetime.now()
        products = validated_data.pop('products')
        order = super().update(instance, validated_data)
        id_list = [product.get('id') for product in products]
        instance.order_detail.exclude(id__in=id_list).delete()
        for product in products:
            if 'id' in product:
                DetailOrderModel.objects.get(id=product.pop('id'))
                DetailOrderModel.objects.update(**product, user_update=user, date_update=today)
            else:
                DetailOrderModel.objects.create(order=order, **product)
        return order
