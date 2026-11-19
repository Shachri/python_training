from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from model.contact import Contact
from fixture.application import Application
from fixture.session import SessionHelper

@pytest.fixture(autouse=True)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login('admin', 'secret')
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович'))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login('admin', 'secret')
    app.contact.init_contact(Contact('Иван', 'Иванов', 'Иванович'))
    app.session.logout()








