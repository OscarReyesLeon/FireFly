from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PermissionOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        groups_user = request.user.groups.all()
        if request.user.is_superuser:
            capture_order = autorize_order = exit_order = super_user = True
        else:
            super_user = False
            capture_order = groups_user.filter(name='CAPTURISTA_ORDEN').exists()
            autorize_order = groups_user.filter(name='AUTORIZAR_ORDEN').exists()
            exit_order = groups_user.filter(name='CAPTURISTA_TRASLADO').exists()
        default_permissions = {
            "autorize_order": False, #Habilitar el boton de autorización
            "change_product": False, #Pueda cambiar el producto
            "delete_product": False, #Eliminar un producto
            "add_product": False, #Añadir un producto

            "quantity_order": False, #Cambiar cantidad en la orden
            "quantity_transfer": False, #Cambiar cantidad en el traslado
            "ton_out": False, #Capturar toneladas de salida
            
            "asign_vehicle": False, #Asignar un vehículo
            "asign_truck": False, #Asignar un remolque
            "asign_pump": super_user, #Asignar una bomba
            
            "super_user": super_user, #Todos los permisos habilitados
            "detail_view": False #Marcar todos los campos como solo lectura
        }

        if capture_order or autorize_order:
            default_permissions.update({
                "add_product": True,
                "delete_product": True,
                "change_product": True,
                "quantity_order": True,
            })
        if autorize_order or exit_order:
            default_permissions.update({
                "asign_vehicle": True,
                "asign_truck": True,
            })
        if autorize_order:
            default_permissions.update({
                "autorize_order": True,
            })
        if exit_order:
            default_permissions.update({
                "quantity_transfer": True,
                "ton_out": True,
            })

        return Response(default_permissions)