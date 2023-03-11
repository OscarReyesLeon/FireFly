$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'name',
            'title': 'Nombre',
        },{
            'data': 'instance',
            'title': 'Código completo',
        },{
            'data': 'group_set',
            'title': 'Grupos',
            'render': function(data, type, row) {
                return render_dt_badge_cicle(data, type, row);
            }
        },{
            'data': 'count_users',
            'title': 'Usuarios asignados directamente',
        }
    ]
    })
});