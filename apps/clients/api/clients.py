from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.clients.serializers import ClientCompleteSerializer
from django.db import transaction
from django.urls import reverse
from django.contrib import messages
from rest_framework.exceptions import NotFound

def convert_array_directions(request):
    data = eval(request.data.get("data", "{}"))
    if 'address' in data:
        for address in data['address']:
            address["neighborhood"] = address["neighborhood"].get("id", None)
    return data
class ClientCreateCompleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            current_data = convert_array_directions(request)
            client_serializer = ClientCompleteSerializer(data=current_data)
            #validar o error
            client_serializer.is_valid(raise_exception=True)
            client_serializer.save()
            messages.success(request, "Información del cliente guardada exitosamente")
            return Response({
                "msg": "Información del cliente guardada exitosamente",
                "url_redirect": reverse("client:client_list")
            })
        return Response({'message': 'Hello, world!'})
    
class ClientGetUpdateCompleteAPIView(APIView):
    serializer_class = ClientCompleteSerializer
    model = serializer_class.Meta.model

    def get_object(self):
        pk = self.kwargs.get("pk", None)
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise NotFound("No se encontró el cliente")

    def get(self, request, *args, **kwargs):
        return Response(
            ClientCompleteSerializer(self.get_object()).data,
            status=200
        )
        
    def patch(self, request, *args, **kwargs):
        client = self.get_object()
        current_data = convert_array_directions(request)
        client_serializer = ClientCompleteSerializer(instance=client, data=current_data, partial=True)
        client_serializer.is_valid(raise_exception=True)
        client_serializer.save()
        return Response({
            "msg": "Información del cliente actualizada exitosamente",
        })