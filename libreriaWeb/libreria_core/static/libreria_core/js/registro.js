$(document).ready(function(){
    //VARIABLES
    var codigoLibro= document.getElementById('codigoLibro');
    var nombreLibro= document.getElementById('nombreLibro');
    var precioLibro=document.getElementById('precioLibro');
    var stockLibro=document.getElementById('stockLibro');
    var portada= document.getElementById('portada');
    var url = 'https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/bibloteca/';
    var url2 = 'https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/';
   
    $('#registroBD').click(function(){
    var data = {
        "codigo": ""+ codigoLibro.value.toUpperCase(),
        "nombre" : ""+nombreLibro.value,
        "precio" : Number(precioLibro.value),
        "stock" : Number(stockLibro.value),
    };

    var data2 = {
        "codigo": ""+ codigoLibro.value.toUpperCase(),
        "nombre" : ""+nombreLibro.value,
        "precio" : Number(precioLibro.value),
        "stock" : Number(stockLibro.value),
        "portada" : portada.value
    };

    var urlGet = 'https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/'+codigoLibro.value.toUpperCase();


    $.get({
        urlGet,
        error: function(status){
            if (status=404){
                $.post(url2, data2, function(){
                    console.clear()
                });
            }
        }
    });

});


});//fin document ready{
