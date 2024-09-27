// Copyright (c) 2024, hevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Metal Rate', {
    refresh_field: function(frm){       
        // frm.page.('get_metal_list','hidden', 1)
        frm.page.get_metal_list.hide();		
    },
	
    get_metal_list: function(frm){ 
        if(frm.is_new()){       
            frm.call({
                doc: frm.doc,
                method: 'set_child_table_data',
                args: {
                    
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
            
    }

	
});
