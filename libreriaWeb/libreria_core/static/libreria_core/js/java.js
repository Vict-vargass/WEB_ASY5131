$(document).ready(function(){
    //VARIABLES
    

    var storage = window.localStorage;

    function cargarCarro(){
        console.log("Carrito guardado: ", storage)
    }
    
    cargarCarro();

});//fin document ready{
