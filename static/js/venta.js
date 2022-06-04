var tblProducts;
var vents = {
    items: {
        id_cliente: '',
        id_sucursal: 36,
        fecha: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        products: []
    },
    calculate_invoice: function() {
    	var subtotal = 0.00;
    	$.each(this.items.products, function (pos, dict) {
    		dict.subtotal = dict.cant * parseFloat(dict.pvp);
    		subtotal += dict.subtotal;
    	});
    	this.items.subtotal = subtotal;
    	$('input[name="total"]').val(this.items.subtotal.toFixed(2));
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

	//Búsqueda de Productos
	$('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'buscar_productos',
                    'term': request.term
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
    });

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
			vents.items.products.splice(tr.row, 1);
			vents.list();
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

	//Evento submit (guardar)
	$('form').on('submit', function (e) {
		e.preventDefault();

		if (vents.items.products.length === 0) {
			//message_error('Debe al menos tener un item en su detalle de venta.');
			alert("aaaa")
			return false;
		};

		vents.items.fecha = $('input[name="fecha"]').val();
		//vents.items.id_cliente = $('input[name="id_id_cliente"]').val();
        vents.items.id_cliente = $('select[name="id_cliente"]').val();
		var parameters = new FormData();
		parameters.append('action', $('input[name="action"]').val());
		parameters.append('vents', JSON.stringify(vents.items));
		console.log(vents);
		submit_with_ajax(window.location.pathname, 'Notificación', '¿Está seguro de realizar la siguiente acción?', parameters, function (response) {
			location.href = '/dashboard/';
		});
	});

	vents.list();
});
