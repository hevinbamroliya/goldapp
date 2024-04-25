frappe.ui.form.on('Purchase Invoice', {
    custom_booking_rate: function(frm) {        
        var custom_booking_rate = frm.doc.custom_booking_rate;     
        frm.doc.items.forEach(function(row) {
            var custom_fine_weight = row.custom_fine_weight;                      
            if (custom_fine_weight && custom_booking_rate) {
                var fine_value = custom_fine_weight * custom_booking_rate;               
                frappe.model.set_value(row.doctype, row.name, 'custom_fine_value', fine_value);                
            }            
       });
    },  
   
})


frappe.ui.form.on('Purchase Invoice Item', {
    
    custom_gross_weight: function(frm, cdt, cdn) {
        updateItem(frm, cdt, cdn);
    },
    custom_less_weight: function(frm, cdt, cdn) {
        updateItem(frm, cdt, cdn);
    }, 
    custom_purity_percentage: function(frm, cdt, cdn) {
        updateItem(frm, cdt, cdn);
    }, 
    qty: function(frm, cdt, cdn) {
        saleslabouramount(frm, cdt, cdn);
        labouramount(frm, cdt, cdn);
    },  
    custom_labour_amount: function(frm, cdt, cdn){
        tatoalamount(frm, cdt, cdn);
    },
    custom_gold_value: function(frm, cdt, cdn){
        tatoalamount(frm, cdt, cdn);
    },
    custom_other_amount: function(frm, cdt, cdn){
        tatoalamount(frm, cdt, cdn);
    },    
    custom_fine_weight: function(frm, cdt, cdn){
        finevalue(frm, cdt, cdn);
        calculateTotal(frm, cdt, cdn);
    },
   
    custom_sales_labour_type: function(frm, cdt, cdn){
        saleslabouramount(frm, cdt, cdn);
    },
    custom_labour_type: function(frm, cdt, cdn){
        labouramount(frm, cdt, cdn);
    },
    custom_total_amount: function(frm, cdt, cdn){
        calculateTotal(frm, cdt, cdn);
    },
    

   

});
//-----calculate custom net weight , custom fine weight , custom gold value -------//
function updateItem(frm, cdt, cdn) {
    var child_doc = locals[cdt][cdn];

    var custom_gross_weight = child_doc.custom_gross_weight ;
    var custom_less_weight = child_doc.custom_less_weight;
    var custom_purity_percentage = child_doc.custom_purity_percentage;
    var custom_gold_rate = child_doc.custom_gold_rate;
    

    var custom_net_weight = custom_gross_weight - custom_less_weight;
    var fine_weight = custom_net_weight / (custom_purity_percentage / 100);
    var gold_value = custom_gold_rate * custom_net_weight;
    
    

    frappe.model.set_value(cdt, cdn, 'custom_net_weight', custom_net_weight);
    
    if(custom_net_weight && custom_purity_percentage ){
        frappe.model.set_value(cdt, cdn, 'custom_fine_weight', fine_weight);
    }
    if(custom_net_weight && custom_gold_rate){
        frappe.model.set_value(cdt, cdn, 'custom_gold_value', gold_value);
    }    
}



//-----calculate custom net weight , custom fine weight-------//
function finevalue(frm,cdt,cdn){
    var child_doc = locals[cdt][cdn];

    var custom_booking_rate = frm.doc.custom_booking_rate;
    var custom_fine_weight = child_doc.custom_fine_weight;
    var custom_gold_rate = child_doc.custom_gold_rate;   

    var fine_value = 0
    
    if(custom_fine_weight && custom_booking_rate){              
        fine_value = custom_fine_weight * custom_booking_rate;               
    }
    else{
        fine_value = custom_fine_weight * custom_gold_rate;
    }

    frappe.model.set_value(cdt, cdn, 'custom_fine_value', fine_value); 
}


//-----calculate custom amount------//
function tatoalamount(frm, cdt, cdn){
    var child_doc = locals[cdt][cdn];

    var custom_gold_value = child_doc.custom_gold_value;
    var custom_other_amount = child_doc.custom_other_amount;
    var custom_labour_amount = child_doc.custom_labour_amount;

    var total_amount = custom_gold_value + custom_other_amount + custom_labour_amount;
    frappe.model.set_value(cdt, cdn, 'custom_total_amount', total_amount);
    frappe.model.set_value(cdt, cdn, 'rate', total_amount);

        
   

}

//-----calculate custom sales labour amountt------//
function saleslabouramount(frm, cdt, cdn){
    var child_doc = locals[cdt][cdn];

    var quantity = child_doc.qty;
    var salestype = child_doc.custom_sales_labour_type;
    var custom_gold_rate = child_doc.custom_gold_rate;
    var custom_fine_weight = child_doc.custom_fine_weight;
    var custom_net_weight = child_doc.custom_net_weight;
    var custom_gross_weight = child_doc.custom_gross_weight;

    var fine_value = custom_fine_weight * custom_gold_rate;
    

    if(salestype == 'Flat'){
        var flat = 36 * quantity;
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', flat);
        frappe.model.set_value(cdt, cdn, 'custom_value_added', 36);
       
    }

    if(salestype == 'On Gold Value Percentage'){
        var Percentage = fine_value * (15 / 100);
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', Percentage);
        frappe.model.set_value(cdt, cdn, 'custom_value_added', 15);
    }

    if(salestype == 'On Gross Weight Per Gram'){
        var Percentage = custom_gross_weight * 25;
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', Percentage);
        frappe.model.set_value(cdt, cdn, 'custom_value_added', 25);
    }

    if(salestype == 'On Net Weight Per Gram'){
        var netweight =  custom_net_weight * 30;
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', netweight);
        frappe.model.set_value(cdt, cdn, 'custom_value_added', 30);
    }   
}


//-----calculate custom labour amountt------//
function labouramount(frm, cdt, cdn){
    var child_doc = locals[cdt][cdn];

    var quantity = child_doc.qty;
    var salestype = child_doc.custom_labour_type;
    var custom_fine_value = child_doc.custom_fine_value;
    var custom_net_weight = child_doc.custom_net_weight;
    var custom_gross_weight = child_doc.custom_gross_weight;   
       

    if(salestype == 'Flat'){
        var flat =  36 * quantity;
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', flat);
        frappe.model.set_value(cdt, cdn, 'custom_labour_rate', 36);
    }

    if(salestype == 'On Gold Value Percentage'){
        var Percentage = custom_fine_value * (15 / 100);
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', Percentage);
        frappe.model.set_value(cdt, cdn, 'custom_labour_rate', 15);
    }

    if(salestype == 'On Gross Weight Per Gram'){
        var Percentage = custom_gross_weight * 25;
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', Percentage);
        frappe.model.set_value(cdt, cdn, 'custom_labour_rate', 25);
    }

    if(salestype == 'On Net Weight Per Gram'){
        var netweight =  custom_net_weight * 30;
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', netweight);
        frappe.model.set_value(cdt, cdn, 'custom_labour_rate', 30);
    }
}



//-----set all Total in purchase order------//
function  calculateTotal(frm){
    var net_weight = 0, fine_weight = 0, gross_weight = 0,less_weight = 0;
    frm.doc.items.forEach(function(row) {
        net_weight += row.custom_net_weight;
        fine_weight += row.custom_fine_weight;
        gross_weight += row.custom_gross_weight;
        less_weight += row.custom_less_weight;
        
                  
    });       
    frm.set_value('custom_total_net_weight', net_weight);
    frm.set_value('custom_total_fine_weight', fine_weight);
    frm.set_value('custom_total_gross_weight', gross_weight);
    frm.set_value('custom_total_less_weight', less_weight);
     
}