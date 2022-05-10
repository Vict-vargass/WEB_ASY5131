$(document).ready(function(){

var base_de_datos = []
var contenedor = $('#contenedor')
var cargador = $('#cargador')
var carrito = [];
var localStorage = window.localStorage;
const divisa = '$'
var numeroItem = 0;
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
            base_de_datos.push(libro)
            $('#'+libro.codigo).click(
                function(){
                    carrito.push(libro.codigo);
                    guardar();
                    renderCarro();
                }
            )

        });

    }


});

function guardar (){
    localStorage.setItem('carrito', JSON.stringify(carrito));   
};

function renderCarro(){
    console.log("AREA RENDER CARRO");
    const carritoSinDuplicados = [...new Set(carrito)];
    
    carritoSinDuplicados.forEach((item)=>{
        const miItem = base_de_datos.filter((itemBD)=>{
            return itemBD.codigo == item
        });
        const numeroUnidadesItem = carrito.reduce((total, itemId)=>{
            return itemId === item ? total +=1 : total;
        }, 0);
        numeroItem = numeroUnidadesItem;

    });

    console.log("CARRO SIN DUPLICADOS: ",carritoSinDuplicados);
    console.log("Numero item: ", numeroItem);
    console.log("CARRO ORIGINAL: ", carrito);

};




});