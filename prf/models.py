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
        verbose_name_plural = "Equipos"
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
        verbose_name_plural = "Equipos"
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
        verbose_name_plural = "Equipos"
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
        verbose_name_plural = "Equipos"
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
        verbose_name_plural = "Equipos"
