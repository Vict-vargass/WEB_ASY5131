$(document).ready(function(){

var contenedor = $('#contenedor')
var cargador = $('#cargador')
$.get({
    url: 'https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/',

    success: function(respuestaOK){
        cargador.empty();
        $.each(respuestaOK.items, function(i, libro){
            contenedor.append("<div class='card dec-hov card_2 shadow'>" +
            "<img src='" + libro.portada + "' class='card-img-top max-tam-img' alt='"+ "'>"+
            "<div class='card-body shadow'>"+
            "<h5 class='card-title text-center title-card'>" + libro.nombre + "</h5>" +
            "<p class='card-text text-center text-by'><b>Precio:"+libro.precio.toLocaleString("es-CL")+ " </b>$"+ 
            "<br>"+
            "Stock: "+libro.stock+"</p>"+
            "<div>"+
            "<div class='d-flex justify-content-center text-center'>"+
            "<button type='button' id='botonC' class='botonC'>Comprar</button>"+
            "<button type='button' id='"+libro.codigo+"' value='"+libro.codigo+"' class='botonA'>Añadir al carro</button>"+
            "</div>"+
            "</div>"+
            "</div></div>");
        });

    }


});





});