from model.contact import Contact
from fixture.application import Application
import pytest


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович', address='Иваново'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович', address='Иваново'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
