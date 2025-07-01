from app.app import app
import sys
import os


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Hello from Flask!" in response.data