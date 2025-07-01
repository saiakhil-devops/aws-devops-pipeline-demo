import sys
import os
from app.app import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Hello from Flask!" in response.data
