from model.group import Group
from fixture.application import Application
import pytest

def test_add_group(app):
    app.group.create(Group('new_group2', 'group_header', 'group_footer'))


def test_add_empty_group(app):
    app.group.create(Group('', '', ''))

