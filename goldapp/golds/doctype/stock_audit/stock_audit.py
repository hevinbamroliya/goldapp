# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class StockAudit(Document):
	pass
	# @frappe.whitelist()
	# def stockiten(self):
	# 	return frappe.db.count("Stock Entry")



@frappe.whitelist()
def fetchdata(doc_no): 	
	stock_entries1 = frappe.db.get_all("Stock Entry Detail", filters={"parent": doc_no}, fields=["custom_size","custom_metal_type","custom_purity","custom_purity_percentage","custom_gross_weight","custom_less_weight","custom_net_weight","custom_westage","custom_fine_weight","custom_gold_rate","custom_gold_value","custom_mrp_rate","custom_other_amount","custom_sales_labour_type","custom_value_added","custom_sales_labour_amount","custom_is_jewellery_item"])
	if stock_entries1:
		return stock_entries1

	 			
	stock_entries = frappe.db.get_all("Purchase Receipt Item", filters={"parent": doc_no}, fields = ["custom_size","custom_metal_type","custom_purity","custom_purity_percentage","custom_gross_weight","custom_less_weight","custom_net_weight","custom_westage","custom_fine_weight","custom_gold_rate","custom_gold_value","custom_mrp_rate","custom_other_amount","custom_sales_labour_type","custom_value_added","custom_sales_labour_amount","custom_is_jewellery_item"])
	if stock_entries:
		return stock_entries  


@frappe.whitelist()
def scan_barcode(barcode):    
    return frappe.db.sql("""
            SELECT
               *	
            FROM `tabItem Barcode` AS ib
            INNER JOIN `tabItem` AS i
            ON ib.parent = i.name 
            WHERE barcode = %s
        """, (barcode))
    
	
	
