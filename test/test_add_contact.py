from model.contact import Contact
from fixture.application import Application
import pytest


def test_add_contact(app):
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович',address='Иваново'))

def test_add_empty_contact(app):
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович', address='Иваново'))








