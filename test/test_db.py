import os
import unittest
from sqlalchemy import text
from app import create_app, db
from test.base import BaseTestCase


class ConnectionTestCase(BaseTestCase):

    def setUp(self): # (1)
        super().setUp()

    # test connection to db
    def test_db_connection(self):
        result = db.session.query(text("'Hello world'")).one()
        self.assertEqual(result[0], 'Hello world')
    
if __name__ == '__main__':
    unittest.main()
