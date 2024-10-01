from erpnext.selling.doctype.installation_note.installation_note import InstallationNote
from erpnext.utilities.transaction_base import TransactionBase
import frappe
class installation_note_custom(TransactionBase):
    def validate(self):
        frappe.msgprint("\n\n\n Hello \n\n\n")
        return