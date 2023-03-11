$(document).ready(function() {
    createDataTable({
        'columns':[{
            'data': 'name',
            'title': 'Nombre',
        },{
            'data': 'description',
            'title': 'Descripción',
        },{
            'data': 'base_price',
            'title': 'Precio',
        },{
            'data': 'category',
            'title': 'Categoria',
        },{
            'data': 'unit_measure',
            'title': 'Unidad de medida',
        }
    ]
    })
});