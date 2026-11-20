from model.group import Group
from fixture.application import Application
import pytest

def test_delete_group(app):
    app.group.delete(Group)

