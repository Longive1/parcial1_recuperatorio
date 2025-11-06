import unittest
import os
from app import create_app, db

class BaseTestCase(unittest.TestCase):
    """
    Clase de Test Base de la cual heredarán todos los
    otros tests de la aplicación.
    
    Contiene la lógica común setUp (crear app y db)
    y tearDown (destruir db).
    """
    
    def setUp(self):
        """ Se ejecuta ANTES de cada test. """
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """ Se ejecuta DESPUÉS de cada test. """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()