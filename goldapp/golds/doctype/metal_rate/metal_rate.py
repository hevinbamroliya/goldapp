# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MetalRate(Document):
    pass
    # def validate(self):
    #     for i in self.get('items'):
    #         if i.rate <=0:
    #             frappe.msgprint("Plase checked Item Rate")     
   
        




@frappe.whitelist()
def set_child_table_data(docname):
    return frappe.get_all("Purity", fields=["metal_type", "purity"])



@frappe.whitelist()
def query(purity, date, metal_type):   
    date1 = frappe.get_list("Metal Rate", filters={"date": date , "DocStatus": 1}, fields=["date"])
    if date1:
        return frappe.db.sql("""SELECT
                                        rate
                                    FROM `tabDaily Metal Rate` AS dmr
                                    INNER JOIN `tabMetal Rate` AS mr
                                    ON dmr.parent = mr.name AND mr.DocStatus = 1
                                    WHERE metal_type = %s AND purity = %s AND date = %s
                             """,(metal_type,purity,date))
    
    else:
        frappe.msgprint("this date " + date + " Metal Rate Not Avialabel ather wise not submited")
        return 0




    




    