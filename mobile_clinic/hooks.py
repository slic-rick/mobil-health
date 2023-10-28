from . import __version__ as app_version

app_name = "mobile_clinic"
app_title = "Mobile Clinic"
app_publisher = "Wellness Warriors"
app_description = "An ERP for managing a clinic"
app_email = "erickabraham63@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mobile_clinic/css/mobile_clinic.css"
# app_include_js = "/assets/mobile_clinic/js/mobile_clinic.js"

# include js, css files in header of web template
# web_include_css = "/assets/mobile_clinic/css/mobile_clinic.css"
# web_include_js = "/assets/mobile_clinic/js/mobile_clinic.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mobile_clinic/public/scss/website"

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
#	"methods": "mobile_clinic.utils.jinja_methods",
#	"filters": "mobile_clinic.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mobile_clinic.install.before_install"
# after_install = "mobile_clinic.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mobile_clinic.uninstall.before_uninstall"
# after_uninstall = "mobile_clinic.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mobile_clinic.notifications.get_notification_config"

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

override_doctype_class = {
	"Patient": "mobile_clinic.overrides.patient.CustomPatient",
    "Patient Appointment": "mobile_clinic.overrides.appointment.Appointment",
}

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"mobile_clinic.tasks.all"
#	],
#	"daily": [
#		"mobile_clinic.tasks.daily"
#	],
#	"hourly": [
#		"mobile_clinic.tasks.hourly"
#	],
#	"weekly": [
#		"mobile_clinic.tasks.weekly"
#	],
#	"monthly": [
#		"mobile_clinic.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "mobile_clinic.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "mobile_clinic.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "mobile_clinic.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mobile_clinic.utils.before_request"]
# after_request = ["mobile_clinic.utils.after_request"]

# Job Events
# ----------
# before_job = ["mobile_clinic.utils.before_job"]
# after_job = ["mobile_clinic.utils.after_job"]

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
#	"mobile_clinic.auth.validate"
# ]
fixtures = ["Custom Field"]
