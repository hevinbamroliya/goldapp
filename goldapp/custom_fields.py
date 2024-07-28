CUSTOM_FIELDS = {
    "Sales Invoice": [
        {
            "fieldname": "custom_wholesale",
            "fieldtype": "Check",
            "label": "Wholesale",
            "insert_after": "update_stock",
        },
        {
            "fieldname": "custom_total_net_weight",
            "fieldtype": "Float",
            "label": "Total Net Weight",            
            "insert_after": "section_break_30",
        },
        {
            "fieldname": "custom_total_fine_weight",
            "fieldtype": "Float",
            "label": "Total Fine Weight",            
            "insert_after": "custom_total_net_weight",            
        },
        {
            "fieldname": "custom_column_break_ijk7e",
            "fieldtype": "Column Break",            
            "insert_after": "custom_total_fine_weight",            
        },
        {
            "fieldname": "custom_total_gross_weight",
            "fieldtype": "Float",
            "label": "Total Gross Weight",            
            "insert_after": "custom_column_break_ijk7e",            
        }, 
        {
            "fieldname": "custom_total_less_weight",
            "fieldtype": "Float",
            "label": "Total Less Weight",            
            "insert_after": "custom_total_gross_weight",            
        },
        {
            "fieldname": "custom_section_break_yyzel",
            "fieldtype": "Section Break",            
            "insert_after": "custom_total_less_weight",            
        },           
    ],
    "Sales Invoice Item": [
        {
            "fieldname": "custom_section_break_3sjla",
            "fieldtype": "Section Break",            
            "insert_after": "customer_item_code",            
        },
        {
            "fieldname": "custom_size",
            "fieldtype": "Float",
            "label": "Size",
            "insert_after": "custom_section_break_3sjla",
        },
        {
            "fieldname": "custom_metal_type",
            "fieldtype": "Data",
            "label": "Metal Type",
            "insert_after": "custom_size",
        },
        {
            "fieldname": "custom_purity",
            "fieldtype": "Data",
            "label": "Purity",
            "insert_after": "custom_metal_type",
        },
        {
            "fieldname": "custom_purity_percentage",
            "fieldtype": "Data",
            "label": "Purity Percentage",
            "fieldname": "custom_purity",
           
        },
    ]

}
