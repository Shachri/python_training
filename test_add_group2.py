from group import Group
from application import Application
import pytest


@pytest.fixture(autouse=True)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login('admin', 'secret')
    app.create_group(Group('new_group2', 'group_header', 'group_footer'))
    app.logout()


def test_add_empty_group(app):
    app.login('admin', 'secret')
    app.create_group(Group('', '', ''))
    app.logout()
