from rest_framework import serializers
from inv.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    preciotransaccion = serializers.IntegerField()
    fc = serializers.DateTimeField(format="%d/%m/%Y %H:%M")
    fm = serializers.DateTimeField(format="%d/%m/%Y %H:%M")
    autpor = serializers.CharField(source='autpor.descripcion')
    uc = serializers.CharField(source='uc.username')
    motivo_peticion2 = serializers.CharField(source='motivo_peticion')
    class Meta:
        model = Pedido
        fields = (
            'id', 'autpor','status2', 'uc', 'motivo_peticion', 'descripcioncorregida', 'cantidad', 'UniMed', 
            'divisa', 'precio_uni', 'iva', 'preciotransaccion', 'status', 'proceso', 
            'fc', 'fm', 'fecha_recotizado', 'fecha_aprobado', 'fecha_requerido','fecha_finalizado', 'fecha_rechazo', 
            'motivo_peticion2', 'comentario','indentificador_estado', 'folio_ingreso', 'folio_ingreso', 'proveedoroc' ,)

        nombre_columnas = (
            'ID', 'PA', 'Autorizado', 'Solicitante', 'Articulo', 'Corregido', 'Cantidad', 'Unidad Medida',
            'Divisa', '$ Unitario', 'IVA', '$ Total', 'Estado', 'Proceso',
            'F-Registro', 'F-Modificado', 'F-Cotizado', 'F-Aprobado', 'F-Proveedor',  'F-Finalizado', 'F-Rechazo',
            'OC Descripción', 'Comentario', 'IO', 'Proveedor Directo', 'Proveedor de OC'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data