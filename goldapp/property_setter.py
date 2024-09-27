import frappe
def get_property_setters():
    return [            
            {
                "doctype": "Sales Invoice",				
				"field_name": "custom_total_net_weight",				
				"property": "read_only",
				"value": 1,
                "property_type": "Check",				
				"is_system_generated": 0,
            },
            {
                "doctype": "Sales Invoice",				
				"field_name": "custom_total_fine_weight",				
				"property": "read_only",
				"value": 1,
                "property_type": "Check",				
				"is_system_generated": 0,
            },
            {
                "doctype": "Sales Invoice",				
				"field_name": "custom_total_gross_weight",				
				"property": "read_only",
				"value": 1,
                "property_type": "Check",				
				"is_system_generated": 0,
            },
            {
                "doctype": "Sales Invoice",				
				"field_name": "custom_total_less_weight",				
				"property": "read_only",
				"value": 1,
                "property_type": "Check",				
				"is_system_generated": 0,
            }
        ]


def execute():
    for field in get_property_setters():
        property_setter = frappe.new_doc("Property Setter")
        property_setter.update(field)
        property_setter.flags.ignore_permissions = True
        property_setter.insert()   
        


    