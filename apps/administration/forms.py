from django.contrib.auth.models import User
from apps.administration.models import (
    ProductModel, CategoryProductModel, UnitMeasureModel, 
    FuelPumpModel, BrandVehicleModel, VehicleModel,
    TruckVehicleModel
)
from apps.core.forms import GeneralForm

"""
-----------------PRODUCTOS-----------------
"""
class CategoryProductForm(GeneralForm):
    class Meta:
        model = CategoryProductModel
        fields = ('name', 'description',)

class UnitMeasureForm(GeneralForm):
    class Meta:
        model = UnitMeasureModel
        fields = ('name', 'description', 'symbol')
class ProductForm(GeneralForm):
    class Meta:
        model = ProductModel
        fields = ('name', 'description', 'base_price', 
                'category', 'unit_measure', 'image')
        
"""
-----------------VEHICULOS-----------------
"""
class FuelPumpForm(GeneralForm):
    class Meta:
        model = FuelPumpModel
        fields = ('name', 'description', 'type_fuel_pump', 'location')

class BrandVehicleForm(GeneralForm):
    class Meta:
        model = BrandVehicleModel
        fields = ('name', 'description')

class TruckVehicleForm(GeneralForm):
    class Meta:
        model = TruckVehicleModel
        fields = ('economic_number', 'plates', 'type_truck', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].initial = True

class VehicleForm(GeneralForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['responsible'].queryset = User.objects.filter(groups__name='CHOFER')
        self.fields['is_active'].initial = True
    
    class Meta:
        model = VehicleModel
        fields = (
            'name', 'description', 'economic_number', 'plates', 
            'brand', 'model', 'type_vehicle', 'responsible', 'asigned_truck',
            'is_active',
        )