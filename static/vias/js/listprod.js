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
				{"data": "id_producto"},
				{"data": "codigo_barras_1"},
				{"data": "codigo_barras_2"},
				{"data": "nombre_compra"},
				{"data": "nombre_venta"},
				{"data": "nombre_corto"},
				{"data": "id_categoria"},
				{"data": "id_fabricante"},
				{"data": "id_presentacion"},
				{"data": "id_pais"},
				{"data": "id_unidad_medida"},
				{"data": "conversion"},
				{"data": "id_via_administracion"},
				{"data": "prioridad"},
				{"data": "imagen"},
				{"data": "id_tipo_prescripcion"},
				{"data": "afecto_impuesto"},
				{"data": "registro_sanitario"},
				{"data": "precio_costo"},
				{"data": "precio_venta"},
				{"data": "clasificacion_abc"},
				{"data": "estado"},
				{"data": "id_empresa"},
				{"data": "id_empresa"}
			],
			columnDefs: [
				{ targets: [0,3,4], visible: false },
				{ targets: [-1], class: 'text-center', orderable: false,
					render: function (data, type, row) {
						var buttons = '<a href="/productos/editar/' + row.id_producto + '" class="btn btn-warning btn-xs btn-flat" title="Editar"><i class="fas fa-edit"></i></a> ';
						buttons += '<button class="btn btn-danger btn-xs btn-flat" onclick="return eliminar();" type="submit" title="Eliminar"><i class="fas fa-trash-alt"></i></button>';
						return buttons;
					}
				}
			],
			initComplete: function(settings, json) {
			
			}
		});