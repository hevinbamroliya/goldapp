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


	



# @frappe.whitelist()
# def custom_update_serial_nos_after_submit(controller, parentfield):
#     stock_ledger_entries = frappe.db.sql(
#         """SELECT voucher_detail_no, serial_no, actual_qty, warehouse, item_code
#         FROM `tabStock Ledger Entry` WHERE voucher_type=%s AND voucher_no=%s""",
#         (controller.doctype, controller.name),
#         as_dict=True,
#     )

#     field = ["custom_size", "custom_metal_type", "custom_purity", "custom_purity_percentage", "custom_gross_weight", "custom_less_weight",
#              "custom_net_weight", "custom_westage", "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate",
#              "custom_other_amount", "custom_sales_labour_type", "custom_value_added", "custom_sales_labour_amount", "custom_is_jewellery_item"]

#     if not stock_ledger_entries:
#         return

#     for sle in stock_ledger_entries:
#         item_code = sle.item_code

#         if controller.doctype == "Stock Entry":
#             data = frappe.db.get_all('Stock Entry Detail', filters={"parent": controller.name, "item_code": item_code}, fields=field)
#         elif controller.doctype == "Purchase Receipt":
#             data = frappe.db.get_all('Purchase Receipt Item', filters={"parent": controller.name, "item_code": item_code}, fields=field)
#         elif controller.doctype == "Purchase Invoice":
#             data = frappe.db.get_all('Purchase Invoice Item', filters={"parent": controller.name, "item_code": item_code}, fields=field)
#         else:
#             frappe.msgprint("Not Available Serial No for this doctype")
#             return

#         for d in controller.get("items"):
#             print(controller.get("items"))

#             if d.serial_no:
#                 continue

#             update_rejected_serial_nos = (
#                 True
#                 if (
#                     controller.doctype in ("Purchase Receipt", "Purchase Invoice", "Subcontracting Receipt")
#                     and d.rejected_qty
#                 )
#                 else False
#             )
#             accepted_serial_nos_updated = False

#             if controller.doctype == "Stock Entry":
#                 warehouse = d.t_warehouse
#                 qty = d.transfer_qty
#             elif controller.doctype in ("Sales Invoice", "Delivery Note"):
#                 warehouse = d.warehouse
#                 qty = d.stock_qty
#             else:
#                 warehouse = d.warehouse
#                 qty = (
#                     d.qty
#                     if controller.doctype in ["Stock Reconciliation", "Subcontracting Receipt"]
#                     else d.stock_qty
#                 )

#             if sle.voucher_detail_no == d.name:
#                 if (
#                     not accepted_serial_nos_updated
#                     and qty
#                     and abs(sle.actual_qty) == abs(qty)
#                     and sle.warehouse == warehouse
#                     and sle.serial_no != d.serial_no
#                 ):
#                     d.serial_no = sle.serial_no
#                     frappe.db.set_value(d.doctype, d.name, "serial_no", sle.serial_no)
#                     print("\n\n"+str(sle.serial_no))
#                     if data:
#                         record = data[0]
#                         target_doc = frappe.get_doc('Serial No', sle.serial_no)
#                         print("\n"+str(sle.serial_no))
#                         for key in field:
#                             setattr(target_doc, key, record.get(key))

#                         target_doc.save()
#                     else:
#                         frappe.msgprint(f"No data found for serial no: {sle.serial_no}")

#                     accepted_serial_nos_updated = True
#                     if not update_rejected_serial_nos:
#                         break
#                 elif (
#                     update_rejected_serial_nos
#                     and abs(sle.actual_qty) == d.rejected_qty
#                     and sle.warehouse == d.rejected_warehouse
#                     and sle.serial_no != d.rejected_serial_no
#                 ):
#                     d.rejected_serial_no = sle.serial_no
#                     frappe.db.set_value(d.doctype, d.name, "rejected_serial_no", sle.serial_no)
#                     print("\n\n"+str(sle.serial_no))
#                     if data:
#                         record = data[0]
#                         target_doc = frappe.get_doc('Serial No', sle.serial_no)
#                         print("\n"+str(sle.serial_no))
#                         for key in field:
#                             setattr(target_doc, key, record.get(key))

#                         target_doc.save()
#                     else:
#                         frappe.msgprint(f"No data found for serial no: {sle.serial_no}")
#                     update_rejected_serial_nos = False
#                     if accepted_serial_nos_updated:
#                         break


   
    

                 
               




			

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
