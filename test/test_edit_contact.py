from model.contact import Contact
from fixture.application import Application
import pytest


def test_edit_contact(app):
    app.session.login('admin', 'secret')
    app.contact.edit(Contact('Сергей', 'Сергеевич', 'Сергеев','Иваново'))
    app.session.logout()
