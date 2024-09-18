// // Copyright (c) 2024, Jay Patel and contributors
// // For license information, please see license.txt

frappe.ui.form.on("Event Management", {
	after_save: function(frm) {
        
            // Fetch the last 5 events
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    doctype: 'Event Management',
                    fields: ['name', 'event_name', 'event_date'],
                    order_by: 'creation desc',
                    limit: 5
                },
                callback: function(r) {
                    if (r.message) {
                        let events = r.message;
                        let event_options = '';
                        //to display only 5 events
                        let event_count = 0;

                        // Generate clickable links for the last 5 events
                        events.forEach(function(event) {
                            if (event_count < 5) {
                            event_options += `
                                <p><a href="javascript:void(0);" data-event="${event.name}">
                                    ${event.event_name} (${event.event_date})
                                </a></p>`;
                                event_count++;
                            }
                        });
                            // frappe.msgprint(`${event_options}`);
                            
                        // Create the dialog box
                        let dialog = new frappe.ui.Dialog({
                            title: 'Event Created',
                            fields: [
                                {
                                    label: 'Message',
                                    fieldname: 'message',
                                    fieldtype: 'HTML',
                                    options: `<p><strong>Event has been created!</strong></p>`
                                },
                                {
                                    label: 'Last 5 Events',
                                    fieldname: 'last_5_events',
                                    fieldtype: 'HTML',
                                    options: event_options
                                }
                            ],
                            primary_action_label: 'Close',
                            primary_action: function() {
                                dialog.hide();
                            }
                        });

                        // Show the dialog
                        dialog.show();
                        
                        dialog.$wrapper.find('[data-event]').on('click', function() {
                            let event_name = $(this).data('event');
                            // Navigate to the clicked event
                            frappe.set_route('Form', 'Event Management', event_name);
                        });
                        // Mark the dialog as shown
                        frm.dialog_shown = true;
                    }
                }
            });
        
    }
       
});
