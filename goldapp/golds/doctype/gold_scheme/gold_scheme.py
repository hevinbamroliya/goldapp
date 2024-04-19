# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GoldScheme(Document):
	def validate(self):
		self.set_satus()


	def set_satus(self):
		start_date = self.start_date
		last_date = self.last_date_of_enroll
		if start_date < last_date:
			
			self.status = "Active"
			
		else:
			self.status = "Expired"
