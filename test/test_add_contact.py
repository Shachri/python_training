from model.contact import Contact
from fixture.application import Application
import pytest


def test_add_contact(app):
    app.session.login('admin', 'secret')
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович'))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login('admin', 'secret')
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович'))
    app.session.logout()








