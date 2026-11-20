from fixture.application import Application
import pytest


@pytest.fixture(autouse=True, scope='session')
def app(request):
    fixture = Application()
    fixture.session.login('admin', 'secret')

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
