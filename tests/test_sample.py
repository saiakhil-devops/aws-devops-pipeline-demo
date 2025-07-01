import sys
import os

# Add the app folder to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app import app  # Now Python can find app.py inside the app folder

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Hello from Flask!" in response.data
