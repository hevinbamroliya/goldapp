frappe.ui.form.on('Serial No', {
    before_load: function(frm) {
        var fields = ["custom_size", "custom_metal_type", "custom_purity", "custom_purity_percentage", "custom_gross_weight", "custom_less_weight",
             "custom_net_weight", "custom_westage", "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate",
             "custom_other_amount", "custom_sales_labour_type", "custom_value_added", "custom_sales_labour_amount", "custom_is_jewellery_item"];
             
        for (var i = 0; i < fields.length; i++) {
            frm.set_df_property(fields[i], "read_only", 1);
        }
    }
});