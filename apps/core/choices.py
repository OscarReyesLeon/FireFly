CHOICES_PROCESS_STATUS = (
    (1, 'Remisión (Ingreso)'), #Persona1 -Levanta pedido (indica si se factura (0-1), nota de remisión)
    (2, 'Autorización y asignación de camión'), #Persona2- Autoriza pedido y asigna camión
    (3, 'Cáptura de salida'),  #Persona3-Captura datos de salida del almacen (piezas)
    (4, 'Salida del almacén'), #Bascula - Indica el tonelaje que lleva el chofer, peso y GPS (Se genera Carta porte)
    (5, 'Entregado'), #Chofer- Indica lo mismo que en la salida de báscula(peso,GPS, Imagen(?)) y se pasa a por facturar (si es 1)
    (7, 'Entrada a almacén'), #Chofer-Indica que el viaje ha finalizado.
    (8, 'Cáptura de entrada'), #Vigilante- Indica litros de diesel que recargó y cierra viaje
    (9, 'Finalizado'), #Fin del viaje
)

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
    (0, 'Entrega')
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