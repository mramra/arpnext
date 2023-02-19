import frappe

def validate_branch(doc,method):
	if doc.status == 'Left':
		if not doc.branch:
			frappe.throw('Must be Enter Reason For branch')