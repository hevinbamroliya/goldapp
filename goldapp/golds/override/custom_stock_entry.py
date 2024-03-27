import frappe

from typing import Dict, Optional
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from erpnext.stock.doctype.serial_no.serial_no import SerialNo




class Custom_Stock_Entery(Document):
	pass
	







    # def scan_barcode(barcode):  
    #     print("\n\n\n hello ")    
        # item = frappe.get_all("Item", filters={"barcode": barcode}, fields=["metal_type","purity"])
        # if item:
        #     return item[0] 
        # else:
        #     return None 

        # doc.append("Stock Entry Detail", {
        #         "custom_metal_type": "custom_metal_type",
        #         "custom_purity": "custom_purity"
                
        # })


   


     


       
        # source_doc = frappe.get_doc("Stock Entry", frm.name)
        # target_doc = frappe.get_doc({"doctype": "Serial No", "purchase_document_no": frm.name})
        # mapped_doc = get_mapped_doc("Stock Entry", frm.name, {
        #     frm.name: {
        #         "doctype": "Stock Entry",
        #         "field_map": {
        #                         "custom_size": "custom_size",
        #                         "custom_metal_type": "custom_metal_type",
        #                         "custom_purity": "custom_purity",
        #                         "custom_purity_percentage": "custom_purity_percentage",
        #                         "custom_gross_weight": "custom_gross_weight",
        #                         "custom_less_weight": "custom_less_weight",
        #                         "custom_net_weight": "custom_net_weight",
        #                         "custom_westage": "custom_westage",
        #                         "custom_fine_weight": "custom_fine_weight",
        #                         "custom_gold_rate": "custom_gold_rate",
        #                         "custom_gold_value": "custom_gold_value",
        #                         "custom_mrp_rate": "custom_mrp_rate",
        #                         "custom_other_amount": "custom_other_amount",
        #                         "custom_labour_type": "custom_labour_type",
        #                         "custom_sales_labour_rate": "custom_sales_labour_rate",
        #                         "custom_labour_amount": "custom_labour_amount",
        #                         "custom_is_jewellery_item": "custom_is_jewellery_item",
        #                         "custom_item_image": "custom_item_image"
        #                     }

        #     }
        # }, target_doc)

        # mapped_doc.insert()
        # print(mapped_doc)
        # return
        
       