# Copyright (c) 2023, arpnext and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import time_diff_in_hours
from frappe.model.document import Document

class EmployeeExcuseApplication(Document):
	def validate(self):
		self.validate_max_hours()
	def on_submit(self):
		self.create_attendance()
	def validate_max_hours(self):
		if self.to_time and self.from_time:
			diff_hour=time_diff_in_hours(self.to_time,self.from_time)
			if float(diff_hour>2):
				frappe.throw("must be less 2 hour")
	def create_attendance(self):
		attendance_doc=frappe.new_doc("Attendance")
		attendance_doc.employee=self.employee
		attendance_doc.attendance_date=self.excuse_date
		attendance_doc.status='Present'
		attendance_doc.insert()
