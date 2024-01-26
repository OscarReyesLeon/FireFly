$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'economic_number',
            'title': 'Número económico',
        },{
            'data': 'plates',
            'title': 'Placas',
        },{
            'data': 'get_type_truck_display',
            'title': 'Tipo de remolque',
        },{
            'data': 'is_active',
            'title': 'Disponible',
            'render': function(data, type, row){
                return data == true ? 'SI' : 'NO';
            }
        }
    ]
    })
});

