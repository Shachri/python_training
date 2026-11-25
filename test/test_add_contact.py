from model.contact import Contact
from fixture.application import Application
import pytest


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact('Иван', 'Иванов', 'Иванович', address='Иваново')
    app.contact.init_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts,key=Contact.id_or_max)


'''def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact('Иван', 'Иванов', 'Иванович', address='Иваново')
    app.contact.init_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts,key=Contact.id_or_max)
'''