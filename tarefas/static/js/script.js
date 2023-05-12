
/*
$(document).ready(function(){
 DataTable configurações
    $("#tabela").DataTable({
            paging:false,
            searching:true,
    });
        alert("entrei aqui");
});



$(document).ready(function () {
    alert("entrei aqui");
    var table = $('#tabela').DataTable();
        table.fnSort( [ [0,'desc'] ] );
        table.draw(true);
});
*/
var table;
$(document).ready(function () {
    table = $('#tabela').DataTable({
        order: [[0, 'desc']],
        paging:true,
        searching:true,
        scrollY: '200px',
        scrollCollapse: true,
    });
});

function criarBorda(){
    var table = $('.dataTables_scroll');
    table.removeClass('table-hover');
    table.addClass('table-bordered');

}


/*
function criarBorda(){

    Jquery
    var table = $('#tabela');
    table.removeClass('table-hover');
    table.addClass('table-bordered');
}

    JavaScript
    var borda = window.document.getElementById("tabela")
    borda.innerHTML = '<table class="table table-bordered" style="width:100%" id="tabela" >'

    */

/*
var table = $('#tabela').DataTable();

$('#myFilter').on( 'keyup', function () {
    table
        .search( this.value )
        .draw();
} );*/