		$('#myTable').DataTable({
			responsive: true,
			autoWidth: false,
			destroy: true,
			deferRender: true,
			"language": {
				"url" : "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
			},
			ajax: {
				url: '',
				type: 'POST',
				data: {
					'action': 'searchdata'
				},
				dataSrc: ""
			},
			columns: [
				{"data": "id_via_administracion"},
				{"data": "descripcion"},
				{"data": "abreviatura"},
				{"data": "estado"},
				{"data": "id_empresa"},
				{"data": "id_empresa"}
			],
			columnDefs: [
				{ targets: [0,3,4], visible: false },
				{ targets: [-1], class: 'text-center', orderable: false,
					render: function (data, type, row) {
						var buttons = '<a href="/vias/editar/' + row.id_via_administracion + '" class="btn btn-warning btn-xs btn-flat" title="Editar"><i class="fas fa-edit"></i></a> ';
						buttons += '<button class="btn btn-danger btn-xs btn-flat" onclick="return eliminar();" type="submit" title="Eliminar"><i class="fas fa-trash-alt"></i></button>';
						return buttons;
					}
				}
			],
			initComplete: function(settings, json) {
			
			}
		});