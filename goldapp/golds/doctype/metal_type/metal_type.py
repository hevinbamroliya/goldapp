# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MetalType(Document):
	pass

# ----- metal purity filter ----------
# @frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
# def query(doctype, txt, searchfield, start, page_len, filters):	
# 	return frappe.db.sql(""" SELECT 
# 								purity
# 							FROM `tabPurity`							
# 							WHERE
# 								metal_type = %(mt)s 			
# 								AND ({key} LIKE %(txt)s)								
								
# 						""".format(**{
# 									'key': searchfield,
									
# 								}), {
# 								'txt': "%{}%".format(txt),															
# 								'mt':filters.get('metal_type')
																								
# 						})
																								
				