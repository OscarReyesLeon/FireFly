$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'name',
            'title': 'Nombre',
        },{
            'data': 'municipality',
            'title': 'municipio',
        },{
            'data': 'postal_code',
            'title': 'Código Postal',
        },
    ]
    })
});