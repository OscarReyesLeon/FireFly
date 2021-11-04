from django.db import models

from bases.models import ClaseModelo

from django.core.validators import MaxValueValidator, MinValueValidator


class Equipo(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Equipo',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Equipo, self).save()

    class Meta:
        verbose_name_plural = "Equipos"


class Proceso(ClaseModelo):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Equipo'
    )

    def __str__(self):
        return '{}:{}'.format(self.equipo.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proceso, self).save()

    class Meta:
        verbose_name_plural = "Procesos"
        unique_together = ('equipo', 'descripcion')


class Autoriza(ClaseModelo):
    descripcion = models.CharField(
        max_length=3,
        help_text='Iniciales de quien autoriza',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Autoriza, self).save()

    class Meta:
        verbose_name_plural = "Autorizantes"


class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categoria"


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"


class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=200,
        unique=True
    )
    codigo_barra = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=200, unique=True)
    precio = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    existencia = models.FloatField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT, null=True, blank=True)
    proceso = models.ForeignKey(Proceso, on_delete=models.PROTECT, null=True, blank=True)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')


class Pedido(ClaseModelo):
    cantidad = models.PositiveIntegerField()
    comentario = models.CharField(max_length=200, null=True, blank=True)
    autpor = models.ForeignKey(Autoriza, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, default='X-Revisar')
    status2 = models.CharField(max_length=20, default='Proximo')
    precio_uni = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    preciotransaccion = models.FloatField(null=True, blank=True)
    articulo = models.CharField(max_length=35)
    proceso = models.CharField(max_length=15)
    UniMed = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    motivo_peticion = models.CharField(max_length=200, null=True, blank=True)
    fecha_aprobado = models.CharField(max_length=200, null=True, blank=True)
    fecha_requerido = models.CharField(max_length=200, null=True, blank=True)
    fecha_recotizado = models.CharField(max_length=200, null=True, blank=True)
    fecha_finalizado = models.CharField(max_length=200, null=True, blank=True)
    fecha_rechazo = models.CharField(max_length=200, null=True, blank=True)
    folio_ingreso = models.CharField(max_length=20, default='--')
    divisa = models.CharField(max_length=3, default='mxn')
    indentificador_estado = models.CharField(max_length=20, default='2')

    # Apunte consulta
    # cotizar = Pedido.objects.filter(indentificador_estado=2).order_by('-id')[:999].count()

    def save(self):
        self.preciotransaccion = float(float(int(self.cantidad)) * float(self.precio_uni))
        self.articulo = self.articulo.upper()
        self.proceso = self.proceso.upper()

        super(Pedido, self).save()


class Banco(ClaseModelo):
    descripcion = models.CharField(
        max_length=20,
        help_text='Bancos donde se paga nomina',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Banco, self).save()

    class Meta:
        verbose_name_plural = "Bancos"


class Empresa(ClaseModelo):
    descripcion = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Empresa, self).save()

    class Meta:
        verbose_name_plural = "Empresas"


class Genero(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Genero, self).save()

    class Meta:
        verbose_name_plural = "Genero"


class Estudios(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Estudios, self).save()

    class Meta:
        verbose_name_plural = "Estudios"


class Ecivil(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Ecivil, self).save()

    class Meta:
        verbose_name_plural = "Estadocivil"


class Parentescocontacto(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Parentescocontacto, self).save()

    class Meta:
        verbose_name_plural = "Parentescocontactos"


class Departamento(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Departamento, self).save()

    class Meta:
        verbose_name_plural = "Departamentos"


class Puesto(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Puesto, self).save()

    class Meta:
        verbose_name_plural = "Puestos"


class Empleado(ClaseModelo):
    nombre = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length=15, default="eliminar default")
    apellido_materno = models.CharField(max_length=15, default="eliminar default")
    rfc = models.CharField(max_length=13, unique=True, default=99)
    nss = models.CharField(max_length=11, unique=True, default=99)
    telefono_fijo = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], default=4427744366)
    telefono_celular = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],unique=True, default=4427744366)
    email = models.EmailField(unique=True, default="oscar@mercax.com")
    contacto_emergencia = models.CharField(max_length=20, default="eliminar default")
    telefono_emergencia = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], default=4427744366)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    nominaBanco = models.ForeignKey(Banco, on_delete=models.PROTECT, default=1)
    cuenta = models.IntegerField(validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)],unique=True, default=1000000001)
    clabe_banco = models.IntegerField(validators=[MinValueValidator(111111111111111111), MaxValueValidator(999999999999999999)], unique=True,default=999999999999999998)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        self.apellido_paterno = self.apellido_paterno.upper()
        self.apellido_materno = self.apellido_materno.upper()
        self.rfc = self.rfc.upper()
        self.nss = self.nss.upper()
        self.contacto_emergencia = self.contacto_emergencia.upper()
        super(Empleado, self).save()

    class Meta:
        verbose_name_plural = "Empleados"


class Computadora(ClaseModelo):
    descripcion = models.CharField(max_length=100)
    cpu = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    almacenamiento = models.CharField(max_length=20)
    tipoAl = models.CharField(max_length=3)
    macEth = models.CharField(max_length=17, unique=True, null=True, blank=True)
    macWifi = models.CharField(max_length=17, unique=True, null=True, blank=True)
    serie = models.CharField(max_length=40, unique=True)
    asignado = models.ForeignKey(Empleado, on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.descripcion, self.macEth, self.macWifi, self.serie)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.macEth = self.macEth.upper()
        self.macWifi = self.macWifi.upper()
        self.serie = self.serie.upper()
        super(Computadora, self).save()

    class Meta:
        verbose_name_plural = "Computadoras"


class Herramienta(ClaseModelo):
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    motivo_de_edicion = models.CharField(max_length=100, null=True, blank=True)
    serie = models.CharField(max_length=40, unique=True)
    asignado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion, self.macEth, self.macWifi, self.serie)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.serie = self.serie.upper()
        super(Herramienta, self).save()

    class Meta:
        verbose_name_plural = "Herramientas"
