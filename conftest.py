import pytest

from service.client import RobotFrameworkApi


def pytest_configure():
    RobotFrameworkApi.host = 'https://robotframework.org'


@pytest.fixture(scope='session')
def robot_framework():
    return RobotFrameworkApi()
