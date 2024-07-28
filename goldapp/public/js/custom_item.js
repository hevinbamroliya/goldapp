frappe.ui.form.on('Item', {
    custom_metal_type: function (frm) {        
        frm.set_query("custom_purity", ()=> {
            return {
                filters: [
                    ["Purity", "metal_type", "=", frm.doc.custom_metal_type]
                ]
            };
        });
    }
})