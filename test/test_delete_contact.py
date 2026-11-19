from model.contact import Contact
from fixture.application import Application
import pytest


def test_delete_contact(app):
    app.session.login('admin', 'secret')
    app.contact.delete()
    app.session.logout()
