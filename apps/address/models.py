from django.db import models
from apps.core.models import BaseModel

class StateModel(BaseModel):
    name = models.CharField(max_length=50, unique=True,
                help_text="Ingresa el nombre del estado de la república (Ej. Jalisco, Veracruz, etc.)",
                verbose_name="Nombre del estado")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Estados"
        verbose_name = "Estado"
        ordering = ['name']
        db_table = 'address_state'

class MunicipalityModel(BaseModel):
    name = models.CharField(max_length=50,
                help_text="Nombre del municipio (Ej. Zapopan, Tlaquepaque, etc.)",
                verbose_name="Nombre del municipio")
    state = models.ForeignKey(StateModel, on_delete=models.PROTECT,
                help_text="Estado al que pertenece el municipio(Ej. Jalisco, Veracruz, etc.)",
                verbose_name="Estado de la república")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Municipios"
        verbose_name = "Municipio"
        ordering = ['name']
        db_table = 'address_municipality'

class NeighborhoodModel(BaseModel):
    name = models.CharField(max_length=50,
                help_text="Nombre de la colonia (Ej. San Juan de Dios, San Pedro, etc.)",
                verbose_name="Nombre de la colonia")
    municipality = models.ForeignKey(MunicipalityModel, on_delete=models.PROTECT,
                help_text="Municipio al que pertenece la colonia",
                verbose_name="Municipio")
    postal_code = models.CharField(max_length=5,
                help_text="Código postal de la colonia (Ej. 45000, 45100, etc.)",
                verbose_name="Código postal")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Colonias"
        verbose_name = "Colonia"
        ordering = ['name']
        db_table = 'address_neighborhood'

class AddressModel(BaseModel):
    street = models.CharField(max_length=50,
                help_text="Calle (Ej. 5 de Mayo, Hidalgo, etc.)",
                verbose_name="Calle")
    number_ext = models.CharField(max_length=10,
                help_text="Número exterior (Ej. 123, 456, etc.)",
                verbose_name="Número exterior")
    number_int = models.CharField(max_length=10, null=True, blank=True,
                help_text="Número interior (Ej. 1, 2, etc.)",
                verbose_name="Número interior")
    neighborhood = models.ForeignKey(NeighborhoodModel, on_delete=models.PROTECT,
                help_text="Colonia a la que pertenece la dirección",
                verbose_name="Colonia")
    reference = models.CharField(max_length=50, null=True, blank=True,
                help_text="Referencia (Ej. Entre calles, a 50 metros de, etc.)",
                verbose_name="Referencia")

    def __str__(self):
        return self.street
    
    class Meta:
        verbose_name_plural = "Direcciones"
        verbose_name = "Dirección"
        ordering = ['street']
        db_table = 'address_address'