$(document).ready(function() {
    createDataTable({
        'columns':[{
            'title': 'Folio de orden',
            'data': 'key_order',
        },{
            'title': 'Estatus',
            'data': 'get_status_display'
        },{
            'title': 'Autorizado',
            'data': 'autorization',
            'render': function(data, type, row) {
                return render_dt_yes_no(data,type, row)
            }
        },{
            'title': 'Cliente',
            'data': 'client'
        },{
            'title': 'Dirección',
            'data': 'address'
        },{
            'title': 'Vehículo',
            'data': 'vehicle'
        },{
            'title': 'Chofer asignado',
            'data': 'driver'
        }
    ]
    })
});