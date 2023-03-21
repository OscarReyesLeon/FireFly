from django.db import models
from apps.core.choices import (
    CHOICES_ORDER_STATUS, CHOICES_INVOICE_STATUS, CHOICES_PAYMENT_METHOD,
)
from apps.core.models import BaseModel
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from crum import get_current_user
from datetime import datetime
import requests
import json

class LogOrderModel(BaseModel):
    order = models.ForeignKey('OrderModel', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=CHOICES_ORDER_STATUS, default=1)
    api_gps = models.JSONField(blank=True, null=True) #Cambios de PedidoModel y DetallesPedidoModel
    odometer = models.PositiveIntegerField(blank=True, null=True, default=0)
    velocity = models.PositiveIntegerField(blank=True, null=True, default=0)
    
    def save(self,with_api=False, *args, **kwargs):
        user = get_current_user()
        if self.pk:
            self.user_update = user
        else:
            self.user_create = user
        if with_api:
            try:
                url = "https://swservicios.mastrack.com.mx/Unidades/LocalizarUnidades/"
                alias = self.order.vehicle.economic_number
                data_send = json.dumps({
                    "LocalizarUnidades":{
                        "sGeocercasSubclasificaciones":"","sGeocercasCategorias":"",
                        "sGrupos":"","sGeocercasSubcategorias":"","bCompania":True,"sSeries":"",
                        "bGeocercas":True,"sAlias":alias,"sUsuario":"C7357LEDSA",
                        "sGeocercasClasificaciones":"","sZonaHoraria":"","sGeocercas":"Todas","sPassword":"admin"
                    }
                })
                data = requests.post(url, data=data_send)
                self.api_gps = data.json()
                response = self.api_gps.get("LocalizarUnidades", {})
                if data.status_code == 200:
                    unity = response.get("Unidades", [{}])[0]
                    odometer = unity.get("Odometro", "0")
                    velocity = unity.get("Velocidad", "0")
                    self.odometer = odometer.split(" ")[0]
                    self.velocity = velocity.split(" ")[0]
            except Exception as e:
                self.api_gps = None
        super().save(*args, **kwargs)

class OrderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs).order_by("-key_order")
        user = get_current_user()
        if user.is_superuser:
            return queryset
        groups_user = user.groups.filter(
            name__in=["CAPTURISTA_ORDEN", "AUTORIZAR_ORDEN", "CAPTURISTA_TRASLADO"]
        )
        if not groups_user.exists():
            return queryset.none()
        status = []
        autorization = None
        if groups_user.filter(name="CAPTURISTA_ORDEN").exists():
            status.append(1)
            autorization = False
        if groups_user.filter(name="AUTORIZAR_ORDEN").exists():
            status.append(2)
        if groups_user.filter(name="CAPTURISTA_TRASLADO").exists():
            status.append(3)
            autorization = False
        queryset =  queryset.filter(status__in=status)
        if autorization is not None:
            queryset = queryset.filter(autorization=autorization)
        return queryset
    
    def get_next_key_order(self, *args, **kwargs):
        import random
        letters = ["A", "B", "C", "D", "E", "F", 
                                "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                                "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
                ]
        query =  self.get_queryset(*args, **kwargs)
        search_key = True
        current_key = "A1"
        while search_key:
            current_key = f"{random.choice(letters)}{random.choice(letters)}{random.randint(0, 10)}{random.randint(0, 10)}{random.randint(0, 10)}"
            if not query.filter(key_order=current_key).exists():
                search_key = False
        return current_key


class OrderModel(BaseModel):
    objects = OrderManager()
    key_order = models.CharField(unique=True, max_length=6,
                    verbose_name='Folio de la orden',
                    help_text='Folio de la orden',)
    status = models.PositiveSmallIntegerField(choices=CHOICES_ORDER_STATUS, default=1,
                    verbose_name='Estatus del pedido',
                    help_text='Estatus del pedido',)
    invoice_status = models.PositiveSmallIntegerField(choices=CHOICES_INVOICE_STATUS, default=0,
                    verbose_name='Estatus del proceso de factura',
                    help_text='Estatus del proceso de factura',)
    autorization = models.BooleanField(default=False,
                    verbose_name='Autorización',
                    help_text='Autorización para realizar la orden',)
    delivery_date_estimated = models.DateField(null=True, blank=True,
                    verbose_name='Fecha de entrega estimada',
                    help_text='Fecha de entrega estimada de la orden',)
    delivery_date = models.DateField(null=True, blank=True,
                    verbose_name='Fecha de entrega',
                    help_text='Fecha de entrega de la orden',)
    client = models.ForeignKey('clients.ClientModel', on_delete=models.PROTECT,
                                null=True, related_name='client',
                                verbose_name='Cliente',
                                help_text='Cliente al que se le realizará el traslado')
    address = models.ForeignKey('clients.ClientAddressModel', on_delete=models.PROTECT, null=True, blank=True,
                                related_name='address_order',
                                verbose_name='Dirección',
                                help_text='Dirección a la que se realizará el traslado')
    
    #Datos de la orden
    vehicle = models.ForeignKey('administration.VehicleModel', on_delete=models.PROTECT, 
                                blank=True, null=True, related_name='vehicle',
                                verbose_name='Vehículo',
                                help_text='Vehículo que se utilizará para el traslado')
    
    driver = models.ForeignKey('administration.DriverModel', on_delete=models.PROTECT,
                                null=True, related_name='driver_transfer',
                                verbose_name='Conductor',
                                help_text='Conductor que realizará el traslado')
    #KM y ubicación con API, no se pide al usuario
    fuel_liters = models.FloatField(default=0, validators=[MinValueValidator(0.0)], null=True, blank=True,
                                verbose_name="Litros de combustible",
                                help_text="Litros de combustible que se utilizaron en el traslado")
    fuel_pump = models.ForeignKey('administration.FuelPumpModel', on_delete=models.PROTECT, null=True, blank=True,
                                verbose_name="Bombas de combustible que se utilizará",
                                help_text="Bombas de combustible que se utilizará")
    
    def __str__(self):
        return f"Orden: {self.key_order}- {self.client}"

    class Meta:
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"
        ordering = ['key_order']
        db_table = 'orders_order'

    def save(self, *args, **kwargs):
        if not self.key_order:
            self.key_order = self.__class__.objects.get_next_key_order()
        if self.status == 4:
            #Si ya se genero carta porte, todo bien
            pass
        if self.status == 6:
            self.delivery_date = datetime.now().date()
            #Generar fáctura
        if self.pk:
            log = LogOrderModel(
                with_api=False,
                order=self,
                status=self.status,
            )
            if self.status in [4, 5,6,7,8]:
                log.with_api = True
            log.save()
        super().save(*args, **kwargs)
        

class DetailOrderModel(BaseModel):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='order_detail',
                    verbose_name='Pedido',
                    help_text='Pedido al que pertenece el detalle',)
    product = models.ForeignKey('administration.ProductModel', on_delete=models.PROTECT, related_name='product',
                    verbose_name='Producto',
                    help_text='Producto que se agregará al pedido',)
    quantity_order = models.FloatField(default=0, validators=[MinValueValidator(0.0)],
                    verbose_name='Cantidad solicitada',
                    help_text='Cantidad solicitada',)
    quantity_transfer = models.FloatField(default=0, validators=[MinValueValidator(0.0)],
                    blank=True, null=True,
                    verbose_name='Cantidad a trasladar',
                    help_text='Cantidad a trasladar',)
    truck = models.ForeignKey('administration.TruckVehicleModel', on_delete=models.PROTECT, 
                            blank=True, null=True,
                            related_name='truck_detail_transfer',
                            verbose_name="Remolque que se utilizará",
                            help_text="Remolque que se utilizará en el traslado")
    #Toneladas por remolque momento en que se genera carta porte en el paso 4
    ton_out = models.FloatField(default=0, validators=[MinValueValidator(0.0)], null=True, blank=True,
                                verbose_name="Peso de sálida (en toneladas)",
                                help_text="Peso con el que salió el vehículo de la planta") #Sale del almacén
    ton_receiver = models.FloatField(default=0, validators=[MinValueValidator(0.0)], null=True, blank=True,
                               verbose_name="Peso recibido por el cliente (en toneladas)",
                               help_text="Peso que entregó el vehiculo al cliente") #Entregado al cliente

class InvoiceModel(BaseModel):
    key_invoice = models.CharField(max_length=50, unique=True,
                    help_text='Folio de factura',
                    verbose_name='Folio de factura')
    order = models.OneToOneField('OrderModel', on_delete=models.CASCADE,
                    help_text='Pedido al que pertenece la factura',
                    verbose_name='Pedido')
    payment_method = models.PositiveSmallIntegerField(choices=CHOICES_PAYMENT_METHOD, default=0,
                    help_text='Método de pago',
                    verbose_name='Método de pago')
    total = models.FloatField(default=0, validators=[MinValueValidator(0.0)],
                    help_text='Total de la factura',
                    verbose_name='Total de la factura')
    subtotal = models.FloatField(default=0, validators=[MinValueValidator(0.0)],
                    help_text='Subtotal de la factura',
                    verbose_name='Subtotal de la factura')
    iva = models.FloatField(default=0, validators=[MinValueValidator(0.0)],
                    help_text='IVA de la factura',
                    verbose_name='IVA de la factura')
    #descuentos
    description = models.TextField(null=True, blank=True,
                    help_text='Descripción o notas asociadas a la factura',
                    verbose_name='Descripción/Notas de factura')

    class Meta:
        verbose_name_plural = "Facturas"
        verbose_name = "Factura"
        ordering = ['key_invoice']
        db_table = 'orders_invoice'

