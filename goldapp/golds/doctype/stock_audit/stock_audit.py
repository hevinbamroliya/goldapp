# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class StockAudit(Document):   

    @frappe.whitelist()
    def items_in_stock(self):

        self.total_items_in_stock = frappe.db.count('Serial No', {'status': 'Active'})
       
        items = frappe.db.get_all('Serial No', filters={"status": "Active"}, fields=['name','item_code','item_name'])
        return items

    @frappe.whitelist()
    def serial_number(self):
        serial_number = frappe.db.get_all('Serial No', filters={'name': self.scan_barcode}, fields=['name', 'status' , 'item_code'])
        if serial_number:
            return serial_number

    

 