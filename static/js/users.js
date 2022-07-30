$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es',
        placeholder: 'Buscar...'
    });

    //Evento submit (guardar)
    $('#frmUsers').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        //parameters.append('action', 'add');
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = list_url;
        });
    });
    
    $('#myTable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "full_name"},
            {"data": "username"},
            {"data": "date_joined"},
            {"data": "image"},
            {"data": "groups"},
            {"data": "sucursales"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="' + row.image + '" class="img-fluid mx-auto d-block" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.groups, function (key, value) {
                        html += '<span class="badge badge-success">' + value.name + '</span> ';
                    });
                    return html;
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.sucursales, function (key, value) {
                        html += '<span class="badge badge-secondary">' + value.name + '</span> ';
                    });
                    return html;
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/usuarios/editar/' + row.id + '" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/usuarios/eliminar/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

});
