from erpnext.controllers.stock_controller import StockController
class GoldLedger(StockController):	
	def update_gold_ledger(self):
		sl_entries = []
		finished_item_row = self.get_finished_item_row()

		# make sl entries for source warehouse first
		self.get_sle_for_source_warehouse(sl_entries, finished_item_row)

		# SLE for target warehouse
		self.get_sle_for_target_warehouse(sl_entries, finished_item_row)

		# reverse sl entries if cancel
		if self.docstatus == 2:
			sl_entries.reverse()

		self.make_sl_entries(sl_entries)

	def get_finished_item_row(self):
		finished_item_row = None
		if self.purpose in ("Manufacture", "Repack"):
			for d in self.get("items"):
				if d.is_finished_item:
					finished_item_row = d

		return finished_item_row

	def get_sle_for_source_warehouse(self, sl_entries, finished_item_row):
		for d in self.get("items"):
			if cstr(d.s_warehouse):
				sle = self.get_sl_entries(
					d, {"warehouse": cstr(d.s_warehouse), "actual_qty": -flt(d.transfer_qty), "incoming_rate": 0}
				)
				if cstr(d.t_warehouse):
					sle.dependant_sle_voucher_detail_no = d.name
				elif finished_item_row and (
					finished_item_row.item_code != d.item_code or finished_item_row.t_warehouse != d.s_warehouse
				):
					sle.dependant_sle_voucher_detail_no = finished_item_row.name

				sl_entries.append(sle)

	def get_sle_for_target_warehouse(self, sl_entries, finished_item_row):
		for d in self.get("items"):
			if cstr(d.t_warehouse):
				sle = self.get_sl_entries(
					d,
					{
						"warehouse": cstr(d.t_warehouse),
						"actual_qty": flt(d.transfer_qty),
						"incoming_rate": flt(d.valuation_rate),
					},
				)
				if cstr(d.s_warehouse) or (finished_item_row and d.name == finished_item_row.name):
					sle.recalculate_rate = 1

				sl_entries.append(sle)
