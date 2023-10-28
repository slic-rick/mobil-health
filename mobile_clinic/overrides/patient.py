import frappe
from healthcare.healthcare.doctype.patient.patient import Patient

class CustomPatient(Patient):
	def validate(self):
		frappe.msgprint("THE HOOK IS WORKING")