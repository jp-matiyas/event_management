from erpnext.selling.doctype.installation_note.installation_note import InstallationNote
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from erpnext.utilities.transaction_base import TransactionBase
from erpnext.controllers.selling_controller import SellingController
from frappe.utils import nowdate
import frappe
class installation_note_custom(TransactionBase):
    def validate(self):
        frappe.msgprint("\n\n\n Hello \n\n\n")
        return
    
class SalesInvoice_custom(SalesInvoice):
    def validate(self):
        date = nowdate()
        if self.posting_date > date:
            frappe.throw("posting Date should not be greater than current date!")
