$(document).ready(function(){
 
    var contenedor = $('#contenedor'); //contenedor de los libros
    contenedor.empty();
    var cargador = $('#cargador') //spinner loader
    var libroAgregado = localStorage;
    var tabla = $('#tabla');
    tabla.empty();
    //GET de la api de la base de datos
    $.get({
        url: 'https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/',

        success: function(respuestaOK){
            $.each(respuestaOK.items, function(i,libro){
                cargador.empty();
                contenedor.append("<div class='card dec-hov card_2 shadow'>" +
                "<img src='" + libro.portada + "' class='card-img-top max-tam-img' alt='"+ "'>"+
                "<div class='card-body shadow'>"+
                "<h5 class='card-title text-center title-card'>" + libro.nombre + "</h5>" +
                "<p class='card-text text-center text-by'><b>Precio: </b>$"+ 
                "<br>"+
                "Stock: "+libro.stock+"</p>"+
                "<div>"+
                "<div class='d-flex justify-content-center text-center'>"+
                "<button type='button' id='botonC' class='botonC'>Comprar</button>"+
                "<button type='button' id='"+libro.codigo+"' class='botonA'>Añadir al carro</button>"+
                "</div>"+
                "</div>"+
                "</div></div>");

                $('#'+libro.codigo).click(function(){
                    const datos = [{"Nombre": libro.nombre, 
                    "Precio": libro.precio
                    }];
                    libroAgregado.setItem(libro.codigo, datos);
                    console.log("libro agregado");
                });

            });   
        },
        error: function(respuestaError){
            console.error(respuestaError);
        }
    });

    //
    
    $(document).ready(function(){
        console.log("CCCCCCCCCCCCCCCCCCCCCC");
        console.log(libroAgregado.getItem('AFK230'));

        tabla.append(
      "<table class='table table-dark' id='tabla'>"+
        "<thead>"+
            "<tr>"+
                "<th scope='col'>Codigo</th>"+
                "<th scope='col'>Libro</th>"+
                "<th scope='col'>Cantidad</th>"+
                "<th scope='col'>Precio</th>"+
            "</tr>"+
        "</thead>"+
        "<tbody>"+
            "<tr>"+
                "<th scope='row'>"+libroAgregado.nombre+"</th>"+
                "<td>"+libroAgregado.precio+"</td>"+
                "<td>X</td>"+
                "<td>precio</td>"+
            "</tr>"+
        "</tbody>"+
        "</table>"
        );
    })


});//fin document ready{
