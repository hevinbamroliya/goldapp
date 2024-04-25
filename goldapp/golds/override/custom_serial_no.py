import frappe
from typing import Dict, Optional
from frappe.model.document import Document
from frappe.model.mapper import map_doc



BarcodeScanResult = Dict[str, Optional[str]]


# ---------it is work on serial no set custom fields --------------   

import frappe
@frappe.whitelist()
def custom_update_serial_nos_after_submit(controller, parentfield):
    field = ["custom_size", "custom_metal_type", "custom_purity", "custom_purity_percentage", "custom_gross_weight", "custom_less_weight",
             "custom_net_weight", "custom_westage", "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate",
             "custom_other_amount", "custom_sales_labour_type", "custom_value_added", "custom_sales_labour_amount", "custom_is_jewellery_item"]

    print(parentfield)
    sle = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype}, fields=['serial_no','item_code','voucher_detail_no'])
    print("\n\n" + str(sle))
    if not sle:
        frappe.msgprint("No Stock Ledger Entry found for this controller")
        return
    for d in controller.get("items"):
        for sle1 in sle:
            if sle1.voucher_detail_no == d.name:  
                if sle1.serial_no and sle1.serial_no != '':
                    serial_numbers = sle1['serial_no'].split('\n')
                    for serial_no in serial_numbers:
                        print("\n\n"+str(serial_no))        
                        if controller.doctype == "Stock Entry":
                            data = frappe.db.get_all('Stock Entry Detail', filters={"parent": controller.name, "item_code": sle1.item_code, "name":d.name}, fields=field)
                        elif controller.doctype == "Purchase Receipt":
                            data = frappe.db.get_all('Purchase Receipt Item', filters={"parent": controller.name, "item_code": sle1.item_code, "name":d.name}, fields=field)
                        elif controller.doctype == "Purchase Invoice":
                            data = frappe.db.get_all('Purchase Invoice Item', filters={"parent": controller.name, "item_code": sle1.item_code, "name":d.name}, fields=field)
                        else:
                            frappe.msgprint("Not Available Serial No for this doctype")
                            return
                        if data:
                            record = data[0]
                            target_doc = frappe.get_doc('Serial No', serial_no)
                           
                            for key in field:
                                setattr(target_doc, key, record.get(key))
                            
                            target_doc.save()
                        else:
                            frappe.msgprint(f"No data found for serial no: {serial_no}")
                else:
                    frappe.msgprint(f"Not created has Serial No. this Item code: {sle1.item_code}")


      
               




			

#------------it is work on barcode scane to fetch custom field value --------------------

@frappe.whitelist()
def custom_scan_barcode(search_value: str) -> BarcodeScanResult:
	def set_cache(data: BarcodeScanResult):
		frappe.cache().set_value(f"erpnext:barcode_scan:{search_value}", data, expires_in_sec=120)

	def get_cache() -> Optional[BarcodeScanResult]:
		if data := frappe.cache().get_value(f"erpnext:barcode_scan:{search_value}"):
			return data

	if scan_data := get_cache():
		return scan_data

	# search barcode no
	barcode_data = frappe.db.get_value(
		"Item Barcode",
		{"barcode": search_value},
		["barcode", "parent as item_code","uom"],
		as_dict=True,
	)
	if barcode_data:
		_update_item_info(barcode_data)
		set_cache(barcode_data)
		return barcode_data

	# search serial no
	serial_no_data = frappe.db.get_value(
		"Serial No",
		{"name":search_value,"status":"Active"},
		["name as serial_no", "item_code", "batch_no","custom_metal_type", "custom_purity", "custom_purity_percentage", "custom_gross_weight", 
		"custom_less_weight","custom_net_weight", "custom_westage", "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate",
        "custom_other_amount", "custom_sales_labour_type", "custom_value_added", "custom_sales_labour_amount", "custom_is_jewellery_item"],
		as_dict=True,
	)
	if serial_no_data:		
		_update_item_info(serial_no_data)
		set_cache(serial_no_data)
		print("\n\n\n"+str(serial_no_data))
		return serial_no_data
	else:
		frappe.msgprint(search_value +" this serial no. not Active")

	# search batch no
	batch_no_data = frappe.db.get_value(
		"Batch",
		search_value,
		["name as batch_no", "item as item_code"],
		as_dict=True,
	)
	if batch_no_data:
		_update_item_info(batch_no_data)
		set_cache(batch_no_data)
		return batch_no_data

	return {}


def _update_item_info(scan_result: Dict[str, Optional[str]]) -> Dict[str, Optional[str]]:
	if item_code := scan_result.get("item_code"):
		if item_info := frappe.get_cached_value(
			"Item",
			item_code,
			["has_batch_no", "has_serial_no", "custom_metal_type", "custom_purity", "custom_purity_percentage" ],
			as_dict=True,
		):
			scan_result.update(item_info)
			
	return scan_result
    
 

	
