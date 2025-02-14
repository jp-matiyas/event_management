// Copyright (c) 2024, Jay Patel and contributors
// For license information, please see license.txt

frappe.query_reports["Event Management Script Report"] = {
	"filters": [
		{
            "fieldname": "event_date",
            "label": __("Event Date"),
            "fieldtype": "Date",
            
        },
		{
            "fieldname": "event_name",
            "label": __("Event Name"),
            "fieldtype": "Data",
            
        },
		{
            "fieldname": "venue",
            "label": __("Venue"),
            "fieldtype": "Data",
            
        },
		{
            "fieldname": "organizer",
            "label": __("Organizer"),
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.now_date(), -1),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.now_date(),
            "reqd": 1
        }
	]
};
