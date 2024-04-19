// Copyright (c) 2024, hevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Metal Rate', {
	
    get_metal_list: function(frm){
        frm.call({
			method: 'goldapp.golds.doctype.metal_rate.metal_rate.set_child_table_data',
			args: {
				docname:frm.doc
			},
			callback: function(r) {
				
                    frm.clear_table("daily_metal_rate");
                    $.each(r.message, function (index,data) {
                        index = frm.add_child("daily_metal_rate");
                        index.metal_type = data.metal_type;
                        index.purity = data.purity; 
                       
                    });
                    frm.refresh_field("daily_metal_rate");
                
			}
			
		})      
          
      
    }

	
});
