# Copyright (c) 2024, hevin and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class GoldLedgerEntry(Document):
	pass

	# [posting_date,item_code,uom,purity,purity_percentage,serial_no,warehouse,party_type,party,debit_amount,debit_gold,credit_amount,credit_gold,account_currency,debit_amount_in_account_currency,credit_amount_in_account_currency,voucher_type,voucher_no,fiscal_year,is_cancelled]

def goldstock(controller, parentfield):
	doc = frappe.new_doc('Gold Ledger Entry')
	doc.title = 'gold ledger entry'


	doc.insert()