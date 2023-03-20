from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.urls import reverse
from django.contrib import messages
from rest_framework.exceptions import NotFound, ValidationError
from apps.orders.serializers import OrderSaveSerializer
from apps.orders.models import OrderModel
from apps.core.choices import (
    convert_to_choices,
    CHOICES_INVOICE_STATUS, CHOICES_ORDER_STATUS
)
class OrderOptionsInitialAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        data = {
            'order_status': convert_to_choices(CHOICES_ORDER_STATUS),
            'invoice_status': convert_to_choices(CHOICES_INVOICE_STATUS),
            'current_key_order': OrderModel.objects.get_next_key_order()
        }
        return Response(data)
    
class OrderValidateCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        key_order = request.query_params.get('key_order', None)
        id = request.query_params.get('id', None)
        if key_order:
            order = OrderModel.objects.filter(key_order=key_order)
            if id: order = order.exclude(id=id)
            if order.exists():
                raise ValidationError({'key_order': 'El folio de la orden ya existe'})
        return Response({})
    
    def post(self, request, *args, **kwargs):
        import json
        data = request.data.get("data", None)
        if isinstance(data, str):
            data = json.loads(data)
        serializer = OrderSaveSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
                messages.success(request, 'Se ha creado el pedido exitosamente')
        except Exception as e:
            print(e)
            raise ValidationError(e)
        return Response({
            'url_redirect': reverse('order:order_list')
        })
    
class OrderValidateGetUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        return Response(OrderSaveSerializer(instance=OrderModel.objects.get(id=kwargs.get('pk'))).data)
    
    def patch(self, request, *args, **kwargs):
        import json
        data = request.data.get("data", None)
        if isinstance(data, str):
            data = json.loads(data)
        serializer = OrderSaveSerializer(data=data, instance=OrderModel.objects.get(id=kwargs.get('pk')))
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save()
            messages.success(request, 'Se ha actualizado el pedido exitosamente')
        return Response({
            'url_redirect': reverse('order:order_list')
        })