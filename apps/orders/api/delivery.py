from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.urls import reverse
from django.contrib import messages
from rest_framework.exceptions import NotFound, ValidationError
from apps.orders.serializers import OrderSaveSerializer, OrderWarehouseSerializer, DetailOrderSerializer
from apps.orders.models import OrderModel
import json
from apps.core.choices import (
    convert_to_choices,
    CHOICES_INVOICE_STATUS, CHOICES_ORDER_STATUS
)
class OrderSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        key_order = request.query_params.get('key_order', None)
        delivery = request.query_params.get('step', None)
        if key_order:
            order = OrderModel.objects.filter(key_order=key_order)
            if not order.exists():
                raise ValidationError({'msg': 'El folio de la orden no existe'})    
            order = order.first()
            msg = None
            disabled = True
            if delivery == 'exit_warehouse': #Cuando se va a capturar las toneladas antes de salir
                if order.status < 4:
                    msg = 'El folio de la orden aún no puede ser despachada'
                if order.status > 4:
                    msg = 'El folio de la orden ya fue despachada'
                disabled = order.status != 4
            elif delivery == 'delivery_customer': #Cuando el chofer captura las toneladas que entrego al cliente
                if order.status < 5:
                    msg = 'El folio de la orden aún no puede ser entregada al cliente'
                if order.status > 5:
                    msg = 'El folio de la orden ya fue entregada al cliente'
                disabled = order.status != 5
            elif delivery == 'return_warehouse': #Cuando el chofer indica que ya regreso al almacén/fin del viaje
                if order.status < 6:
                    msg = 'El traslado aún no puede ser finalizado'
                if order.status > 6:
                    msg = 'El traslado ya fue finalizado'
                disabled = order.status != 6
            elif delivery == 'fuel_capture': #Cuando se va a capturar el combustible, al capturar, se finaliza el viaje
                if order.status < 7:
                    msg = 'No puedes capturar el combustible si el viaje aún no se ha finalizado'
                if order.status > 7:
                    msg = 'El viaje ya fue finalizado y el combustible ya fue capturado'
                disabled = order.status != 7
            return Response({
                'order': OrderWarehouseSerializer(instance=order).data,
                "disabled": disabled,
                'msg': msg,
                'status': order.get_status_display(),
            })
        raise ValidationError({'msg': 'Sin información '})
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.data.get("data", None))
        if data:
            instance = OrderModel.objects.get(pk=data.get('id', None))
            serializer = OrderSaveSerializer(instance=instance, data=data, partial=True,
                context={'request': request, 'save_ton': True }
                                             )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({'msg': 'ok'})
