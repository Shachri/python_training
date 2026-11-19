from model.group import Group
from fixture.application import Application
import pytest

def test_delete_group(app):
    app.session.login('admin', 'secret')
    app.group.delete(Group)
    app.session.logout()
