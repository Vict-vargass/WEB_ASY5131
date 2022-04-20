$(document).ready(function(){
 
    var contenedor = $('#contenedor');
    contenedor.empty();

    $.get({
        url: 'https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/',

        success: function(respuestaOK){
            $.each(respuestaOK.items, function(indice, album){
                console.log(album);
                contenedor.append("<div class='card dec-hov shadow'>" +
                "<img src='" + album.portada + "' class='card-img-top max-tam-img' alt='"+ "'>"+
                "<div class='card-body shadow'>"+
                "<h5 class='card-title text-center'>" + album.nombre + "</h5>" +
                "<p class='card-text text-center'><b>Precio: </b>$" + album.precio.toLocaleString("es-CL") + "<br>"+"Stock: "+album.stock+"</p>"+
            "</div></div>")
            })   
        },
        error: function(respuestaError){
            console.error(respuestaError);
        }
    })
});//fin document ready{
