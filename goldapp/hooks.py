app_name = "goldapp"
app_title = "golds"
app_publisher = "hevin"
app_description = "gold in erpnext"
app_email = "hevin@x.com"
app_license = "MIT"



app_include_js = ["/assets/goldapp/js/barcode_scanning.js"]
# app_include_js = ["/assets/goldapp/js/serial_no.js",]


scheduler_events = {
	"cron": {
	    "* * * * *": [
	        "goldapp.golds.doctype.gold_scheme.gold_scheme.set_status"
	        ]
	},
}
	 


doc_events = {
    "Stock Entry": {
        "on_submit":[ 
			"goldapp.golds.override.custom_serial_no.custom_update_serial_nos_after_submit",
			"goldapp.golds.doctype.gold_ledger.gold_ledger.create_gold_ledger",
		],
		# "on_cancel":(
		# 	"goldapp.golds.doctype.gold_ledger.gold_ledger.remove_gold_ledger"
		# )	
    },
	
	"Purchase Receipt": {
        "on_submit": [ 
			"goldapp.golds.override.custom_serial_no.custom_update_serial_nos_after_submit",
			"goldapp.golds.doctype.gold_ledger.gold_ledger.create_gold_ledger",
		],
		
    },

	"purchase Invoice":{
		"on_submit": "goldapp.golds.override.custom_serial_no.custom_update_serial_nos_after_submit"
	},
	"Delivery Note":{
		"on_submit":"goldapp.golds.doctype.gold_ledger.gold_ledger.create_gold_ledger"
	},
	# "Property Setter": {
	# 	"validate": "goldapp.golds.override.property_setter.validate",
	# 	"on_trash": "goldapp.golds.override.property_setter.on_trash",
	# },
	"Sales Invoice":{
		"validate": "goldapp.golds.override.items.validate"
	}
}



override_whitelisted_methods = {
	
	"erpnext.stock.utils.scan_barcode": "goldapp.golds.override.custom_serial_no.custom_scan_barcode",
	
	# "erpnext.stock.doctype.serial_no.serial_no.update_serial_nos_after_submit":"goldapp.golds.override.custom_serial_no.custom_update_serial_nos_after_submit"
}



doctype_js = {"Purchase Order" : "public/js/purchase_order_item.js",
			  "Sales Order" : "public/js/sales_order_item.js",
			  "Stock Entry" : "public/js/stock_entry_details.js",
			  "Sales Invoice" : "public/js/sales_invoice_item.js",
			  "Purchase Invoice" : "public/js/purchase_invoice_item.js",
			  "Purchase Receipt": "public/js/purchase_receipt_item.js",
			  "Delivery Note": "public/js/delivery_note_item.js",
			  "Serial No": "public/js/serial_no.js",
			  }

fixtures =[    
	{"dt":"Custom Field", "filters": [["dt", "in", ("Item","Sales Invoice","Sales Invoice Item","Sales Order","Sales Order Item","Stock Entry","Stock Entry Details","Purchase Invice","Purchase Invoice Item","Purchase Order","Purchase Order Item","Purchase Receipt","Purchase Receipt Item","Delivery Note","Delivery Note Item","Serial No")]]},
	'Property Setter',
	
]


gold_doctypes = [
	"Item",
	"Sales Invoice",
	"Sales Invoice Item",
	"Sales Order",
	"Sales Order Item",
	"Stock Entry",
	"Stock Entry Details",
	"Purchase Invice",
	"Purchase Invoice Item",
	"Purchase Order",
	"Purchase Order Item",
	"Purchase Receipt",
	"Purchase Receipt Item",
	"Delivery Note",
	"Delivery Note Item",
	"Serial No"
	]



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/goldapp/css/goldapp.css"
# app_include_js = "/assets/goldapp/js/goldapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/goldapp/css/goldapp.css"
# web_include_js = "/assets/goldapp/js/goldapp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "goldapp/public/scss/website"

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "goldapp.utils.jinja_methods",
# 	"filters": "goldapp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "goldapp.install.before_install"
# after_install = "goldapp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "goldapp.uninstall.before_uninstall"
# after_uninstall = "goldapp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "goldapp.utils.before_app_install"
# after_app_install = "goldapp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "goldapp.utils.before_app_uninstall"
# after_app_uninstall = "goldapp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "goldapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# override_doctype_class = {
# 	# "Serial No": "goldapp.serial_no.Custom_Serial_No",
# 	# "Stock Entry":"goldapp.Custom_Stock_Entery.Custom_Stock_Entery"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"goldapp.tasks.all"
# 	],
# 	"daily": [
# 		"goldapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"goldapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"goldapp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"goldapp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "goldapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "goldapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "goldapp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["goldapp.utils.before_request"]
# after_request = ["goldapp.utils.after_request"]

# Job Events
# ----------
# before_job = ["goldapp.utils.before_job"]
# after_job = ["goldapp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"goldapp.auth.validate"
# ]
