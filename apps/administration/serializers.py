from apps.administration.models import (CategoryProductModel, 
    BrandVehicleModel, FuelPumpModel, ProductModel,
    TruckVehicleModel, UnitMeasureModel, VehicleModel, DriverModel
)
from apps.core.serializers import SerializerBase
from rest_framework import serializers

class CategorySerializer(SerializerBase):
    class Meta:
        model = CategoryProductModel
        fields = ('id', 'name', 'description')

class UnitMeasureSerializer(SerializerBase):
    class Meta:
        model = UnitMeasureModel
        fields = ('id', 'name', 'description', 'symbol')

class ProductSerializer(SerializerBase):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'description', 
                  'base_price', 'category',
                  'unit_measure')

class BrandVehicleSerializer(SerializerBase):
    class Meta:
        model = BrandVehicleModel
        fields = ('id', 'name', 'description')

class FuelPumpSerializer(SerializerBase):
    class Meta:
        model = FuelPumpModel
        fields = ('id', 'name', 'description', 
                'get_type_fuel_pump_display',
                'get_location_display'
        )
        
class TruckVehicleSerializer(SerializerBase):
    class Meta:
        model = TruckVehicleModel
        fields = ('id', 'economic_number',
                'plates', 'get_type_truck_display',
                'is_active'
            )
        
class VehicleSerializer(SerializerBase):
    class Meta:
        model = VehicleModel
        fields = ('id', 'economic_number', 'brand',
                'plates', 'model', 'get_type_vehicle_display',
                'responsible', 'asigned_truck',
                'is_active'
            )
        
class VehicleOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ('id', 'name')

class DriverOptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_full_name')
    class Meta:
        model = DriverModel
        fields = ('id', 'name')

class FuelPumpOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelPumpModel
        fields = ('id', 'name')

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name')

class TruckVehicleOptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='economic_number')
    class Meta:
        model = TruckVehicleModel
        fields = ('id', 'name')