// Copyright (c) 2024, hevin and contributors
// For license information, please see license.txt

frappe.provide("erpnext.stock");
frappe.provide("erpnext.accounts.dimensions");

frappe.ui.form.on('Stock Audit', {
	onload: function (frm) {
		frm.call({
			doc: frm.doc,
			method: 'items_in_stock',
			callback: function (r) {
			
				if (r.message) {
					frm.clear_table("stock_items");
					$.each(r.message, function (data) {
						var child = frm.add_child("stock_items");
						frappe.model.set_value(child.doctype, child.name, "item_code", data.item_code);
						frappe.model.set_value(child.doctype, child.name, "serial_no", data.name);						
					});
					frm.refresh_field("stock_items");
				}
			}
		})
	},	

	scan_barcode: function (frm) {
				
		if (frm.doc.scan_barcode !== '') {
			var not_in_stock = frm.doc.not_in_stock.length;
			var not_found = frm.doc.total_not_found_items;
			
			frm.call({
				doc: frm.doc,	
				method: 'serial_number',
				callback: function (r) {
					if (r.message) {
											
						var barcode = r.message[0].name;
						var status = r.message[0].status;

						if (frm.doc.scan_barcode) {
							frm.doc.stock_items.forEach(function (d) {
								if (d.serial_no === barcode) {
									if(d.qty_checked !== 1){
										// frappe.model.set_value(d.doctype, d.name, 'qty_checked', 1);
										d.qty_checked = 1;
										frappe.msgprint(d.serial_no + " This Serial No. Availabel in Stock."); 
									}
									else{		
									frappe.msgprint(d.serial_no + " This Serial No. Checked in Stock."); 
									}																		
								}
							});
							refresh_field('stock_items');
						}
						if (status == 'Delivered') {
								r.message.forEach(function (i) {
								var existingRow = frm.doc.not_in_stock.find(function (row) {
									return row.serial_no === i.name;
								});
								if (!existingRow) {
									var row = frappe.model.add_child(frm.doc, 'Not In Stock', 'not_in_stock');
									frappe.model.set_value(row.doctype, row.name, 'serial_no', i.name);
									frappe.model.set_value(row.doctype, row.name, 'item_code', i.item_code);
									not_in_stock += 1;
									frm.set_value('total_not_in_stock_items', not_in_stock);
									frappe.msgprint(i.name +" This Serial No added in Not in Stock table.");
									return;
								}
								else {
									frappe.msgprint(i.name + "This Serial No is already delivered added in Not in Stock table.");
									return;
								}
							});
							frm.refresh_field('not_in_stock');

						}
						if (status == 'Inactive') {
							var code = handleBarcodeScan(barcode);
							if(code){
								not_found += 1;
								frm.set_value('total_not_found_items', not_found);
								frappe.msgprint(barcode +" This Serial No added in Not in Stock table.");
							}
							else{
								frappe.msgprint(barcode +" this Serial No alredy Checked in Not in Stock table")
							}	
												
						}						
					}
					else { 
						frappe.msgprint("Barcode not found in the system."); 
					}
					frm.set_value('scan_barcode', '');
				}
			}).then(() => {
				frm.set_value('scan_barcode', '');
			})
		}
		
	}	

});

//-- this Function one time Inactive serail No add not fount stock ---//
let barcodeArray = [];	
function handleBarcodeScan(scannedBarcode) {	
    if (!barcodeArray.includes(scannedBarcode)) {      
		barcodeArray.push(scannedBarcode);
        return true
		
    } else {
        return false
		
    }
	
}

