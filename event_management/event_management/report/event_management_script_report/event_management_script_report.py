# Copyright (c) 2024, Jay Patel and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_evm_data(filters)
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
        {
            'fieldname': 'customer_name',
            'label': _('Customer Name'),
            'fieldtype': 'Data',
            'width': '150'
        },
        {
            'fieldname': 'customer_email',
            'label': _('Customer Email'),
            'fieldtype': 'Data',
            'width': '150'
        },
    ]

def get_evm_data(filters):
    conditions = []
    
    # Add filters for Event Management fields
    if filters.get("event_name"):
        conditions.append("evm.event_name LIKE '%%%s%%'" % filters["event_name"])
    if filters.get("venue"):
        conditions.append("evm.venue LIKE '%%%s%%'" % filters["venue"])
    if filters.get("event_date"):
        conditions.append("evm.event_date = '%s'" % filters["event_date"])
    if filters.get("organizer"):
        conditions.append("evm.organizer LIKE '%%%s%%'" % filters["organizer"])

    conditions_str = " AND ".join(conditions) if conditions else "1=1"

    # Query to fetch event management data along with customer details
    query = """
        SELECT
            evm.event_name,
            evm.venue,
            evm.event_date,
            evm.organizer,
            cust.customer_name,
            cust.customer_email
        FROM
            `tabEvent Management` evm
        LEFT JOIN
            `tabCustomer` cust ON evm.customer = cust.name
        WHERE
            {conditions}
        ORDER BY
            evm.event_name DESC
    """.format(conditions=conditions_str)

    # Execute the query and return the data
    return frappe.db.sql(query, as_dict=1)
