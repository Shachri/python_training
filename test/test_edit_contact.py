from model.contact import Contact
from fixture.application import Application
import pytest


def test_edit_contact(app):
    app.contact.edit(Contact('Сергей', 'Сергеевич', 'Сергеев','Иваново'))

