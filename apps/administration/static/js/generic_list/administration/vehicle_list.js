$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'economic_number',
            'title': 'Número económico',
        },{
            'data': 'plates',
            'title': 'Placas',
        },{
            'data': 'brand',
            'title': 'Marca',
        },{
            'data': 'model',
            'title': 'Modelo',
        },{
            'data': 'get_type_vehicle_display',
            'title': 'Tipo de vehiculo',
        },{
            'data': 'responsible',
            'title': 'Responsable',
        },{
            'data': 'asigned_truck',
            'title': 'Remolques Asignadas',
            'render': function(data, type, row){
                return render_dt_badge_cicle(data, type, row);
            }
        },{
            'data': 'is_active',
            'title': 'Disponible',
            'render': function(data, type, row){
                return render_dt_yes_no(data, type, row);
            }
        }
    ]
    })
});