import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture()
def client():
    """Provide a TestClient with a fresh copy of the in-memory activities data."""
    original_activities = copy.deepcopy(app_module.activities)

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))

    with TestClient(app_module.app) as test_client:
        yield test_client

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))
