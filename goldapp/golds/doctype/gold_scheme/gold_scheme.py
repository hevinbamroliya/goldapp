# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt

import frappe
from datetime import date
from frappe.model.document import Document

class GoldScheme(Document):
	# pass
	def validate(self):
		self.set_status()

	
	def set_status(self):
		start_date = self.start_date  
		last_date = self.last_date_of_enroll
		today = str(date.today())
		frappe.msgprint("hello set status")

		if start_date <= today <= last_date:
			self.status = "Active"
		else:
			self.status = "Expired"


def gold_sche():
	doc = frappe.get_doc('Gold Scheme')
	doc.titale('hello')
	doc.save()
