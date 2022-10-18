from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Almacenista(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Almacenista',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Almacenista, self).save()

    class Meta:
        verbose_name_plural = "Almacenistas"
class Comprador(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Comprador Estandar',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Comprador, self).save()

    class Meta:
        verbose_name_plural = "Compradores"
class AuxCompras(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien hace compras express',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(AuxCompras, self).save()

    class Meta:
        verbose_name_plural = "Auxiliares de compras"
class Autorizador(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien hace compras express',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(AuxCompras, self).save()

    class Meta:
        verbose_name_plural = "Autorizadores"
class UsuarioCompras(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien hace compras express',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UsuarioCompras, self).save()

    class Meta:
        verbose_name_plural = "Usuarios que pueden comprar"
class Vigilante(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien hace compras express',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Vigilante, self).save()

    class Meta:
        verbose_name_plural = "Vigilantes"
        
class EditorBitacoras(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien hace compras express',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(EditorBitacoras, self).save()

    class Meta:
        verbose_name_plural = "Editor de Bitacoras"

class AutorizanteMLS(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien puede autorizar compras de ALR',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(AutorizanteMLS, self).save()

    class Meta:
        verbose_name_plural = "Editor de Bitacoras"

class AutorizanteGLS(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien puede autorizar planta',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(AutorizanteGLS, self).save()

    class Meta:
        verbose_name_plural = "Autorizante planta"
        
class AutorizanteALS(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien puede autorizar planta',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(AutorizanteALS, self).save()

    class Meta:
        verbose_name_plural = "Autorizante planta"

class ComprasALR(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien puede autorizar planta',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(ComprasALR, self).save()

    class Meta:
        verbose_name_plural = "Comprador Oficinas"
class ComprasOficinas(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien puede autorizar planta',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(ComprasOficinas, self).save()

    class Meta:
        verbose_name_plural = "Comprador Oficinas"
class ComprasPlanta(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Quien puede autorizar planta',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(ComprasPlanta, self).save()

    class Meta:
        verbose_name_plural = "Comprador Planta"
class AlmacenistaPlanta(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Almacenista',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(AlmacenistaPlanta, self).save()

    class Meta:
        verbose_name_plural = "Almacenistas"
class AlmacenistaOficina(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Almacenista',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(AlmacenistaOficina, self).save()

    class Meta:
        verbose_name_plural = "Almacenistas"
class CXP(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Cuentas por pagar',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(CXP, self).save()

    class Meta:
        verbose_name_plural = "ComprasPorPagar"
