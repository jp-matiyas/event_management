# Copyright (c) 2024, Jay Patel and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
	# if not filters: filters = {}

	columns, data = [], []
	columns = get_columns()
	# evm_data = get_evm_data(filters)
	
	# if not evm_data:
	# 	msgprint(_('No records found'))
	# 	return columns, evm_data
	
	data = get_evm_data(filters)
	# for d in evm_data:
	# 	row = frappe._dict({
	# 			'event_name': d.event_name,
	# 			'event_date': d.event_date,
	# 			'venue': d.venue,
	# 			'organizer': d.organizer
	# 		})
	# 	data.append(row)
	return columns, data

def get_columns():
	return [
		{
			'fieldname': 'event_name',
			'label': _('Event Name'),
			'fieldtype': 'Data',
			'width': '120'
		},
		{
			'fieldname': 'event_date',
			'label': _('Event Date'),
			'fieldtype': 'Date',
			'width': '120'
		},
		{
			'fieldname': 'venue',
			'label': _('Venue'),
			'fieldtype': 'Data',
			'width': '100'
		},
		{
			'fieldname': 'organizer',
			'label': _('Organizer'),
			'fieldtype': 'Data',
			'width': '120'
		},
	]

# def get_evm_data(filters):
# 	conditions = get_conditions(filters)
# 	data = frappe.get_all(
# 		doctype='Event Management',
# 		fields=['event_name', 'event_date', 'venue','organizer'],
# 		filters=conditions,
# 		order_by='event_name desc'
# 	)
# 	return data

# def get_conditions(filters):
# 	conditions = {}
# 	for key, value in filters.items():
# 		if filters.get(key):
# 			conditions[key] = value

# 	return conditions

def get_evm_data(filters):
    # Initialize conditions list
    conditions = []
    
    # Add conditions based on filters
    if filters.get("event_name"):
        conditions.append("event_name LIKE '%%%s%%'" % filters["event_name"])
    if filters.get("venue"):
        conditions.append("venue LIKE '%%%s%%'" % filters["venue"])
    if filters.get("event_date"):
        conditions.append("event_date = '%s'" % filters["event_date"])
    if filters.get("organizer"):
        conditions.append("organizer LIKE '%%%s%%'" % filters["organizer"])

    # Join conditions with AND operator
    conditions_str = " AND ".join(conditions) if conditions else "1=1"

    # Query to fetch the data
    query = """
        SELECT
            event_name, venue, event_date, organizer
        FROM
            `tabEvent Management`
        WHERE
            {conditions}
        ORDER BY
            event_name DESC
    """.format(conditions=conditions_str)

    # Execute the query and return the data
    return frappe.db.sql(query, as_dict=1)