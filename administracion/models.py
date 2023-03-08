from django.db import models
from bases.models import ClaseModelo
from django.conf.global_settings import AUTH_USER_MODEL
from django.core.validators import MinValueValidator

OPCIONES_PROCESO_ESTATUS = (
    (1, 'Remisión (Ingreso)'), #Persona1 -Levanta pedido (indica si se factura (0-1), nota de remisión)
    (2, 'Autorización y asignación de camión'), #Persona2- Autoriza pedido y asigna camión
    (3, 'Cáptura de salida'),  #Persona3-Captura datos de salida del almacen (piezas)
    (4, 'Salida del almacén'), #Bascula - Indica el tonelaje que lleva el chofer, peso y GPS (Se genera Carta porte)
    (5, 'Entregado'), #Chofer- Indica lo mismo que en la salida de báscula(peso,GPS, Imagen(?)) y se pasa a por facturar (si es 1)
    (7, 'Entrada a almacén'), #Chofer-Indica que el viaje ha finalizado.
    (8, 'Cáptura de entrada'), #Vigilante- Indica litros de diesel que recargó y cierra viaje
    (9, 'Finalizado'), #Fin del viaje
)

OPCIONES_FACTURA_PROCESO = (
    (0, 'Sin factura'),
    (1, 'Proceso con factura'),
    (2, 'Por facturar'),
    (3, 'Facturado')
)

OPCIONES_TIPO_CAMION = (
    (0, 'Vehiculo ligero'),
    (1, 'Vehiculo pesado'),
)

OPCIONES_TIPO_TRASLADO = (
    (0, 'Entrega')
)

OPCIONES_TIPO_BOMBA = (
    (0, 'Diesel'),
    (1, 'Gasolina'),
)

class CategoriaproductoModel(ClaseModelo): #Presentación
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class UnidadMedidaModel(ClaseModelo):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class ProductoModel(ClaseModelo):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    precio_base = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    categoria = models.ForeignKey(CategoriaproductoModel, on_delete=models.PROTECT)
    unidad_medida = models.ForeignKey(UnidadMedidaModel, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='producto/', null=True, blank=True)


# class BombaModel(ClaseModelo):
#     nombre = models.CharField(max_length=50, unique=True)
#     descripcion = models.CharField(max_length=100, null=True, blank=True)
#     tipo_bomba = models.PositiveSmallIntegerField(choices=OPCIONES_TIPO_BOMBA, default=0)

# class VehiculoModel(ClaseModelo):
#     numero_economico = models.CharField(max_length=5, unique=True, help_text='Numero de la unidad de Vehiculo')
#     placas = models.CharField(max_length=7, unique=True, help_text='placas sin guiones')
#     marca = models.CharField(max_length=20)
#     modelo = models.CharField(max_length=20)
#     notas = models.CharField(max_length=100, null=True, blank=True)
#     tipo_vehiculo=models.PositiveSmallIntegerField(choices=OPCIONES_TIPO_CAMION, default=0)
#     responsable = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    
# class ClienteModel(ClaseModelo):
#     razon_social = models.CharField(max_length=50, unique=True)
#     rfc = models.CharField(max_length=13, unique=True)
#     email = models.EmailField(max_length=50, null=True, blank=True)
#     telefono = models.CharField(max_length=10, null=True, blank=True)
#     nombre = models.CharField(max_length=50, null=True, blank=True)

# class CreditoModel(ClaseModelo):
#     descripcion = models.CharField(max_length=100, null=True, blank=True)
#     monto = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
#     fecha_limite = models.DateField(null=True, blank=True)
#     cliente = models.ForeignKey(ClienteModel, on_delete=models.PROTECT)

# class EstadoModel(ClaseModelo):
#     nombre = models.CharField(max_length=50, unique=True)

# class MunicipioModel(ClaseModelo):
#     nombre = models.CharField(max_length=50, unique=True)
#     estado = models.ForeignKey(EstadoModel, on_delete=models.PROTECT)

# class ColoniaModel(ClaseModelo):
#     nombre = models.CharField(max_length=50, unique=True)
#     municipio = models.ForeignKey(MunicipioModel, on_delete=models.PROTECT)
#     codigo_postal = models.CharField(max_length=5, null=True, blank=True)

# class DireccionClienteModel(ClaseModelo):
#     cliente = models.ForeignKey(ClienteModel, on_delete=models.PROTECT)
#     calle = models.CharField(max_length=50)
#     numero_interior = models.CharField(max_length=20, null=True, blank=True)
#     numero_exterior = models.CharField(max_length=20)
#     colonia = models.ForeignKey(ColoniaModel, on_delete=models.PROTECT)


# class PedidoModel(ClaseModelo):
#     clave_pedido = models.CharField(max_length=50, unique=True, help_text='Orden de compra')
#     estatus = models.PositiveSmallIntegerField(choices=OPCIONES_PROCESO_ESTATUS, default=1)
#     facturacion = models.PositiveSmallIntegerField(choices=OPCIONES_FACTURA_PROCESO, default=0)
#     fecha_entrega = models.DateField(null=True, blank=True)

# class TrasladoModel(ClaseModelo):
#     pedido = models.OneToOneField(PedidoModel, on_delete=models.CASCADE)
#     vehiculo = models.ForeignKey(VehiculoModel, on_delete=models.PROTECT, blank=True, null=True, related_name='vehiculo')
#     chofer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, related_name='chofer')
#     tipo_traslado = models.PositiveSmallIntegerField(choices=OPCIONES_TIPO_TRASLADO, default=0)
#     lugar_entrega = models.ForeignKey(DireccionClienteModel, on_delete=models.PROTECT)
#     km_salida = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
#     km_entrada = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
#     tonelaje_salida = models.FloatField(default=0, validators=[MinValueValidator(0.0)]) #Sale del almacén
#     tonelaje_entregado = models.FloatField(default=0, validators=[MinValueValidator(0.0)]) #Entregado al cliente
#     litros_recargados = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
#     bomba = models.ForeignKey(BombaModel, on_delete=models.PROTECT, null=True, blank=True)    
    
# class DetallesPedidoModel(ClaseModelo):
#     producto = models.ForeignKey(ProductoModel, on_delete=models.PROTECT)
#     pedido = models.ForeignKey(PedidoModel, on_delete=models.CASCADE)
#     cantidad_previa = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
#     cantidad = models.FloatField(default=0, validators=[MinValueValidator(0.0)])

# class LogPedidoModel(ClaseModelo):
#     pedido = models.ForeignKey(PedidoModel, on_delete=models.CASCADE)
#     estatus = models.PositiveSmallIntegerField(choices=OPCIONES_PROCESO_ESTATUS, default=1)
#     descripcion = models.TextField(null=True, blank=True)
#     cambios = models.JSONField(blank=True, null=True) #Cambios de PedidoModel y DetallesPedidoModel