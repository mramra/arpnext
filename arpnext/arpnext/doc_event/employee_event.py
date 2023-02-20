import frappe
from frappe.utils import time_diff_in_hours

def validate_branch(doc,method):
	if doc.status == 'Left':
		if not doc.branch:
			frappe.throw('Must be Enter Reason For branch')

def validate_creat_task(doc,method):
	if doc.status == 'Left':
		task_doc=frappe.new_doc("Task")
		task_doc.subject=str(doc.employee_name) + " End Of Service"
		task_doc.insert()

def validate_hours(doc,method):
    if doc.check_in and doc.check_out:
        diff_hours = time_diff_in_hours(doc.check_out, doc.check_in)
        doc.hours_ = diff_hours
    else:
        doc.status = "Absent"

@frappe.whitelist()
def get_age(birth_day):
	return 30
