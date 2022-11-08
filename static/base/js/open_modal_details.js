$(document).ready(function(){
  $(".search_details").on("click", function(){
    var id = $(this).attr("data_id");
    $.ajax({
      url: `/cmp/ordencompra/modal?id=${id}`,
      type: "GET",
      success: function(data){
        $("#data_details").html(data);
        $("#modal_details").modal("show");
      }
    })
  })
})