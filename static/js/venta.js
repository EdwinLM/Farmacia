var tblProducts;
var vents = {
    items: {
        id_cliente: '',
        id_empresa: '',
        nit: '',
        nombre: '',
        direccion: '',
        telefono: '',
        email: '',
        se_factura: 'N',
        id_sucursal: 3,
        fecha: '',
        subtotal_afecto: 0.00,
        subtotal_noafecto: 0.00,
        iva: 0.00,
        total: 0.00,
        id_forma_pago: 1,
        products: []
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.products, function (key, value) {
            ids.push(value.id_producto);
        });
        return ids;
    },
    calculate_invoice: function() {
    	var subtotal_afecto = 0.00;
        var subtotal_noafecto = 0.00;
    	$.each(this.items.products, function (pos, dict) {
            dict.subtotal = dict.cant * parseFloat(dict.pvp);
            if (dict.afecto_impuesto)
        		subtotal_afecto += dict.subtotal;
            else
                subtotal_noafecto += dict.subtotal;
    	});
    	this.items.subtotal_afecto = subtotal_afecto;
        this.items.subtotal_noafecto = subtotal_noafecto;
        this.items.total = this.items.subtotal_afecto + this.items.subtotal_noafecto;
        this.items.iva = this.items.subtotal_afecto - this.items.subtotal_afecto/1.12;
        $('input[name="subtotal_afecto"]').val(this.items.subtotal_afecto.toFixed(2));
        $('input[name="subtotal_noafecto"]').val(this.items.subtotal_noafecto.toFixed(2));
        $('input[name="iva"]').val(this.items.iva.toFixed(2));
    	$('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function(item){
        this.items.products.push(item);
        this.list();
    },
    list: function () {
    	this.calculate_invoice();

        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "id_producto"},
                {"data": "nombre_venta"},
                {"data": "cat.descripcion"},
                {"data": "pvp"},
                {"data": "cant"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Q' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="'+row.cant+'">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Q' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex ) {
            	$(row).find('input[name="cant"]').TouchSpin( {
            		min: 1,
            		max: 100000000,
            		step: 1
            	});
            },
            initComplete: function (settings, json) {

            }
        });
    },
};

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    if (!Number.isInteger(repo.id)) {
        return repo.text;
    }

    var html_componentes = '';
    let arr = repo.comp.split('| ');
    arr.forEach(function(item){
        if (item !== ' ') html_componentes += '<span class="badge badge-success">' + item + '</span> ';
    })

    var option = $(
        '<div class="wrapper container">' +
        '<div class="row">' +
        '<div class="col-lg-1">' +
        '<img src="' + repo.imagen + '" class="img-fluid img-thumbnail d-block mx-auto rounded">' +
        '</div>' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Nombre:</b> ' + repo.full_name + '<br>' +
        '<b>Componentes:</b> ' + html_componentes + '<br>' +
        '<b>Stock:</b> ' + repo.stock + '<b>   Precio Venta:</b> <span class="badge badge-warning">Q' + repo.pvp + '</span>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

$(function () {

	$('.select2').select2({
		theme: "bootstrap4",
		language: 'es'
	});

	$('#fecha').datetimepicker({
		format: 'YYYY-MM-DD',
		date: moment().format('YYYY-MM-DD'),
		locale: 'es',
		minDate: moment().format('YYYY-MM-DD'),
		maxDate: moment().format('YYYY-MM-DD'),
	});

    //Búsqueda de Clientes
    $('select[name="id_cliente"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'buscar_clientes'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        $('input[name="nit"]').val(data.nit);
        $('input[name="nombre"]').val(data.nombre);
        $('input[name="direccion"]').val(data.direccion);
        $('input[name="telefono"]').val(data.telefono);
        $('input[name="email"]').val(data.email);
    });

    $('.btnAddClient').on('click', function () {
        $('#myModalClient').modal('show');
    });

    $('#myModalClient').on('hidden.bs.modal', function (e) {
        $('#frmClient').trigger('reset');
    })

    $('#frmClient').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_client');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear al siguiente cliente?', parameters, function (response) {
                //console.log(response);
                var newOption = new Option(response.full_name, response.id_cliente, false, true);
                $('select[name="id_cliente"]').append(newOption).trigger('change');
                $('#myModalClient').modal('hide');
            });
    });

	//Búsqueda de Productos
	/*$('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_autocomplete',
                    'ids': JSON.stringify(vents.get_ids()),
                    'term': $('input[name="search"]').val()
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {
            	
            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
        	event.preventDefault();
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            console.log(vents.items);
            vents.add(ui.item);
            $(this).val('');
        }
    });*/

	//Eliminar todos los items
	$('.btnRemoveAll').on('click', function() {
		if (vents.items.products.length === 0) return false;
		alert_action('Notificación', '¿Está seguro de eliminar todos los items del detalle?', function () {
			vents.items.products = [];
			vents.list();
		}, function () {

		});
	});

	//Evemto Cantidad
	$('#tblProducts tbody')
		.on('click', 'a[rel="remove"]', function () {
			var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?',
                function () {
                    vents.items.products.splice(tr.row, 1);
                    vents.list();
                }, function () {

                });
		})
		.on('change keyup', 'input[name="cant"]', function () {
			var cant = parseInt($(this).val());
			var tr = tblProducts.cell($(this).closest('td, li')).index();
			vents.items.products[tr.row].cant = cant;
			vents.calculate_invoice();
			$('td:eq(5)', tblProducts.row(tr.row).node()).html('Q'+vents.items.products[tr.row].subtotal.toFixed(2));
		});

	//Evento CleanSearch
	$('.btnClearSearch').on('click', function () {
		$('input[name="search"]').val('').focus();
	});

    //Buscar Productos
    $('.btnSearchProducts').on('click', function () {
        tblSearchProducts = $('#tblSearchProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'id_sucursal': vents.items.id_sucursal,
                    'ids': JSON.stringify(vents.get_ids()),
                    'term': $('select[name="search"]').val()
                },
                dataSrc: ""
            },
            columns: [
                {"data": "full_name"},
                {"data": "imagen"},
                {"data": "id_producto"},
                {"data": "pvp"},
                {"data": "id_producto"},
            ],
            columnDefs: [
                {
                    targets: [-4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img src="' + data + '" class="img-fluid d-block mx-auto" style="width: 20px; height: 20px;">';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '<span class="badge badge-secondary">' + data + '</span>';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'X' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a rel="add" class="btn btn-success btn-xs btn-flat"><i class="fas fa-plus"></i></a> ';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
        $('#myModalSearchProducts').modal('show');
    });

    $('#tblSearchProducts tbody')
        .on('click', 'a[rel="add"]', function () {
            var tr = tblSearchProducts.cell($(this).closest('td, li')).index();
            var product = tblSearchProducts.row(tr.row).data();
            product.cant = 1;
            product.subtotal = 0.00;
            vents.add(product);
            tblSearchProducts.row($(this).parents('tr')).remove().draw();
        });

	//Evento submit (guardar)
	$('#frmSale').on('submit', function (e) {
		e.preventDefault();

		if (vents.items.products.length === 0) {
			message_error('Debe al menos tener un item en su detalle de venta.');
			return false;
		};

		vents.items.fecha = $('input[name="fecha"]').val();
        vents.items.nit = $('input[name="nit"]').val();
        vents.items.nombre = $('input[name="nombre"]').val();
        vents.items.telefono = $('input[name="telefono"]').val();
        vents.items.direccion = $('input[name="direccion"]').val();
        vents.items.email = $('input[name="email"]').val();
        if (document.querySelector('input[name="se_factura"]').checked) {
            vents.items.se_factura = 'S';
        }
		//vents.items.id_cliente = $('input[name="id_id_cliente"]').val();
        vents.items.id_cliente = $('select[name="id_cliente"]').val();
        vents.items.id_empresa = $('input[name="id_empresa"]').val();
        vents.items.id_forma_pago = $('select[name="id_forma_pago"]').val();
		var parameters = new FormData();
		parameters.append('action', $('input[name="action"]').val());
		parameters.append('vents', JSON.stringify(vents.items));
		console.log(vents);
		submit_with_ajax(window.location.pathname, 'Notificación', '¿Está seguro de realizar la siguiente acción?', parameters, function (response) {
			location.href = '/ventas/crear';
		});
	});

    $('select[name="search"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_autocomplete',
                    id_sucursal: vents.items.id_sucursal,
                    ids: JSON.stringify(vents.get_ids())
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        if (!Number.isInteger(data.id_producto)) {
            return false;
        }
        data.cant = 1;
        data.subtotal_afecto = 0.00;
        data.subtotal_no_afecto = 0.00;
        data.iva = 0.00;
        data.total = 0.00;
        vents.add(data);
        $(this).val('').trigger('change.select2');
    });

    // Esto se puso aqui para que funcione bien el editar y calcule bien los valores del iva. // sino tomaría el valor del iva de la base debe
    // coger el que pusimos al inicializarlo.

	vents.list();
});
