from email.policy import default
from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from django.http import HttpResponse

from bases.models import ClaseModelo
from inv.models import Pedido, Banco, Empresa

from django.contrib.humanize.templatetags.humanize import intcomma


from django.core.validators import MaxValueValidator, MinValueValidator


class Proveedor(ClaseModelo):
    descripcion=models.CharField(max_length=100,unique=True)
    direccion=models.CharField(
        max_length=250,
        null=True, blank=True
        )
    contacto=models.CharField(
        max_length=100
    )
    telefono=models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email=models.CharField(
        max_length=250,
        null=True, blank=True
    )
    telefono2=models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email2=models.CharField(
        max_length=250,
        null=True, blank=True
    )
    bancoproveedor=models.ForeignKey(Banco,null=True, on_delete=models.PROTECT)
    cuentabanco= models.IntegerField(null=True, blank=True)
    clabeproveedor=models.CharField(max_length=18, null=True, blank=True)
    rfcproveedor=models.CharField(max_length=14, unique=True, blank=True, null=True)
    diascredito=models.IntegerField(null=True, blank=True)
    giro=models.CharField(max_length=50,null=True,blank=True)
    ubicacion=models.CharField(max_length=20,null=True,blank=True)
    nombrecomercial=models.CharField(max_length=70)
    @property
    def cuentabancoauto(self):
        if self.clabeproveedor:
            cuentabanco=self.clabeproveedor[-12:-1]
        else:
            cuentabanco="no-tiene-#C"
        return cuentabanco

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"

class UsoFactura(ClaseModelo):
    descripcion=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UsoFactura, self).save()

    class Meta:
        verbose_name_plural = "Usos Facturas"

class ComprasEnc(ClaseModelo):
    fecha_compra=models.DateField(null=True,blank=True)
    observacion=models.TextField(blank=True,null=True)
    no_factura=models.CharField(max_length=100,null=True,blank=True,default="Gastos en general (G03)")
    uso_factura=models.ForeignKey(UsoFactura,on_delete=models.PROTECT,null=True, blank=True)
    fecha_factura=models.DateField(null=True,blank=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    descuento2=models.FloatField(default=0)
    total=models.FloatField(default=0)
    empresaoc=models.ForeignKey(Empresa,on_delete=models.PROTECT, null=True)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    clienteuniqueid = models.CharField(max_length=100, null=True, blank=True)
    autorizacion = models.CharField(max_length=50, default="OC: Autorización Pendiente")
    @property
    def fechalistado(self):
        fechalistado = self.fm.strftime('%y-%m-%d %H:%M.%S')
        return fechalistado
    
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
        self.total = float(self.sub_total) + float(self.descuento) - float(self.descuento2)
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"

class ComprasDet(ClaseModelo):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    pedido=models.OneToOneField(Pedido,on_delete=models.CASCADE, blank=True, null=True)
    cantidad=models.FloatField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0, blank=True, null=True)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.pedido)

    def save(self):
        self.sub_total = float(float(float(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total + float(self.descuento)
        super(ComprasDet, self).save()
    class Mega:
        verbose_name_plural = "Detalles Ordenes"
        verbose_name="Detalle Ordenes"


@receiver(post_delete, sender=ComprasDet)
def detalle_compra_borrar(sender,instance, **kwargs):
    id_pedido = instance.pedido.id
    id_compra = instance.compra.id

    enc = ComprasEnc.objects.filter(pk=id_compra).first()
    if enc:
        sub_total = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('sub_total'))
        descuento = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        enc.sub_total=sub_total['sub_total__sum']
        enc.descuento=descuento['descuento__sum']
        enc.save()
    
    prod=Pedido.objects.filter(pk=id_pedido).first()
    if prod:
        prod.status='X asignar OC'
        prod.indentificador_estado='3'
        prod.save()

@receiver(post_save, sender=ComprasDet)
def detalle_compra_guardar(sender,instance,**kwargs):
    id_pedido = instance.pedido.id
    fecha_compra=instance.compra.fecha_compra

    prod=Pedido.objects.filter(pk=id_pedido).first()
    if prod:
        prod.status='en Proveedor'
        prod.indentificador_estado='4'
        prod.ultima_compra=fecha_compra
        prod.save()


