import pytest 
from faker import Faker
from fastapi.testclient import TestClient

from ots_nuke.application import get_app


@pytest.fixture(scope='session')
def fake():
    """Generator fake data"""
    return Faker()


@pytest.fixture
def app():
    """An instance of the FastAPI application for testing"""
    return get_app()

@pytest.fixture
def client(app) -> TestClient:
    """Sync test client"""
    return TestClient(app)
