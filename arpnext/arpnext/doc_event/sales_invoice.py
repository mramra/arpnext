import frappe
@frappe.whitelist()
def add_remarks(doc,method):
    items=""
    for item in doc.get("items"):
        items=str(items)+" "+str(item.item_name)
    doc.remarks=str(items)+str(doc.note)

@frappe.whitelist()
def check_pos(doc,method):
    if doc.is_pos:
        payments = 0
        for item in doc.get("payments"):
            payments = float(item.amount)
        if payments == 0:
            frappe.msgprint("Payment amount must not be equal to 0")
            frappe.throw("Payment amount must not be equal to 0")