from django.db import models
from bases.models import ClaseModelo


# Create your models here.
class DieselPiusiCar(ClaseModelo):
    stockinliter = models.FloatField(help_text="Stock en litros")
    tanklevel = models.FloatField(help_text="MM")
    tankporcentage = models.FloatField(help_text="Porcentaje")
    date = models.CharField(max_length=100)
    dispenseliters = models.FloatField(help_text="Litros despachados")
    odometer = models.FloatField(help_text="Odometro")
    presetvolume = models.FloatField(help_text="?")
    vehicleplate = models.CharField(max_length=20, help_text="Placas")
    drivername = models.CharField(max_length=50, help_text="Nombre conductor")
    partnumber = models.IntegerField(help_text="Numero de parte en enero")
    workorder = models.IntegerField(help_text="Numero de orden")
    dispenseridentifier = models.CharField(max_length=50, help_text="Identificador de bomba")
    time = models.CharField(max_length=50, help_text="texto")
    dispensername = models.CharField(max_length=50, help_text="Nombre de la bomba")
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(DieselPiusiCar, self).save()
    class Meta:
        verbose_name_plural = 'Carga de Diesel'
