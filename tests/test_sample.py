# tests/test_sample.py

import unittest
from app.app import hello


class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
