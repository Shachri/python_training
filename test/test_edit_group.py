from model.group import Group
from fixture.application import Application
import pytest

def test_edit_group(app):
    app.session.login('admin', 'secret')
    app.group.edit(Group(name='4',header='4',footer='4'))
    app.session.logout()
