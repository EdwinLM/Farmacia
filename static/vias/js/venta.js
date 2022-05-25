var vents = {
	items: {
		cli: '',
		fec: '',
		sub: 0.00,
		iva: 0.00,
		tot: 0.00,
		pro: []
	},
	add: function (item) {
		this.items.products.push(item);
        this.list();
	};
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
            	console.log('aaaaaa');
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



});
