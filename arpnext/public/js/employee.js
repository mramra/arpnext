frappe.ui.form.on("Employee", {
    get_age: function(frm) {
        frappe.call({
            method:"arpnext.arpnext.doc_event.employee_event.get_age",
            args:{
                birth_day:frm.doc.date_of_birth
            },
            callback: function(r){
                frm.set_value("age",r.message);
            }
        })
		
	},
});