import frappe

def validate(doc, method):
    for i in doc.get('items'):
        if(i.custom_gross_weight <= 0):
            frappe.msgprint("plase Checked gross Weight")
        
        if(i.custom_less_weight < 0):
            frappe.msgprint("plase Checked less Weight")