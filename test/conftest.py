import pytest
from app import create_app
from dynaconf import settings


@pytest.fixture()
def app():
    app = create_app()
    return app


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="test")
