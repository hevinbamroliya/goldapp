frappe.ui.form.on('Purchase Receipt Item', {
    item_code: fetchGoldRate,
    custom_gold_type: fetchGoldRate,
    custom_purity: fetchGoldRate, 
    custom_gross_weight: updateItem,
    custom_less_weight: updateItem,
    custom_purity_percentage: updateItem,
    qty:saleslabouramount,labouramount,    
    custom_labour_amount: tatoalamount,
    custom_fine_weight: finevalue,
    custom_sales_labour_type: saleslabouramount,
    custom_labour_type: labouramount,
    custom_total_amount: calculateTotal,
      
    

   

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

    var custom_gold_rate = child_doc.custom_gold_rate;
    var custom_fine_weight = child_doc.custom_fine_weight;

    var fine_value = custom_fine_weight * custom_gold_rate;  

    if(custom_fine_weight !== undefined && custom_gold_rate !== undefined){
              
        frappe.model.set_value(cdt, cdn, 'custom_fine_value', fine_value);
        
    }
}


//-----calculate custom amount------//
function tatoalamount(frm, cdt, cdn){
    var child_doc = locals[cdt][cdn];

    var custom_gold_value = child_doc.custom_gold_value;
    var custom_other_amount = child_doc.custom_other_amount;
    var custom_labour_amount = child_doc.custom_labour_amount;

    var total_amount = custom_gold_value + custom_other_amount + custom_labour_amount;
    if(custom_gold_value && custom_other_amount && custom_labour_amount){
        frappe.model.set_value(cdt, cdn, 'custom_total_amount', total_amount);
        
    }

}

//-----calculate custom sales labour amountt------//
function saleslabouramount(frm, cdt, cdn){
    var child_doc = locals[cdt][cdn];

    var custom_value_added = child_doc.custom_value_added;
    var quantity = child_doc.qty;
    var salestype = child_doc.custom_sales_labour_type;
    var custom_fine_value = child_doc.custom_fine_value;
    var custom_net_weight = child_doc.custom_net_weight;
    var custom_gross_weight = child_doc.custom_gross_weight;
   
     

    if(salestype == 'Flat'){
        var flat = custom_value_added * quantity;
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', flat);
    }

    if(salestype == 'On Gold Value Percentage'){
        var Percentage = custom_fine_value * (custom_value_added / 100);
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', Percentage);
    }

    if(salestype == 'On Gross Weight Per Gram'){
        var Percentage = custom_gross_weight * custom_value_added;
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', Percentage);
    }

    if(salestype == 'On Net Weight Per Gram'){
        var netweight =  custom_net_weight * custom_value_added;
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', netweight);
    }   
}


//-----calculate custom labour amountt------//
function labouramount(frm, cdt, cdn){
    var child_doc = locals[cdt][cdn];

    var custom_labour_rate = child_doc.custom_labour_rate;
    var quantity = child_doc.qty;
    var salestype = child_doc.custom_labour_type;
    var custom_fine_value = child_doc.custom_fine_value;
    var custom_net_weight = child_doc.custom_net_weight;
    var custom_gross_weight = child_doc.custom_gross_weight;   
       

    if(salestype == 'Flat'){
        var flat =  custom_labour_rate * quantity;
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', flat);
    }

    if(salestype == 'On Gold Value Percentage'){
        var Percentage = custom_fine_value * (custom_labour_rate / 100);
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', Percentage);
    }

    if(salestype == 'On Gross Weight Per Gram'){
        var Percentage = custom_gross_weight * custom_labour_rate;
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', Percentage);
    }

    if(salestype == 'On Net Weight Per Gram'){
        var netweight =  custom_net_weight * custom_labour_rate;
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', netweight);
    }
}


//-----fetch Gold Rate------//
function fetchGoldRate(frm, cdt, cdn) {
    var child_doc = locals[cdt][cdn];
    var custom_purity = child_doc.custom_purity;
    var custom_metal = child_doc.custom_metal_type
    var date = frm.doc.posting_date;
   
    frm.call({        
        method: 'goldapp.golds.doctype.metal_rate.metal_rate.query',
        args: {           
           
            purity:custom_purity,
            metal_type:custom_metal,
            date:date,       
            
        },
        callback: function(r) {
            var rate = r.message[0];
            frappe.model.set_value(cdt, cdn, 'custom_gold_rate', rate);

        }
    });
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