from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.core.validators import MinValueValidator
from apps.core.models import BaseModel
from apps.address.models import AddressModel

class ClientModel(BaseModel):
    business_name = models.CharField(max_length=50, unique=True,
            help_text="Razón social del cliente (Ej. Transportes S.A. de C.V.)",
            verbose_name="Razón social")
    rfc = models.CharField(max_length=13, unique=True,
            help_text="RFC del cliente (Ej. TASA800101XXX)",
            verbose_name="RFC")
    email = models.EmailField(max_length=50, null=True, blank=True,
            help_text="Correo electrónico del cliente (Opcional)",
            verbose_name="Correo electrónico")
    phone = models.CharField(max_length=10, null=True, blank=True,
            help_text="Número de teléfono del cliente (Opcional)",
            verbose_name="Teléfono")
    first_name = models.CharField(max_length=50,
            help_text="Nombre del cliente o responsable",
            verbose_name="Nombre")
    last_name = models.CharField(max_length=50,
            help_text="Apellido paterno del cliente o responsable",
            verbose_name="Apellido paterno")
    last_name_mother = models.CharField(max_length=50, null=True, blank=True,
            help_text="Apellido materno del cliente o responsable (Opcional)",
            verbose_name="Apellido materno")
    address = models.ManyToManyField(AddressModel, blank=True,
                help_text="Dirección del cliente (Opcional)", 
                through='ClientAddressModel',
                verbose_name="Dirección")

    def __str__(self):
        return f'{self.business_name} ({self.rfc})'
    
    @property
    def nombre_completo(self):
        return f'{self.business_name} - {self.rfc}'
    
    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name} {self.last_name_mother}'
    
    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"
        ordering = ['business_name']
        db_table = 'clients_client'

class ClientAddressModel(BaseModel):
        client = models.ForeignKey(ClientModel, on_delete=models.PROTECT,
                        help_text="Cliente al que pertenece la dirección",
                        verbose_name="Cliente", related_name='address_set')
        address = models.ForeignKey(AddressModel, on_delete=models.PROTECT,
                        help_text="Dirección del cliente",
                        verbose_name="Dirección")
        def __str__(self):
                return f'{self.client} - {self.address}'
        
        class Meta:
                verbose_name_plural = "Direcciones de clientes"
                verbose_name = "Dirección de cliente"
                ordering = ['client']
                db_table = 'clients_client_address'
        
class CreditModel(BaseModel):
    description = models.CharField(max_length=100, 
                    help_text="Descripción del credito (Ej. Credito para cliente de X empresa)",
                    verbose_name="Descripción")
    amount = models.FloatField(default=0, validators=[MinValueValidator(0.0)],
                    help_text="Monto máximo del crédito( Ej. 100,000)",
                    verbose_name="Monto del crédito")
    limit_date = models.DateField(null=True, blank=True,
                    help_text="Fecha límite para el pago del crédito (Opcional)",
                    verbose_name="Fecha límite")
    client = models.ForeignKey(ClientModel, on_delete=models.PROTECT,
                    help_text="Cliente al que pertenece el crédito",
                    verbose_name="Cliente", related_name='credit_set')
    def __str__(self):
        return f'{self.client} - {self.amount}'
    
    class Meta:
        verbose_name_plural = "Creditos"
        verbose_name = "Credito"
        ordering = ['client']
        db_table = 'clients_credit'