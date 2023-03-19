from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.administration.serializers import (
    DriverOptionSerializer, ProductOptionSerializer,
    VehicleOptionSerializer, FuelPumpOptionSerializer,
    TruckVehicleOptionSerializer
)
class AdministarationInitialAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        
        return Response({
            'options_products': ProductOptionSerializer(ProductOptionSerializer.Meta.model.objects.all(), many=True).data,
            #Conductores, vehiculos y remolques, filtrar por activos
            'options_vehicles': VehicleOptionSerializer(VehicleOptionSerializer.Meta.model.objects.all(), many=True).data,
            'options_drivers': DriverOptionSerializer(DriverOptionSerializer.Meta.model.objects.all(), many=True).data,
            'options_trucks': TruckVehicleOptionSerializer(TruckVehicleOptionSerializer.Meta.model.objects.filter(
                is_active=True
            ), many=True).data,
            'options_fuel_pump': FuelPumpOptionSerializer(FuelPumpOptionSerializer.Meta.model.objects.all(), many=True).data,
        })