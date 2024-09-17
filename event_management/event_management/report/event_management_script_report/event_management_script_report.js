// Copyright (c) 2024, Jay Patel and contributors
// For license information, please see license.txt

frappe.query_reports["Event Management Script Report"] = {
	"filters": [
		{
            "fieldname": "event_date",
            "label": __("Event Date"),
            "fieldtype": "Date",
            // "reqd": 1
        },
		{
            "fieldname": "event_name",
            "label": __("Event Name"),
            "fieldtype": "Data",
            // "reqd": 1
        },
		{
            "fieldname": "venue",
            "label": __("Venue"),
            "fieldtype": "Data",
            // "reqd": 1
        },
		{
            "fieldname": "organizer",
            "label": __("Organizer"),
            "fieldtype": "Link",
            "options": "Employee"
        },
	]
};
