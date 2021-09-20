class Requisicion(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    cantidad = models.CharField(max_length=50)
    """descripcion = models.CharField(max_length=200)"""
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    proceso = models.ForeignKey(Proceso, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Requisicion,self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_barra')