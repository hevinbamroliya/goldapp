// Copyright (c) 2024, hevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gold Ledger', {
	refresh: function(frm) {
		frm.page.btn_secondary.hide();
		frm.hide('status');
		
	},
	on_submit: function(frm){
		frm.show_alert(__("Gold Ledger is save"), "green");
	}
});





