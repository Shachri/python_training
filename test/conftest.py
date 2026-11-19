from fixture.application import Application
import pytest


@pytest.fixture(autouse=True, scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
