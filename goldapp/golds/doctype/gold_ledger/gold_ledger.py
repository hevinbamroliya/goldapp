# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class GoldLedger(Document):
	pass

@frappe.whitelist()	
def create_gold_ledger(controller, parentfield):
    sle = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype}, fields=["posting_date","item_code","stock_uom","serial_no","warehouse","voucher_type","voucher_no","fiscal_year","is_cancelled","incoming_rate","stock_value"])

    for entry in sle:
        serial_numbers = entry.serial_no.split('\n')
        serial_counter = 0

        for serial in serial_numbers:            
            serial_counter += 1           
            
            if serial_counter == 2:
                continue

            sn = frappe.db.get_all('Serial No', filters={"serial_no": serial}, fields=["custom_purity","custom_purity_percentage","customer","supplier","custom_fine_weight"])
            
            if controller.docstatus == 1:
                for serial_entry in sn:
                    doc = frappe.new_doc('Gold Ledger')                
                    doc.posting_date = entry.posting_date
                    doc.item_code = entry.item_code
                    doc.uom = entry.stock_uom
                    doc.purity = serial_entry.custom_purity
                    doc.purity_percentage = serial_entry.custom_purity_percentage
                    snl = entry.serial_no       
                    doc.serial_no = snl.replace('\n', ' ')
                    doc.warehouse = entry.warehouse    
                    doc.voucher_type = entry.voucher_type
                    doc.voucher_no = entry.voucher_no
                    doc.fiscal_year = entry.fiscal_year
                    doc.is_cancelled = entry.is_cancelled
                    doc.account_currency = "NIR"

                    if serial_entry.customer:
                        doc.party_type = "Customer"
                        doc.party = serial_entry.customer
                        doc.debit_amount = entry.incoming_rate
                        doc.debit_gold = serial_entry.custom_fine_weight
                        doc.debit_amount_in_account_currency = doc.debit_amount
                    elif serial_entry.supplier:
                        doc.party_type = "Supplier"
                        doc.party = serial_entry.supplier
                        doc.credit_amount = entry.incoming_rate
                        doc.credit_gold = serial_entry.custom_fine_weight
                        doc.credit_amount_in_account_currency = doc.credit_amount
                    else:
                        doc.credit_amount = entry.incoming_rate
                        doc.credit_gold = serial_entry.custom_fine_weight
                    frappe.show_alert(__("Gold Ledger " + doc.name + " is Crated "), "green")
                    doc.submit()


@frappe.whitelist()	
def remove_gold_ledger(controller, parentfield): 
    sle = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype}, fields=["posting_date","item_code","stock_uom","serial_no","warehouse","voucher_type","voucher_no","fiscal_year","is_cancelled","incoming_rate","stock_value"])

    for entry in sle:
        serial_numbers = entry.serial_no.split('\n')
        serial_counter = 0

        for serial in serial_numbers:            
            serial_counter += 1           
            
            if serial_counter == 2:
                continue

            sn = frappe.db.get_all('Serial No', filters={"serial_no": serial}, fields=["custom_purity","custom_purity_percentage","customer","supplier","custom_fine_weight"])
            
            if controller.docstatus == 2:
                for serial_entry in sn:
                    doc = frappe.new_doc('Gold Ledger')                
                    doc.posting_date = entry.posting_date
                    doc.item_code = entry.item_code
                    doc.uom = entry.stock_uom
                    doc.purity = serial_entry.custom_purity
                    doc.purity_percentage = serial_entry.custom_purity_percentage
                    snl = entry.serial_no       
                    doc.serial_no = snl.replace('\n', ' ')
                    doc.warehouse = entry.warehouse    
                    doc.voucher_type = entry.voucher_type
                    doc.voucher_no = entry.voucher_no
                    doc.fiscal_year = entry.fiscal_year
                    doc.is_cancelled = entry.is_cancelled
                    doc.account_currency = entry.stock_value
                    doc.save()
