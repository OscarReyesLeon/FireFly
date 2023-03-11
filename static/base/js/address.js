$(document).ready(function(){
    function reiniciarSelect2(select){
        select.select2({
            data: [],
            'placeholder': 'Seleccione una opción',
        })
        select.trigger("change")
    }

    function callAPI(url_extra, select){
        let url = "/api/v1/address/" + url_extra
        $.get(url).done(function(data){
            select.empty()
            select.select2({
                data: data.map(function(data){
                    return {id: data.id, text: data.name}
                })
            })
            select.trigger("change")
        })
    }

    $("#id_state").change(function(){
        let state = $(this).val()
        reiniciarSelect2($("#id_municipality"))
        reiniciarSelect2($("#id_neighborhood"))
        if (!state) return 
        callAPI("municipality/?state_id=" + state, $("#id_municipality"))
    });

    $('#id_state').on('select2:clearing', function (e) {
        $(this).val(null).trigger('change');
    });


    $("#id_municipality").change(function(){
        let municipality = $(this).val()
        reiniciarSelect2($("#id_neighborhood"))
        if (!municipality) return
        callAPI("neighborhood/?municipality_id=" + municipality, $("#id_neighborhood"))
    });
})