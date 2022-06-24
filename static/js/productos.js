$(function () {

    //Evento submit (guardar)
    $('#frmProducto').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'add');
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/productos/';
        });
    });

    //Crear Categoría
    $('.btnAddCategoria').on('click', function () {
        $('#myModalCategoria').modal('show');
    });

    $('#myModalCategoria').on('hidden.bs.modal', function (e) {
        $('#frmCategoria').trigger('reset');
    })

    $('#frmCategoria').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_categoria');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear la Categoría?', parameters, function (response) {
                var newOption = new Option(response.descripcion, response.id_categoria, false, true);
                $('select[name="id_categoria"]').append(newOption).trigger('change');
                $('#myModalCategoria').modal('hide');
            });
    });


    //Crear Fabricante
    $('.btnAddFabricante').on('click', function () {
        $('#myModalFabricante').modal('show');
    });

    $('#myModalFabricante').on('hidden.bs.modal', function (e) {
        $('#frmFabricante').trigger('reset');
    })

    $('#frmFabricante').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_fabricante');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear el Laboratorio?', parameters, function (response) {
                var newOption = new Option(response.nombre, response.id_fabricante, false, true);
                $('select[name="id_fabricante"]').append(newOption).trigger('change');
                $('#myModalFabricante').modal('hide');
            });
    });


    //Crear Presentación
    $('.btnAddPresentacion').on('click', function () {
        $('#myModalPresentacion').modal('show');
    });

    $('#myModalPresentacion').on('hidden.bs.modal', function (e) {
        $('#frmPresentacion').trigger('reset');
    })

    $('#frmPresentacion').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_presentacion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear la presentación?', parameters, function (response) {
                var newOption = new Option(response.descripcion, response.id_presentacion, false, true);
                $('select[name="id_presentacion"]').append(newOption).trigger('change');
                $('#myModalPresentacion').modal('hide');
            });
    });


    //Crear País
    $('.btnAddPais').on('click', function () {
        $('#myModalPais').modal('show');
    });

    $('#myModalPais').on('hidden.bs.modal', function (e) {
        $('#frmPais').trigger('reset');
    })

    $('#frmPais').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_pais');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear el país?', parameters, function (response) {
                var newOption = new Option(response.nombre, response.id_pais, false, true);
                $('select[name="id_pais"]').append(newOption).trigger('change');
                $('#myModalPais').modal('hide');
            });
    });



    //Crear Unidad de Medida
    $('.btnAddMedida').on('click', function () {
        $('#myModalMedida').modal('show');
    });

    $('#myModalMedida').on('hidden.bs.modal', function (e) {
        $('#frmMedida').trigger('reset');
    })

    $('#frmMedida').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_unidad');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear la unidad de medida?', parameters, function (response) {
                var newOption = new Option(response.descripcion, response.id_unidad_medida, false, true);
                $('select[name="id_unidad_medida"]').append(newOption).trigger('change');
                $('#myModalMedida').modal('hide');
            });
    });



    //Crear Vía de Administración
    $('.btnAddVia').on('click', function () {
        $('#myModalVia').modal('show');
    });

    $('#myModalVia').on('hidden.bs.modal', function (e) {
        $('#frmVia').trigger('reset');
    })

    $('#frmVia').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_via');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear la via de administración?', parameters, function (response) {
                var newOption = new Option(response.descripcion, response.id_via_administracion, false, true);
                $('select[name="id_via_administracion"]').append(newOption).trigger('change');
                $('#myModalVia').modal('hide');
            });
    });



    //Crear Tipo de Prescripción
    $('.btnAddPrescripcion').on('click', function () {
        $('#myModalPrescripcion').modal('show');
    });

    $('#myModalPrescripcion').on('hidden.bs.modal', function (e) {
        $('#frmPrescripcion').trigger('reset');
    })

    $('#frmPrescripcion').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_prescripcion');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear el tipo de prescripción?', parameters, function (response) {
                var newOption = new Option(response.descripcion, response.id_tipo_prescripcion, false, true);
                $('select[name="id_tipo_prescripcion"]').append(newOption).trigger('change');
                $('#myModalPrescripcion').modal('hide');
            });
    });

});
