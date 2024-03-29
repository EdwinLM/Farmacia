var tblSale;

function format(d) {
    var html = '<table class="table">';
    html += '<thead class="thead-dark">';
    html += '<tr><th scope="col">Producto</th>';
    html += '<th scope="col">Precio Venta</th>';
    html += '<th scope="col">Cantidad</th>';
    html += '<th scope="col">Subtotal</th></tr>';
    html += '</thead>';
    html += '<tbody>';
    $.each(d.det, function (key, value) {
        html+='<tr>'
        html+='<td>'+value.nombre+'</td>'
        html+='<td>'+value.precio_venta+'</td>'
        html+='<td>'+value.cantidad+'</td>'
        html+='<td>'+value.subtotal+'</td>'
        html+='</tr>';
    });
    html += '</tbody>';
    return html;
}

$(function () {

    tblSale = $('#myTable').DataTable({
        //responsive: true,
        scrollX: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata',
                'id_sucursal': $('input[name="id_sucursal"]').val()
            },
            dataSrc: ""
        },
        columns: [
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
            {"data": "sucurs"},
            {"data": "fecha"},
            {"data": "nit"},
            {"data": "nombre"},
            {"data": "total"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-3, -4, -5, -6],
                class: 'text-center',
                orderable: false,
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return 'Q' + parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    //var buttons = '<a href="/cajero/eliminar/' + row.id_venta + '" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    //buttons += '<a href="/cajero/editar/' + row.id_venta + '" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    var buttons = '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
                    buttons += '<a href="/cajero/pdf/'+row.id_venta+'" target="_blank" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    $('#myTable tbody')
        .on('click', 'a[rel="details"]', function () {
            var tr = tblSale.cell($(this).closest('td, li')).index();
            var data = tblSale.row(tr.row).data();
            console.log(data);

            $('#tblDet').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_prod',
                        'id': data.id_venta
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "nombre"},
                    {"data": "precio_venta"},
                    {"data": "cantidad"},
                    {"data": "subtotal"},
                ],
                columnDefs: [
                    {
                        targets: [-1, -3],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return 'Q' + parseFloat(data).toFixed(5);
                        }
                    },
                    {
                        targets: [-2],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return data;
                        }
                    },
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelDet').modal('show');
        })
        .on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var row = tblSale.row(tr);
            if (row.child.isShown()) {
                row.child.hide();
                tr.removeClass('shown');
            } else {
                row.child(format(row.data())).show();
                tr.addClass('shown');
            }
        });

});