frappe.ui.form.on('Customer', {
	refresh: function(frm) {
		if (frm.doc.allow_discount == 0) {
			frm.set_df_property("posa_discount", 'read_only',1);
		}
		else {
			frm.set_df_property("posa_discount", 'read_only',0);
		}
	
	}
});