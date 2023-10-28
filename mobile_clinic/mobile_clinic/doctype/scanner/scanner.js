// Copyright (c) 2023, Wellness Warriors and contributors
// For license information, please see license.txt

frappe.ui.form.on('Scanner', {
	refresh: function(frm) {
		
			// // Trigger the redirection when the 'redirect_field' changes
			// frm.fields_dict.redirect_field.$input.on('change', function() {
			// 	// Check if the field has a value
			// 	if (frm.doc.redirect_field) {
			// 		// Redirect to the specified URL with the ID provided in the field
			// 		var patientId = encodeURIComponent(frm.doc.redirect_field);
			// 		var redirectUrl = 'http://mobi-health:8000/app/patient/' + patientId;
			// 		window.location.href = redirectUrl;
			// 	}
			// });

			frm.add_custom_button(__('Redirect'), function() {
				// Check if the data field has a value
				if (frm.doc.scanner) {
					// Redirect to the specified URL with the ID from the data field
					var patientId = encodeURIComponent(frm.doc.scanner);
					var redirectUrl = 'http://mobi-health:8000/app/patient/' + patientId;
					window.open(redirectUrl, '_blank'); // Opens in a new tab
				} else {
					frappe.msgprint(__('Please enter a redirect link.'));
				}
			});
		
	}
});
