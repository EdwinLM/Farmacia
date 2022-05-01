function submit_with_ajax() {
	$.confirm( options:{
		theme: 'material',
	    title: 'Confirmación',
	    icon: 'fa fa-info'
    	content: '¿Estas seguro?',
    	columnClass: 'small',
    	typeAnimated: true,
    	cancelButtonClass: 'btn-primary',
    	draggable: true,
    	dragWindowBorder: false,
	    buttons: {
	    	info: {
	    		text: 'Si',
	    		btnClass: 'btn-primary',
	    		action: function () {
        	    }
	        },
    	    danger: {
	    		text: 'No',
	    		btnClass: 'btn-red',
	    		action: function () {
        	    }
	        }
    	}
	});
};