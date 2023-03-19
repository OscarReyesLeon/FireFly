from django.core.validators import MinValueValidator
from django.db import models

from apps.core.choices import (
    CHOICES_LOCATION_FUEL_PUMP, CHOICES_TYPE_FUEL_PUMP,CHOICES_TYPE_TRUCK,
    CHOICES_TYPE_VEHICLE
    # OPCIONES_TIPO_BOMBA, UBICACION_BOMBA, OPCIONES_TIPO_CAMION
)
from apps.core.models import BaseModel
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
"""
----------------------PRODUCTS---------------------
            Modelos relacionados a productos
---------------------------------------------------
"""

class CategoryProductModel(BaseModel):
    name = models.CharField(max_length=50, unique=True, 
                            help_text="Nombre de la categoría a la que pertenecerá el producto",
                            verbose_name="Nombre")
    description = models.CharField(max_length=100, null=True, blank=True,
                            help_text="Breve descripción de la categoría que indique su propósito",
                            verbose_name="Descripción")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categorias de producto"
        verbose_name = "Categoria de producto"
        ordering = ['name']
        db_table = 'administration_category_product'

class UnitMeasureModel(BaseModel):
    name = models.CharField(max_length=50, unique=True,
                            help_text="Nombre de la unidad de médida que va a dar de alta (Litros, Toneladas, etc)",
                            verbose_name="Nombre")
    description = models.CharField(max_length=100, null=True, blank=True,
                                help_text="Breve descripción de la unidad de medida que indique su propósito",
                                verbose_name="Descripción")
    symbol = models.CharField(max_length=10, null=True, blank=True,
                               help_text="Símbolo o abreviatura de la unidad de medida (L, T, etc)",
                               verbose_name="Símbolo")

    def __str__(self):
        return f'{self.name} ({self.symbol})'
    class Meta:
        verbose_name_plural = "Unidades de medida"
        verbose_name = "Unidad de medida"
        ordering = ['name']
        db_table = 'administration_unit_measure'

class ProductModel(BaseModel):
    name = models.CharField(max_length=50, unique=True,
                            help_text="Nombre con el que se identificará el producto",
                            verbose_name="Nombre del producto")
    description = models.CharField(max_length=100, null=True, blank=True,
                                help_text="Breve descripción del producto (Nombre comercial, detalles, etc)",
                                verbose_name="Descripción del producto")
    base_price = models.FloatField(default=0, validators=[MinValueValidator(0.0)],
                                help_text="Precio base del producto (Precio considerado como referencia para capturistas)",
                                verbose_name="Precio base")
    category = models.ForeignKey(CategoryProductModel, on_delete=models.SET_NULL, null=True,
                                  help_text="Indica la categoría a la que pertenece el producto",
                                  verbose_name="Categoría del producto")
    unit_measure = models.ForeignKey(UnitMeasureModel, on_delete=models.SET_NULL, null=True,
                                      help_text="Indica la unidad de medida con la que se manejará el producto",
                                      verbose_name="Unidad de medida")
    image = models.ImageField(upload_to='product/', null=True, blank=True,
                               help_text="Imagen del producto (Opcional)",
                               verbose_name="Imagen del producto")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"
        ordering = ['name']
        db_table = 'administration_product'


"""
----------------------VEHICLES---------------------
            Modelos relacionados a vehiculos
---------------------------------------------------
"""
class CustomUserManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(groups__name="CHOFER")

class DriverModel(User):
    objects = CustomUserManager()

    class Meta:
        proxy = True

class FuelPumpModel(BaseModel):
    name = models.CharField(max_length=50, unique=True,
                            help_text="Nombre con el que se identificará la bomba de combustible",
                            verbose_name="Nombre")
    description = models.CharField(max_length=100, null=True, blank=True,
                                help_text="Breve descripción de la bomba de combustible (Ubicación, detalles, etc)",
                                verbose_name="Descripción")
    type_fuel_pump = models.PositiveSmallIntegerField(choices=CHOICES_TYPE_FUEL_PUMP, default=0,
                                help_text="Favor de seleccionar el tipo de bomba(Gasolina, diesel, etc)",
                                verbose_name="Tipo de bomba")
    location = models.PositiveSmallIntegerField(choices=CHOICES_LOCATION_FUEL_PUMP, default=0,
                                help_text="Ubicación con la que se identificará la bomba de combustible",
                                verbose_name="Ubicación")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Bombas"
        verbose_name = "Bomba"
        ordering = ['name']
        db_table = 'administration_fuel_pump'

class BrandVehicleModel(BaseModel):
    name = models.CharField(max_length=50, unique=True,
                            help_text="Nombre de la marca de vehiculo (Ford, Chevrolet, etc)",
                            verbose_name="Nombre")
    description = models.CharField(max_length=100, null=True, blank=True,
                                help_text="Breve descripción de la marca de vehiculo (Detalles, etc)",
                                verbose_name="Descripción")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Marcas de vehiculo"
        verbose_name = "Marca de vehiculo"
        ordering = ['name']
        db_table = 'administration_vehicle_brand'

class TruckVehicleModel(BaseModel):
    economic_number = models.CharField(max_length=10, unique=True,
                            help_text="Número económico del remolque (Ej. 1234)",
                            verbose_name="Número económico")
    plates = models.CharField(max_length=10, unique=True,
                            help_text="Placas del remolque (Ej. ABC1234)",
                            verbose_name="Placas")
    type_truck = models.PositiveSmallIntegerField(choices=CHOICES_TYPE_TRUCK, default=0,
                            help_text="Tipo de remolque",
                            verbose_name="Tipo de remolque")
    is_active = models.BooleanField(default=False,
                            help_text="Indica si el remolque está habilitado para ser usado. Desactivar si está descompueto.",
                            verbose_name="¿Disponible?")
    
    def __str__(self):
        return self.economic_number
    
    class Meta:
        verbose_name_plural = "Remolques"
        verbose_name = "Remolque"
        ordering = ['economic_number']
        db_table = 'administration_truck_vehicle'

class VehicleModel(BaseModel):
    name = models.CharField(max_length=50, unique=True,
            help_text="Nombre con el que se indentifica el vehiculo dentro de la empresa",
            verbose_name="Nombre del vehiculo")
    description = models.CharField(max_length=100, null=True, blank=True,
            help_text="Breve descripción del vehiculo (Detalles, características, etc)",
            verbose_name="Descripción")
    economic_number = models.CharField(max_length=5, unique=True, 
            help_text='Número económico del vehiculo (Ej. 1234)',
            verbose_name="Número económico")
    plates = models.CharField(max_length=10, unique=True, 
            help_text='Placas del vehiculo (Ej. ABC1234)',
            verbose_name="Placas")
    brand = models.ForeignKey(BrandVehicleModel, on_delete=models.SET_NULL, null=True,
            help_text='Marca comercial del vehiculo',
            verbose_name="Marca del vehiculo")
    model = models.CharField(max_length=20,
            help_text='El modelo del vehiculo (Ej. AVEO 2023)',
            verbose_name="Modelo")
    type_vehicle = models.PositiveSmallIntegerField(choices=CHOICES_TYPE_VEHICLE, default=0,
            help_text='Tipo de vehiculo (Ligero, pesado, etc)',
            verbose_name="Tipo de vehiculo")
    responsible = models.ForeignKey(DriverModel, on_delete=models.SET_NULL, null=True, blank=True,
            help_text='Chofer responsable del vehiculo (Opcional)',
            verbose_name="Chofer responsable")
    asigned_truck = models.ManyToManyField(TruckVehicleModel,
            help_text='Remolques asignados al vehiculo (Opcional)',
            verbose_name="Remolques asignados")
    is_active = models.BooleanField(default=False,
            help_text='Indica si el vehiculo está habilitado para ser usado. Desactivar si está descompueto.',
            verbose_name="¿Disponible?")


    def __str__(self):
        return f'{self.name} ({self.economic_number})'
    
    class Meta:
        verbose_name_plural = "Vehiculos"
        verbose_name = "Vehiculo"
        ordering = ['economic_number']
        db_table = 'administration_vehicle'