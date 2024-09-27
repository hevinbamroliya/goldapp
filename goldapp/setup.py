import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

from goldapp.custom_fields import CUSTOM_FIELDS



def setup_fixtures():
    create_custom_fields(CUSTOM_FIELDS)
    create_property_setters_for_versioning()
    


def create_property_setters_for_versioning():
    for doctype in get_gold_doctypes():
        property_setter = frappe.new_doc("Property Setter")
        property_setter.update(
            {
                "doctype_or_field": "DocType",
                "doc_type": doctype,
                "property": "hidden",
                "value": "1",
                "property_type": "Check",
                "is_system_generated": 0,
            }
        )
        property_setter.flags.ignore_permissions = True
        property_setter.insert()


def get_gold_doctypes():
    return set(frappe.get_hooks("gold_doctypes"))

