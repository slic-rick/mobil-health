import frappe
from healthcare.healthcare.doctype.patient_appointment.patient_appointment import PatientAppointment
from twilio.rest import Client
class Appointment(PatientAppointment):
	


	def after_insert(self):
		# frappe.msgprint("THE HOOK IS WORKING")
		account_sid = 'AC16288fd99b498354f7d0f6a9ec006407'
		auth_token = 'd7a9707eebd9a0f80b7e8abdc8724029'
		body = f"Good Day! Your Apointment with {self.practitioner_name} is sheduled on {self.appointment_date} at {self.appointment_time} Thank You!"
		client = Client(account_sid, auth_token)
		doc = frappe.get_doc('Patient', self.patient)
		if doc:
			message = client.messages.create(from_='+12565674632',to=f"+264{doc.mobile}",body=body)
		print(message.sid)
    
    