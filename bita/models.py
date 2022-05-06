from django.db import models
from django.contrib.auth.models import User

from bases.models import ClaseModelo
from inv.models import Empresa, Pedido
from cmp.models import  Proveedor
# Create your models here.
class OperadorPesado(ClaseModelo):
    nombre = models.CharField(max_length=50,unique=True,help_text="Nombres y Apellidos")
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(OperadorPesado, self).save()
    class Meta:
        verbose_name_plural = 'Operadores de camiones pesados'

class SolicitantesUtilitario(ClaseModelo):
    nombre = models.CharField(max_length=50,unique=True,help_text="Nombres y Apellidos")
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(SolicitantesUtilitario, self).save()
    class Meta:
        verbose_name_plural = 'Autorizados para pedir utilitarios'

class VehiculoLigero(ClaseModelo):
    numeroeconomico = models.CharField(max_length=5, unique=True, help_text='Numero de la unidad de Vehiculo')
    placas = models.CharField(max_length=7, unique=True, help_text='placas sin guiones')
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    notas = models.CharField(max_length=100, null=True, blank=True)
    responsable = models.ForeignKey(SolicitantesUtilitario, on_delete=models.PROTECT)
    def __str__(self):
        return '{}'.format(self.numeroeconomico)
    def save(self):
        self.numeroeconomico = self.numeroeconomico.upper()
        self.placas = self.placas.upper()
        self.modelo = self.modelo.upper()
        super(VehiculoLigero, self).save()
    class Meta:
        verbose_name_plural = 'Vehiculos Ligeros'

class VehiculoPesado(ClaseModelo):
    numeroeconomico = models.CharField(max_length=5, unique=True, help_text='Numero de la unidad de Vehiculo')
    placas = models.CharField(max_length=7, unique=True, help_text='placas sin guiones')
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    notas = models.CharField(max_length=100, null=True, blank=True)
    responsable = models.ForeignKey(OperadorPesado, on_delete=models.PROTECT)
    def __str__(self):
        return '{}'.format(self.numeroeconomico)
    def save(self):
        self.numeroeconomico = self.numeroeconomico.upper()
        self.placas = self.numeroeconomico.upper()
        self.modelo = self.modelo.upper()
        super(VehiculoPesado, self).save()
    class Meta:
        verbose_name_plural = 'Vehiculos Pesados'

class ReciboEntrega(ClaseModelo):
    movimiento = models.CharField(max_length=7, help_text='recibo o entrega')
    def __str__(self):
        return '{}'.format(self.movimiento)
    def save(self):
        self.movimiento = self.movimient.upper()
        super(ReciboEntrega, self).save()
    class Meta:
        verbose_name_plural = 'Recibo o entrega'
class LlavesEnResguardo(ClaseModelo):
    movimiento = models.ForeignKey(ReciboEntrega, on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(VehiculoPesado, on_delete=models.PROTECT)
    involucrado = models.ForeignKey(OperadorPesado, on_delete=models.PROTECT, help_text='Nombre de quien se recibe o entrega las llaves')
    golpes = models.BooleanField(default=False, help_text='¿Gopes nuevos?')
    tarjeta = models.BooleanField(default=True, help_text='Tarjeta de circulación')
    poliza = models.BooleanField(default=True, help_text='Poliza de seguro')
    notas = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.vehiculo)
    class Meta:
        verbose_name_plural = 'Llaves en resguardo'

class MotivoIngresoUnidad(ClaseModelo):
    motivo = models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.motivo)
    def save(self):
        self.motivo = self.motivo.upper()
        super(MotivoIngresoUnidad, self).save()
    class Meta:
        verbose_name_plural = 'Motivos de ingresos'

class IngresoUnidadPesada(ClaseModelo):
    vehiculo = models.ForeignKey(VehiculoPesado, on_delete=models.PROTECT)
    operador = models.ForeignKey(OperadorPesado, on_delete=models.PROTECT)
    motivo = models.ForeignKey(MotivoIngresoUnidad, on_delete=models.PROTECT)
    fsalida = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.vehiculo)
    class Meta:
        verbose_name_plural = 'Ingresos de unidades pesadas'

class TanquesDiesel(ClaseModelo):
    nombre = models.CharField(max_length=50,unique=True,help_text="Banco, Patio, Planta, ETC.")
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(TanquesDiesel, self).save()
    class Meta:
        verbose_name_plural = 'Tanques de Diesel'

"""Modelo donde la pipa descarga diesel"""
class DescargaDeDiesel(ClaseModelo):
    pedido = models.OneToOneField(Pedido, on_delete=models.PROTECT)
    tanquedediesel = models.ForeignKey(TanquesDiesel, on_delete=models.PROTECT, help_text="en donde se descarga?")
    residual = models.FloatField(null=True, blank=True)
    litrosenbomba = models.FloatField(null=True, blank=True)
    """
    def save(self):
        resilitros = DescargaDeDiesel.objects.filter(tanquedediesel=self.tanquedediesel).order_by('-id')[:1]
        if not resilitros:
            self.residual = 0
        else:
            pass
            """

    def __str__(self):
        return '{}:{}'.format(self.pedido.id, self.pedido)
class DestinosClientes(ClaseModelo):
    descripcion = models.CharField(
        max_length=50,
        unique=True,
        help_text='Nombre Sucursal'
    )
    razonsocial = models.CharField(max_length=200, null=True, blank=True)
    direccionfiscal = models.CharField(max_length=200, null=True, blank=True)
    direccionentrega = models.CharField(max_length=200, null=True, blank=True)
    rfcempresa = models.CharField(max_length=13, null=True, blank=True)
    horarios = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.razonsocial = self.razonsocial.upper()
        self.rfcempresa = self.rfcempresa.upper()
        super(DestinosClientes, self).save()

class CargaDeDiesel(ClaseModelo):
    vehiculo = models.ForeignKey(VehiculoPesado, on_delete=models.PROTECT)
    litros = models.FloatField()
    destino = models.ForeignKey(DestinosClientes, on_delete=models.PROTECT)

class CargaDeUrea(ClaseModelo):
    vehiculo = models.ForeignKey(VehiculoPesado, on_delete=models.PROTECT)
    operador = models.ForeignKey(OperadorPesado, on_delete=models.PROTECT)
    litros = models.FloatField()

class MotivoVisita(ClaseModelo):
    descripcion = models.CharField(max_length=50, help_text='RH, Proveedor, etc')
    def __str__(self):
        return '{}'.format(self.descripcion) 
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(MotivoVisita, self).save()

class Visitantes(ClaseModelo):
    nombre = models.CharField(max_length=50)
    visitaa = models.CharField(max_length=50)
    motivo = models.ForeignKey(MotivoVisita, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, null=True, blank=True, help_text="Si es proveedor, selecciona aquí")
    placas = models.CharField(max_length=7, unique=True, help_text='placas sin guiones')
    temperatura = models.FloatField()
    horasalida = models.DateTimeField(null=True, blank=True)
