import unittest
from flask import current_app
from app import create_app, db

from test.base import BaseTestCase

class IndexTestCase(BaseTestCase):


    def test_index(self):
        client = self.app.test_client(use_cookies=True)
        response = client.get('/api/v1/home')
        self.assertEqual(response.status_code, 200)
