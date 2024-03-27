frappe.ui.form.on('Delivery Note Item', {
    custom_gross_weight: function(frm, cdt, cdn) {
        updateCustomNetWeight(frm, cdt, cdn);
    },
    custom_less_weight: function(frm, cdt, cdn) {
        updateCustomNetWeight(frm, cdt, cdn);
    }, 
    custom_purity_percentage: function(frm, cdt, cdn) {
        updateCustomFields(frm, cdt, cdn);
    },
    custom_labour_amount: function(frm, cdt, cdn){
        tatoalamount(frm, cdt, cdn);
    }, 
    item_code: function(frm, cdt, cdn){
        fetchMetalRate(frm, cdt, cdn);
    }



});

function updateCustomNetWeight(frm, cdt, cdn) {
    var child_doc = locals[cdt][cdn];

    var custom_gross_weight = child_doc.custom_gross_weight ;
    var custom_less_weight = child_doc.custom_less_weight;
    var custom_purity_percentage = child_doc.custom__purity_percentage;
   

    var custom_net_weight = custom_gross_weight - custom_less_weight;
    
    var fine_weight = custom_net_weight / (custom_purity_percentage / 100);
    
    if(custom_gross_weight && custom_less_weight){
        frappe.model.set_value(cdt, cdn, 'custom_net_weight', custom_net_weight);
    }
    if(custom_net_weight && custom_purity_percentage ){
        frappe.model.set_value(cdt, cdn, 'custom_fine_weight', fine_weight);
    }
    
    
}

function goldvalue(frm, cdt, cdn) {
    var child_doc = locals[cdt][cdn];
    
    var custom_gold_rate = child_doc.custom_gold_rate;
    var custom_net_weight = child_doc.custom_net_weight;
    
    var gold_value = custom_gold_rate * custom_net_weight;
    
    
    if(custom_net_weight && custom_gold_rate){
        frappe.model.set_value(cdt, cdn, 'custom_gold_value', gold_value);
    }
    
}

function tatoalamount(frm, cdt, cdn){
    var child_doc = locals[cdt][cdn];

    var custom_gold_value = child_doc.custom_gold_value;
    var custom_other_amount = child_doc.custom_other_amount;
    var custom_labour_amount = child_doc.custom_labour_amount;

    var total_amount = parseFloat(custom_gold_value) + parseFloat(custom_other_amount) + parseFloat(custom_labour_amount);
    if(custom_gold_value && custom_other_amount && custom_labour_amount){
        frappe.model.set_value(cdt, cdn, 'custom_total_amount', total_amount);
    }

}