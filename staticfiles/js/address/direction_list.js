$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'street',
            'title': 'Calle',
        },{
            'data': 'number_ext',
            'title': 'Número Exterior',
        },{
            'data': 'number_int',
            'title': 'Número Interior',
        },{
            'data': 'neighborhood',
            'title': 'Colonia',
        },{
            'data': 'reference',
            'title': 'Referencia',
        }
    ]
    })
});