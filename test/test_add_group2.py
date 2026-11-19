from model.group import Group
from fixture.application import Application
from fixture.session import SessionHelper
import pytest


@pytest.fixture(autouse=True)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login('admin', 'secret')
    app.group.create(Group('new_group2', 'group_header', 'group_footer'))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login('admin', 'secret')
    app.group.create(Group('', '', ''))
    app.session.logout()
