import json
import os.path
import pytest
from pages.application import Application

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope="function", autouse=False)
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser=browser, base_url=config["web"]["base_url"])
    fixture.home.ensure_login(login=config["web"]["login"], password=config["web"]["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.home.logout()
            fixture.destroy()

    request.addfinalizer(fin)
    return fixture
