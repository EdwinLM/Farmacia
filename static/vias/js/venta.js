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
});
