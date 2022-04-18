$(document).ready(function(){
 
    var contenedor = $('#contenedor');
    contenedor.empty();

    $.get({
        url: 'https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/bibloteca/',

        success: function(respuestaOK){
            $.each(respuestaOK.items, function(indice, album){
                contenedor.append("<div class='card'>" +
                "<div class='card-body'>"+
                "<h5 class='card-title'>" + album.nombre + "</h5>" +
                "<p class='card-text'><b>Precio: </b>$" + album.precio.toLocaleString("es-CL") + "<br>"+"Stock: "+album.stock+"</p>"+
            "</div></div>")
            })
        },
        error: function(respuestaError){
            console.error(respuestaError);
        }
    })
});//fin document ready{
