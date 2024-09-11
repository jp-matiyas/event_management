# Copyright (c) 2024, Jay Patel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.utils import time_diff_in_hours
from datetime import date,datetime

class EventManagement(Document):
	
	
	def validate(self):
	#event date should not be less than current date.
		current_date = str(date.today())
		event_date = self.event_date
		if event_date < current_date:
			frappe.throw("enter valid event date")


	def before_save(self): 
	#getting the values of start and end time and storing it into variables.
		start_time_str = self.start_time
		end_time_str = self.end_time

    # Ensure both start_time and end_time are present
		if start_time_str and end_time_str:
        # Convert the time strings to datetime objects
			try:
				start_time = datetime.strptime(start_time_str, '%H:%M:%S')
				end_time = datetime.strptime(end_time_str, '%H:%M:%S')

            # Calculate the difference
				time_difference = end_time - start_time

            # Convert the difference to hours
				duration_in_hours = time_difference.total_seconds() / 3600
				rounded_num = round(duration_in_hours, 2)

            # Set the calculated duration in the 'duration' field
				self.duration = f"{rounded_num} hours"

            # Optionally, you can add a custom validation to make the field read-only by permissions
				frappe.msgprint(f"Duration calculated: {rounded_num} hours")

			except ValueError as e:
				frappe.throw(f"Time format error: {e}")

		else:
			frappe.throw("Start time or end time is missing.")

			