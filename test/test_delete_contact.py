from model.contact import Contact
from fixture.application import Application
import pytest


def test_delete_contact(app):
    app.contact.delete()

