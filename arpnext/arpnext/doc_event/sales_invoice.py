import frappe
@frappe.whitelist()
def add_remarks(doc,method):
    items=""
    for item in doc.get("items"):
        items=str(items)+" "+str(item.item_name)
    doc.remarks=str(items)