// Copyright (c) 2024, hevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stock Audit', {
	refresh: function(frm) {
		frm.call({
			doc: frm.doc,
			method: 'stockiten',
			callback: function(r) {
			    
				frm.set_value("total_items_in_stock", r.message);


				
				// frm.clear_table("stock_items");
				// $.each(r.message, function (data) {
				// 	if('scan_barcode' == data.item_code){
				// 	var child = frm.add_child("stock_items");
				// 	frappe.model.set_value(child.doctype, child.name, "item_code", data.item_code);
				// 	}
					
				// });
				// frm.refresh_field("stock_items");
			}
			
		})
		

	}
});



// scan_barcode() {
// 	const barcode_scanner = new erpnext.utils.BarcodeScanner({frm:this.frm});
// 	barcode_scanner.process_scan();
// }