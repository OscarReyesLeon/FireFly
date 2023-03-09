from django.db import models

class TipoModel(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'tipo'

class ProcesoModel(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'proceso'

class MaquinaModel(models.Model):
    nombre = models.CharField(max_length=50)
    proceso = models.ForeignKey(ProcesoModel, models.DO_NOTHING, db_column='proceso_id')
    tipo = models.ForeignKey(TipoModel, models.DO_NOTHING, db_column='tipo_id')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'maquina'

class LecturaModel(models.Model):
    maquina = models.ForeignKey(MaquinaModel, models.DO_NOTHING, db_column='maquina')
    valor = models.IntegerField()
    fecha = models.DateTimeField(db_column='fecha_hora')

    def __str__(self):
        return str(self.valor)

    class Meta:
        managed = False
        db_table = 'lectura'

