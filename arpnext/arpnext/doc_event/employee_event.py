import frappe
from frappe.utils import time_diff_in_hours,date_diff,nowdate

def validate_branch(doc,method):
	if doc.status == 'Left':
		if not doc.branch:
			frappe.throw('Must be Enter Reason For branch')

def validate_date(doc,method):
	doc.number_of_wives=0
	doc.children=0
	doc.number_of_years=int(float(date_diff(nowdate(), doc.date_of_joining))/365)
	for x in doc.wives:
		doc.number_of_wives =doc.number_of_wives+1
	for y in doc.sons:
		doc.children =doc.children+1
	
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
	age=date_diff(nowdate(), birth_day)
	return int(float(age)/365)
