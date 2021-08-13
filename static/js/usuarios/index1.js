function listadoLibro(){
    $.ajax({
        url:'/libro/listas_libros/',
        type:'get',
        dataType:'json',
        success: function(response){
            console.log(response);
        },
        error: function(response){
            console.log(response);
        }
    });
}
$(document).ready(function(){
    listadoLibro()
});