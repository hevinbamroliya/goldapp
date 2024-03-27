import frappe
from typing import Dict, Optional
from frappe.model.document import Document
from frappe.model.mapper import map_doc


BarcodeScanResult = Dict[str, Optional[str]]
	
@frappe.whitelist()
# def custom_update_serial_nos_after_submit(controller, parentfield):
#     field = ["custom_size","custom_metal_type","custom_purity","custom_purity_percentage","custom_gross_weight","custom_less_weight","custom_net_weight","custom_westage","custom_fine_weight","custom_gold_rate","custom_gold_value","custom_mrp_rate","custom_other_amount","custom_sales_labour_type","custom_value_added","custom_sales_labour_amount","custom_is_jewellery_item"]

#     field_map = {
#         # "Stock Entry Detail": field,
#         "Purchase Receipt Item": field,
#         # "Purchase Invoice Item": field
#     }

#     def update_serial_no(record, target_doc, field_map):
#         doc_type = record.get("doctype")
#         if doc_type not in field_map:
#             return

#         mapped_values = map_doc(record, target_doc, field_map[doc_type])

#         target_doc.update(mapped_values)
#         target_doc.save()

#     documents = [
#         # frappe.get_all('Stock Entry Detail', filters={"parent": controller.name},fields=field),
#         frappe.get_all('Purchase Receipt Item', filters={"parent": controller.name},fields=field),
#         # frappe.get_all('Purchase Invoice Item', filters={"parent": controller.name},fields=field)
#     ]

#     sle = frappe.db.get_all('Stock Ledger Entry',filters={"voucher_no": controller.name, "voucher_type": controller.doctype},fields=['serial_no'])
    
#     for document_list in documents:
#         for record in document_list:
#             target_doc = frappe.get_doc('Serial No', sle)
#             update_serial_no(record, target_doc, field_map)


# # ---------it is work on serial no set custom fields --------------   

@frappe.whitelist()
def custom_update_serial_nos_after_submit(controller, parentfield):
	
	field = ["custom_size", "custom_metal_type", "custom_purity", "custom_purity_percentage", "custom_gross_weight", "custom_less_weight",
			 "custom_net_weight", "custom_westage", "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate", 
			 "custom_other_amount", "custom_sales_labour_type", "custom_sales_labour_rate", "custom_sales_labour_amount", "custom_is_jewellery_item"]
	sle = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype}, fields=['serial_no'])

	if "Stock Entry" == controller.doctype:
		data = frappe.db.get_all('Stock Entry Detail', filters={"parent": controller.name}, fields=field)
	elif "Purchase Receipt" == controller.doctype:
		data = frappe.db.get_all('Purchase Receipt Item', filters={"parent": controller.name}, fields=field)
	elif "Purchase Invoice" == controller.doctype:
		data = frappe.db.get_all('Purchase Invoice Item', filters={"parent": controller.name}, fields=field)
	else:
		frappe.msgprint("Not Available Serial No for this doctype")

	for record in data:	
			target_doc = frappe.get_doc('Serial No', sle)
			target_doc.custom_size = record.custom_size
			target_doc.custom_metal_type = record.custom_metal_type
			target_doc.custom_purity = record.custom_purity
			target_doc.custom_purity_percentage = record.custom_purity_percentage
			target_doc.custom_gross_weight = record.custom_gross_weight
			target_doc.custom_less_weight = record.custom_less_weight
			target_doc.custom_net_weight = record.custom_net_weight
			target_doc.custom_westage = record.custom_westage
			target_doc.custom_fine_weight = record.custom_fine_weight
			target_doc.custom_gold_rate = record.custom_gold_rate
			target_doc.custom_gold_value = record.custom_gold_value
			target_doc.custom_mrp_rate = record.custom_mrp_rate
			target_doc.custom_other_amount = record.custom_other_amount
			target_doc.custom_labour_type = record.custom_sales_labour_type
			target_doc.custom_sales_labour_rate = record.custom_sales_labour_rate
			target_doc.custom_sales_labour_amount = record.custom_sales_labour_amount
			target_doc.custom_is_jewellery_item = record.custom_is_jewellery_item
			target_doc.save()
	
	
	


	
	
	
      
        

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
		search_value,
		["name as serial_no", "item_code", "batch_no"],
		as_dict=True,
	)
	if serial_no_data:
		_update_item_info(serial_no_data)
		set_cache(serial_no_data)
		return serial_no_data

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
			["has_batch_no", "has_serial_no", "custom_metal_type", "custom_purity"],
			as_dict=True,
		):
			scan_result.update(item_info)
			
			print("\n\n\n"+str(scan_result))
	return scan_result
    
 




					




      

# @frappe.whitelist()
# def fetchdata(doc_no,item_code): 
#     stock_entries = frappe.get_all("Stock Entry Detail", filters={"parent": doc_no,"item_code":item_code },fields=["custom_size","custom_metal_type","custom_purity","custom_purity_percentage","custom_gross_weight","custom_less_weight","custom_net_weight","custom_westage","custom_fine_weight","custom_gold_rate","custom_gold_value","custom_mrp_rate","custom_other_amount","custom_labour_type","custom_sales_labour_rate","custom_labour_amount","custom_is_jewellery_item","custom_item_image"])
#     return stock_entries
    



# source_doc = frappe.get_doc("Stock Entry", frm.name)
# target_doc = frappe.get_doc({"doctype": "Serial No", "purchase_document_no": frm.name})
# mapped_doc = get_mapped_doc("Stock Entry", frm.name, {
#     frm.name: {
#         "doctype": "Stock Entry",
#         "field_map": {
#             "custom_size","custom_metal_type","custom_purity","custom_purity_percentage","custom_gross_weight","custom_less_weight","custom_net_weight","custom_westage","custom_fine_weight","custom_gold_rate","custom_gold_value","custom_mrp_rate","custom_other_amount","custom_labour_type","custom_sales_labour_rate","custom_labour_amount","custom_is_jewellery_item","custom_item_image"
#         }
#     }
# }, target_doc)

# mapped_doc.insert()





# # Register the hook to execute the function on Material Request save
# def execute_serial_number_generation(doc, method):
#     if doc.doctype == "Material Request" and method == "on_update":
#         material_request = MaterialRequest(doc)
#         material_request.generate_serial_numbers()

# # Register the hook
# frappe.get_doc("DocType", "Material Request").add_fetch_method("on_update", __name__ + ".execute_serial_number_generation")

# # Example usage:
# # When a Material Request is saved, the hook will execute the generate_serial_numbers function
