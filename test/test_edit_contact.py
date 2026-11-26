from model.contact import Contact
from fixture.application import Application
import pytest
from random import randrange

def test_edit_contact(app):
    contact = Contact('test', 'test', 'test', 'test', None, None, None, None, None)
    if app.contact.count() == 0:
        app.contact.init_contact(contact)
    old_contacts= app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.edit_by_index(contact,index)
    new_contacts= app.contact.get_contact_list()
    assert len(old_contacts)==len(new_contacts)
