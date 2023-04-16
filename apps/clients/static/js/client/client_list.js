$(document).ready(function() {
    createDataTable({
        'columns':[{
            'title': 'Nombre responsable',
            'data': 'full_name',
        },{
            'data': 'business_name',
            'title': 'Razón social',
        },{
            'data': 'rfc',
            'title': 'RFC',
        },{
            'data': 'email',
            'title': 'Correo electrónico',
        },{
            'data': 'phone',
            'title': 'Teléfono',
        }
    ]
    })
});