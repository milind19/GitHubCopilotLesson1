from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


_INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app_module, "activities", deepcopy(_INITIAL_ACTIVITIES))
    with TestClient(app_module.app, follow_redirects=False) as test_client:
        yield test_client
