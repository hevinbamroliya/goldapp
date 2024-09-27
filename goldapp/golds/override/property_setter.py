import frappe
from frappe.utils import cint

def validate(doc, method=None):
    if (
        frappe.flags.in_install
        or frappe.flags.in_migrate
        or not is_gold_enabled()
    ):
        return

    is_protected = is_protected_property_setter(doc)
    if doc.is_new() and (not is_protected or cint(doc.value) == 1):
        return

    if is_protected:
        throw_cannot_change_property_error(doc)

    old_doc = doc.get_doc_before_save()
    if is_protected_property_setter(old_doc):
        throw_cannot_change_property_error(old_doc)


def on_trash(doc, method=None):
    if not is_gold_enabled() or not is_protected_property_setter(doc):
        return

    throw_cannot_change_property_error(doc)


def throw_cannot_change_property_error(doc):
    frappe.throw(
        _(
            "Cannot change the Track Changes property for {0}, since it has been"
            " enabled to maintain Gold"
        ).format(_(doc.doc_type))
    )


def is_protected_property_setter(doc):
    return (
        doc.doctype_or_field == "DocType"
        and doc.property == "track_changes"
        and doc.doc_type in get_gold_doctypes()
    )



def is_gold_enabled():
    return bool(frappe.db.get_single_value("Accounts Settings", "enable_audit_trail"))


def get_gold_doctypes():
    return set(frappe.get_hooks("gold_doctypes"))



@frappe.whitelist(methods=["POST"])
def enable_audit_trail():
    accounts_settings = frappe.get_doc("Accounts Settings")
    accounts_settings.enable_audit_trail = 1
    accounts_settings.flags.ignore_version = True
    accounts_settings.save()

