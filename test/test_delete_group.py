from model.group import Group
from fixture.application import Application
import pytest


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group('test', 'test', 'test'))
    app.group.delete(Group)
