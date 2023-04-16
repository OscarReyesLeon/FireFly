$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'first_name',
            'title': 'Nombre',
        },{
            'data': 'last_name',
            'title': 'Apellido',
        },{
            'data': 'email',
            'title': 'Correo electrónico',
        },{
            'data': 'is_active',
            'title': 'Activo',
            'render': function(data, type, row) {
                return render_dt_activo_inactivo(data, type, row);
            }

        },{
            'data': 'groups',
            'title': 'Grupos',
            'render': function(data, type, row) {
                return render_dt_badge_cicle(data, type, row);
            }
        },{
            'data': 'count_permissions',
            'title': 'Permisos',
        }
    ]
    })
});