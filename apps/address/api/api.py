from apps.address.serializers import MunicipalitySerializer, NeighborhoodOptionsSerializer, StateSerializer
#LoginRequired
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GenericListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    param_name = None
    def filter_queryset(self, queryset):
        if self.param_name:
            param = self.request.query_params.get(self.param_name)
            if param:
                queryset = queryset.filter(**{self.param_name:param})
        return queryset

    def get_queryset(self):
        queryset = self.serializer_class.Meta.model.objects.all()
        queryset = self.filter_queryset(queryset)
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListStateAPIView(GenericListAPIView):
    serializer_class = StateSerializer
    param_id = None

class ListMunicipalityAPIView(GenericListAPIView):
    serializer_class = MunicipalitySerializer
    param_name = 'state_id'

class ListNeighborhoodAPIView(GenericListAPIView):
    serializer_class = NeighborhoodOptionsSerializer
    param_name = 'municipality_id'