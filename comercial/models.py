from django.db import models
from bases.models import ClaseModelo

import string
import random


# Create your models here.
def normalize(s):
    replacements = (
        ("á", "A"),
        ("é", "E"),
        ("í", "I"),
        ("ó", "O"),
        ("ú", "U"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
def clave_generator(size=40, chars=string.ascii_letters + string.digits):
    verificadorid = ''.join(random.choice(chars) for _ in range(size))
    repetidocheck = Pedidos.objects.filter(claveunica=verificadorid).exists()
    while repetidocheck == True:
        verificadorid = ''.join(random.choice(chars) for _ in range(size))
        repetidocheck = Pedidos.objects.filter(claveunica=verificadorid).exists()
    return verificadorid


class ProductoC(ClaseModelo):
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="descripción")
    def __str__(self):
        return self.descripcion
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)
class Presentacion(ClaseModelo):
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="descripción")
    def __str__(self):
        return self.descripcion
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)
class EstadoRepublica(ClaseModelo):
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="Nombre del Estado de la Republica")
    def __str__(self):
        return self.descripcion
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)
class ClienteC(ClaseModelo):
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="Nombre común o comercial")
    razonSocial = models.CharField(max_length=120, unique=True, verbose_name="Razón Social")
    rfc = models.CharField(max_length=13, unique=True, verbose_name="RFC")
    nombreContacto = models.CharField(max_length=20, verbose_name="Nombre del contacto")
    email = models.EmailField()
    telefono = models.PositiveIntegerField()
    diasCredito = models.PositiveIntegerField(verbose_name="Dias de credito")
    credito = models.FloatField(default=0.00, verbose_name="Credito Autorizado")
    def __str__(self):
        return self.razonSocial
    def save(self, *args, **kwargs):
        self.descripcion = normalize(self.descripcion)
        self.razonSocial = normalize(self.razonSocial)
        self.rfc = normalize(self.rfc)
        self.nombreContacto = normalize(self.nombreContacto)
        self.email = normalize(self.email)
        super().save(*args, **kwargs)
class LugarEntrega(ClaseModelo):
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="Nombre común")
    cliente = models.ForeignKey(ClienteC, on_delete=models.PROTECT, verbose_name="Razon Social")
    numero = models.CharField(max_length=10, verbose_name="Numero de la calle")
    calle = models.CharField(max_length=10, verbose_name="Calle")
    colonia = models.CharField(max_length=10, verbose_name="Colonia")
    municipio = models.CharField(max_length=10, verbose_name="Municipio")
    EstadoRepublica = models.ForeignKey(EstadoRepublica, on_delete=models.PROTECT)
    codigoPostal = models.PositiveIntegerField(verbose_name="Codigo Postal")
    def __str__(self):
        return self.descripcion
    def save(self, *args, **kwargs):
        self.descripcion = normalize(self.descripcion)
        self.cliente = normalize(self.cliente)
        self.calle = normalize(self.calle)
        self.colonia = normalize(self.colonia)
        self.municipio = normalize(self.municipio)
        super().save(*args, **kwargs)
class Pedidos(ClaseModelo):
    claveunica = models.CharField(max_length=150, unique=True, verbose_name="identificador Aleatorio")
    producto = models.ForeignKey(ProductoC, on_delete=models.PROTECT, verbose_name="Producto")
    presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT, verbose_name="Tipo de empaque")
    cantidad = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name="Cantidad en Toneladas")
    fEntrega = models.DateField()
    lEntrega = models.ForeignKey(LugarEntrega, on_delete=models.PROTECT, verbose_name="Lugar de entrega")
    estadoRef = models.CharField(max_length=20, default="Capturado", verbose_name="Estado de pedido")
    facturado = models.BooleanField()
    timbre = models.CharField(max_length=20, default="No timbrado", verbose_name="Verificador de timbrado")
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="Nombre del Estado de la Republica")
    def __str__(self):
        return self.id
    def save(self, *args, **kwargs):
        self.claveunica = clave_generator()
        super().save(*args, **kwargs)
        
##inician los modelos para el modulo de traslados
class BombaDiesel(ClaseModelo):
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="descripción")
    def __str__(self):
        return self.descripcion
    def save(self, *args, **kwargs):
        self.descripcion = normalize(self.descripcion)
        super().save(*args, **kwargs)
class TrasladoTipo(ClaseModelo):
    descripcion = models.CharField(max_length=10, unique=True, verbose_name="descripción")
    def __str__(self):
        return self.descripcion
    def save(self, *args, **kwargs):
        self.descripcion = normalize(self.descripcion)
        super().save(*args, **kwargs)

class Traslado(ClaseModelo):
    pedidoClave = models.OneToOneField(Pedidos, on_delete=models.PROTECT, verbose_name="Clave del pedido")
    fEntrega = models.DateField(null=True, blank=True)
    fRegreso = models.DateField(null=True, blank=True)
    kmtoma = models.PositiveIntegerField(verbose_name="Kilometraje inicial", null=True, blank=True)
    kmentrega = models.PositiveIntegerField(verbose_name="Kilometraje de entrega", null=True, blank=True)
    kmfinal = models.PositiveIntegerField(verbose_name="Kilometraje final", null=True, blank=True)
    ubitoma = models.CharField(max_length=10, verbose_name="Ubicacion inicial", null=True, blank=True)
    ubientrega = models.CharField(max_length=10, verbose_name="Ubicacion de entrega", null=True, blank=True)
    ubifinal = models.CharField(max_length=10, verbose_name="Ubicacion final", null=True, blank=True)
    tonelajeDeclarado = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name="Tonelaje declarado", null=True, blank=True)
    tonelajeEntregado = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name="Tonelaje entregado", null=True, blank=True)
    litrosRecarga = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name="Litros de recarga", null=True, blank=True)
    bomba = models.ForeignKey(BombaDiesel, on_delete=models.PROTECT, verbose_name="Bomba de diesel")
    trasladoTipo = models.ForeignKey(TrasladoTipo, on_delete=models.PROTECT, verbose_name="Tipo de traslado")
    
    
    
##https://conectia.mx/
##https://timbradorxpress.mx/xml.html