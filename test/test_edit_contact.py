from model.contact import Contact
from fixture.application import Application
import pytest


def test_edit_contact(app):
    old_contacts= app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.init_contact(Contact('test', 'test', 'test', 'test'))
    app.contact.edit(Contact('Сергей', 'Сергеевич', 'Сергеев', 'Иваново'))
    new_contacts= app.contact.get_contact_list()
    assert len(old_contacts)==len(new_contacts)
