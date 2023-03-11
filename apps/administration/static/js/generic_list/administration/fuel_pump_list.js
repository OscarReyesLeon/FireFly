$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'name',
            'title': 'Nombre',
        },{
            'data': 'description',
            'title': 'Descripción',
        },{
            'data': 'get_type_fuel_pump_display',
            'title': 'Tipo de bomba',
        },{
            'data': 'get_location_display',
            'title': 'Ubicación',
        }
    ]
    })
});