from model.group import Group
from fixture.application import Application
import pytest


def test_edit_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group('test', 'test', 'test'))
    app.group.modify_first_group(Group(name='4', header='4', footer='4'))
    new_groups = app.group.get_group_list()
    assert  len(old_groups)==len(new_groups)
