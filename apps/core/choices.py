CHOICES_ORDER_STATUS = (
    (1, 'Remisión (Ingreso)'), #Persona1 -Levanta pedido (indica si se factura (0-1), nota de remisión)
    (2, 'Autorización y asignación de camión'), #Persona2- Autoriza pedido y asigna camión
    (3, 'Cáptura de salida'),  #Persona3-Captura datos de salida del almacen (piezas)
    (4, 'Salida del almacén'), #Bascula - Indica el tonelaje que lleva el chofer, peso y GPS (Se genera Carta porte)
    #Se bloquea el pedido y ya no se actualiza nada
    (5, 'Entregando'), #Chofer- Indica lo mismo que en la salida de báscula(peso,GPS, Imagen(?)) y se genera factura
    (6, 'Entrada a almacén'), #Chofer-Indica que el viaje ha finalizado.
    (7, 'Cáptura de entrada'), #Vigilante- Indica litros de diesel que recargó y cierra viaje
    (8, 'Finalizado'), #Fin del viaje
)
"""
Paso 4: Salida del almacén
    - Se genera carta porte
    - Se toma captura de GPS (latitud, longitud, velocidad, odometro (km))
    - Chofer indica toneladas con las que sale cada remolque
Paso 5:
    - Chofer indica TON entregadas
    -  API GPS (latitud, longitud, velocidad, odometro (km)) #Salida
    - Se genera factura
Paso 6:
    - Check del Chofer indica que el viaje ha finalizado
    - API GPS (latitud, longitud, velocidad, odometro (km))
    - Chofer pasa a estar disponible
Paso 7:
    - Usuario indica litros de diesel que recargó
    - Se cierra viaje y vehiculo-remolque-chofer pasan a estar disponibles
    - API GPS (latitud, longitud, velocidad, odometro (km)) #Entrada
Paso 8:
    - Fin del viaje
"""

# cliente A -> Ruta Planta A a Cliente A = 200 KM , 200*2=400KM ->  700KM -> 300KM consumo extra

"""
Salida - Entrada = KM recorridos
Litros gasto = N litros
KM/L = KM recorridos / N litros para X camion (ultimo mes)

Direccion A -> 100 KM
Camion A por 100km = 100 * km/L = 100 * 10 = 1000 litros
Cargue litros: 1200 -> 1050 - 1200 = 200 litros
"""


CHOICES_INVOICE_STATUS = (
    (0, 'Sin factura'),
    (1, 'Proceso con factura'),
    (2, 'Por facturar'),
    (3, 'Facturado')
)

CHOICES_TYPE_VEHICLE = (
    (0, 'Vehiculo ligero'),
    (1, 'Vehiculo pesado'),
)

CHOICES_TYPE_TRANSFER = (
    (0, 'Entrega'),
    (1, 'Interno'),
    (2, 'Externo'),
)

CHOICES_TYPE_FUEL_PUMP = (
    (0, 'Diesel'),
    (1, 'Gasolina'),
)

CHOICES_LOCATION_FUEL_PUMP = (
    (0, 'Almacén'),
    (1, 'Planta'),
    (2, 'Patio'),
)

CHOICES_TYPE_TRUCK = (
    (1, 'Pipa'),
    (2, 'Plataforma'),
)

CHOICES_PAYMENT_METHOD = (
    (0, 'Efectivo'),
    (1, 'Tarjeta de crédito'),
    (2, 'Tarjeta de débito'),
    (3, 'Transferencia'),
    (4, 'Cheque'),
    (5, 'Depósito'),
    (6, 'Otro'),
)

def convert_to_choices(choices):
    """
    Convert a list of tuples to a list of dictionaries
    """
    return [{'id': id, 'name': name} for id, name in choices]