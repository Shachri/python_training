from model.group import Group
from fixture.application import Application
import pytest


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group('test', 'test', 'test'))
    app.group.edit(Group(name='4', header='4', footer='4'))
