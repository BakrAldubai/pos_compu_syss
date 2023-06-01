from erpnext.accounts.utils import get_balance_on
from frappe.utils import now

def get_balance(doc, method=None):
    doc.party_balance_before_transiction = get_balance_on(
        account=doc.debit_to,
        date=doc.posting_date,
        party_type="Customer",
        party=doc.customer,
        company=doc.company
    )
    doc.party_balance_after_transiction = doc.party_balance_before_transiction + doc.outstanding_amount