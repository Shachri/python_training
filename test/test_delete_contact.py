from model.contact import Contact
from fixture.application import Application
import pytest


def test_delete_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count()==0:
        app.contact.init_contact(Contact('test','test','test','test'))
    app.contact.delete()
    new_contacts =app.contact.get_contact_list()
    assert len(old_contacts)-1==len(new_contacts)
    old_contacts[0:1]=[]
    assert old_contacts==new_contacts

