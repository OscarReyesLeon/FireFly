from django.db import models

from bases.models import ClaseModelo

from django.core.validators import MaxValueValidator, MinValueValidator

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
class Artciulosestandarizados (ClaseModelo):
    descripcion = models.CharField(max_length=50, unique=True, null=False, blank=False)
    fechapreciosugerido = models.DateTimeField(auto_now_add=True) 
    preciosugerido = models.FloatField(default=0)
    fecha2 = models.DateTimeField(null=True, blank=True)
    precio2 = models.FloatField(default=0)
    fecha3 = models.DateTimeField(null=True, blank=True)
    precio3 = models.FloatField(default=0)
    fecha4 = models.DateTimeField(null=True, blank=True)
    precio4 = models.FloatField(default=0)
    def __str__(self):
        return '{}'.format(self.descripcion)
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

class Nombresrelacion (ClaseModelo):
    descripcion = models.CharField(max_length=50, blank=False, null=False, unique=True)
    relacion = models.ForeignKey(Artciulosestandarizados, on_delete=models.PROTECT)
    def __str__(self):
        return '{}'.format(self.descripcion)
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Equipos"
class Equipo(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Equipo',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')


class Pedido(ClaseModelo):
    cantidad = models.FloatField()
    comentario = models.CharField(max_length=200, null=True, blank=True)
    autpor = models.ForeignKey(Autoriza, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, default='Cotizando')
    status2 = models.CharField(max_length=20, null=True, blank=True)
    precio_uni = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    preciotransaccion = models.FloatField(null=True, blank=True)
    articulo = models.CharField(max_length=50, null=True, blank=True, default='NA')
    proceso = models.CharField(max_length=15)
    UniMed = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    motivo_peticion = models.CharField(max_length=200, null=True, blank=True, default='NA')
    fecha_aprobado = models.CharField(max_length=200, null=True, blank=True)
    fecha_requerido = models.CharField(max_length=200, null=True, blank=True)
    fecha_recotizado = models.CharField(max_length=200, null=True, blank=True)
    fecha_finalizado = models.CharField(max_length=200, null=True, blank=True)
    fecha_rechazo = models.CharField(max_length=200, null=True, blank=True)
    folio_ingreso = models.CharField(max_length=20, default='--')
    divisa = models.CharField(max_length=3, default='MXN')
    indentificador_estado = models.CharField(max_length=20, default='1')
    iva = models.FloatField(default=.16)
    recibidos = models.FloatField(default=0)
    estandarizadoprodu = models.ForeignKey(Artciulosestandarizados, null=True, blank=True, on_delete=models.PROTECT)
    @property
    def estandarizadorq(self):
        abuscar = self.articulo
        abuscar = abuscar.upper()
        if Nombresrelacion.objects.filter(descripcion=abuscar).exists():
            respuesta = "si"
        else:
            respuesta = "no"
        return respuesta
    @property
    def variacion(self):
        abuscar = self.articulo
        abuscar = abuscar.upper()
        if Nombresrelacion.objects.filter(descripcion=abuscar).exists():
            respuesta = Nombresrelacion.objects.filter(descripcion=abuscar).get()
            respuesta = respuesta.relacion.preciosugerido
            respuesta = self.precio_uni - respuesta
        else:
            respuesta = 0.0001
        return respuesta
    @property
    def descripcioncorregida(self):
        abuscar = self.articulo
        abuscar = abuscar.upper()
        if Nombresrelacion.objects.filter(descripcion=abuscar).exists():
            respuesta = Nombresrelacion.objects.filter(descripcion=abuscar).get()
            respuesta = respuesta.relacion.descripcion
        else:
            respuesta = "No"
        return respuesta
    @property
    def idestandarizado(self):
        abuscar = self.articulo
        abuscar = abuscar.upper()
        if Nombresrelacion.objects.filter(descripcion=abuscar).exists():
            respuesta = Nombresrelacion.objects.filter(descripcion=abuscar).get()
            respuesta = respuesta.relacion.id
        else:
            respuesta = 1
        return respuesta

    @property
    def oc(self):
        from cmp.models import ComprasDet
        if ComprasDet.objects.filter(pedido_id=self.id).exists() == True:
            numeroOC = ComprasDet.objects.filter(pedido_id=self.id).get()
            numeroOC = numeroOC.compra_id
            return numeroOC
        else:
            numeroOC = "Sin orden de compras"
            return numeroOC
    @property
    def proveedoroc(self):
        from cmp.models import ComprasDet, ComprasEnc, Proveedor
        if ComprasDet.objects.filter(pedido_id=self.id).exists() == True:
            proveedorOC = ComprasDet.objects.filter(pedido_id=self.id).get()
            proveedorOC = proveedorOC.compra_id
            proveedorOC = ComprasEnc.objects.filter(id=proveedorOC).get()
            proveedorOC = proveedorOC.proveedor_id
            proveedorOC = Proveedor.objects.filter(id=proveedorOC).get()
            proveedorOC = proveedorOC.descripcion
            return proveedorOC
        else:
            proveedorOC = "sin proveedor de OC registrado"
            return proveedorOC
    @property
    def precio_uni_iva(self):
        precioiva = self.precio_uni * self.iva
        return precioiva
    @property
    def precio_unimasiva(self):
        unitario = self.precio_uni
        ivapuro = self.iva
        ivaoperacion = unitario * ivapuro
        precioiva = unitario + ivaoperacion
        return precioiva
    @property
    def transaccion_iva(self):
        transaccion = self.preciotransaccion
        ivapuro = self.iva
        preciotransaccion_iva = transaccion * ivapuro
        return preciotransaccion_iva
    @property
    def transaccionconiva(self):
        transaccion = self.preciotransaccion
        ivapuro = self.iva
        ivaoperacion = transaccion * ivapuro
        preciotransaccioniva = transaccion + ivaoperacion
        return preciotransaccioniva
    # Apunte consulta
    # cotizar = Pedido.objects.filter(indentificador_estado=2).order_by('-id')[:999].count()
    def save(self, *args, **kwargs):
        self.preciotransaccion = float(float(self.cantidad)) * float(self.precio_uni)
        self.proceso = self.proceso.upper()
        self.proceso = self.proceso.replace("'","")

        estandar = Artciulosestandarizados.objects.filter(descripcion=self.articulo)
        if estandar.exists():
            self.estandarizadoprodu = estandar.first()
            self.motivo_peticion = self.estandarizadoprodu.descripcion
            self.articulo = self.estandarizadoprodu.descripcion
        elif self.articulo != 'NA' and self.motivo_peticion == 'NA':
            self.articulo = self.articulo.upper()
            self.articulo = self.articulo.replace("'", "")
            self.articulo = normalize(self.articulo)
            self.motivo_peticion = self.articulo
        super().save(*args, **kwargs)

"""       if self.estandarizadoprodu is None:
            self.motivo_peticion = chr(abuscar)
        else:
            self.motivo_peticion = self.estandarizadoprodu.descripcion"""

"""        if self.estandarizadoprodu == 0:
            if Nombresrelacion.objects.filter(descripcion=abuscar).exists():
                preciosug = Nombresrelacion.objects.filter(descripcion=abuscar).get()
                nombrecorrecto = preciosug.relacion.descripcion
                self.motivo_peticion = nombrecorrecto
                preciosug = preciosug.relacion.preciosugerido
                self.precio_uni = preciosug
            else:
                pass
        else:
            self.motivo_peticion = self.articulo"""





class Banco(ClaseModelo):
    descripcion = models.CharField(
        max_length=20,
        help_text='Bancos',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Bancos"


class Empresa(ClaseModelo):
    descripcion = models.CharField(
        max_length=50,
        unique=True,
    )
    razonsocial = models.CharField(max_length=200, null=True, blank=True)
    direccionfiscal = models.CharField(max_length=200, null=True, blank=True)
    direccionentrega = models.CharField(max_length=200, null=True, blank=True)
    rfcempresa = models.CharField(max_length=13, null=True, blank=True)
    urllogoempresa = models.CharField(max_length=100, null=True, blank=True)
    horarios = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        self.rfcempresa = self.rfcempresa.upper()
        self.razonsocial = self.razonsocial.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Empresas"


class Genero(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Genero"


class Estudios(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Estudios"


class Ecivil(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Estadocivil"


class Parentescocontacto(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Parentescocontactos"


class Departamento(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Departamentos"


class Puesto(ClaseModelo):
    descripcion = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Puestos"



class Empleado(ClaseModelo):
    nombre = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    rfc = models.CharField(max_length=13, unique=True)
    nss = models.CharField(max_length=11, unique=True)
    telefono_fijo = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    telefono_celular = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],unique=True)
    email = models.EmailField(unique=True)
    contacto_emergencia = models.CharField(max_length=20)
    telefono_emergencia = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    nominaBanco = models.ForeignKey(Banco, on_delete=models.PROTECT)
    cuenta = models.BigIntegerField(validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)],unique=True)
    clabe_banco = models.BigIntegerField(validators=[MinValueValidator(99999999999999999), MaxValueValidator(999999999999999999)], unique=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)


    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido_paterno = self.nombre.upper()
        self.apellido_materno = self.nombre.upper()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        self.macEth = self.macEth.upper()
        self.macWifi = self.macWifi.upper()
        self.serie = self.serie.upper()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        self.serie = self.serie.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Herramientas"

class Almacen(ClaseModelo):
    descripcion = models.CharField(max_length=10)
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

class Tipomovimiento(ClaseModelo):
    descripcion = models.CharField(max_length=10)
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

class Existencias(ClaseModelo):
    pedidoorigen = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    codigobarras = models.CharField(max_length=4296, null=False, blank=False)
    almacen = models.ForeignKey(Almacen, on_delete=models.PROTECT)
    posi1 = models.CharField(max_length=3)
    posi2 = models.CharField(max_length=3)
    posi3 = models.CharField(max_length=3)

class Bitacoramov(ClaseModelo):
    movido = models.ForeignKey(Existencias, on_delete=models.PROTECT)
    tipomov = models.ForeignKey(Tipomovimiento, on_delete=models.PROTECT)
    oposi1 = models.CharField(max_length=3)
    oposi2 = models.CharField(max_length=3)
    oposi3 = models.CharField(max_length=3)
    nposi1 = models.CharField(max_length=3)
    nposi2 = models.CharField(max_length=3)
    nposi3 = models.CharField(max_length=3)