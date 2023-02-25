from . import __version__ as app_version

app_name = "arpnext"
app_title = "Arpnext"
app_publisher = "arpnext"
app_description = "arpnext"
app_email = "e@f.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/arpnext/css/arpnext.css"
# app_include_js = "/assets/arpnext/js/arpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/arpnext/css/arpnext.css"
# web_include_js = "/assets/arpnext/js/arpnext.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "arpnext/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "arpnext.utils.jinja_methods",
#	"filters": "arpnext.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "arpnext.install.before_install"
# after_install = "arpnext.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "arpnext.uninstall.before_uninstall"
# after_uninstall = "arpnext.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "arpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

#doc_events = {
#    "Employee": {
#	    "validate": "arpnext.arpnext.doc_event.employee_event.validate_branch"
#     }
#}
doctype_js = {"Employee" : "public/js/employee.js",
              "Quotation" : "public/js/quotation.js",
              
              }
doc_events = {
	 "Employee": {"validate": "arpnext.arpnext.doc_event.employee_event.validate_creat_task"},
	 "Employee": {"validate": "arpnext.arpnext.doc_event.employee_event.validate_date"},
     "Attendance": {"validate": "arpnext.arpnext.doc_event.employee_event.validate_hours"},
	 "Sales Invoice": {"validate": "arpnext.arpnext.doc_event.sales_invoice.add_remarks"},
     "Sales Invoice": {"validate": "arpnext.arpnext.doc_event.sales_invoice.check_pos"},
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"arpnext.tasks.all"
#	],
#	"daily": [
#		"arpnext.tasks.daily"
#	],
#	"hourly": [
#		"arpnext.tasks.hourly"
#	],
#	"weekly": [
#		"arpnext.tasks.weekly"
#	],
#	"monthly": [
#		"arpnext.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "arpnext.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "arpnext.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "arpnext.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"arpnext.auth.validate"
# ]
