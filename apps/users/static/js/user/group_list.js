$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'name',
            'title': 'Nombre',
        },{
            'data': 'count_permissions',
            'title': 'Total de permisos',
        }
    ]
    })
});