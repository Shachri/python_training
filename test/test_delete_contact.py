from model.contact import Contact
from fixture.application import Application
import pytest


def test_delete_contact(app):
    if app.contact.count()==0:
        app.contact.init_contact(Contact('test','test','test','test'))
    app.contact.delete()

