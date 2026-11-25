from model.group import Group
from fixture.application import Application
import pytest
from random import randrange

def test_edit_group(app):
    group = Group('test', 'test', 'test')
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert  len(old_groups)==len(new_groups)
