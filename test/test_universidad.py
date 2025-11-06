import unittest
from app.models import Universidad
from app.services import UniversidadService 
from app import db
from test.instancias import nuevauniversidad
from test.base import BaseTestCase 

class UniversidadTestCase(BaseTestCase):
    
    def setUp(self):
        super().setUp()
        self.service = UniversidadService()

    def test_crear(self):
        universidad = nuevauniversidad()
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.nombre, "Universidad Nacional")

    def test_buscar_por_id(self):
        universidad = nuevauniversidad()
        r = self.service.buscar_por_id(universidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Universidad Nacional")
        self.assertEqual(r.sigla, "UN")
    
    def test_buscar_todos(self):
        universidad1 = nuevauniversidad()
        universidad2 = nuevauniversidad()
        universidades = self.service.buscar_todos()
        self.assertIsNotNone(universidades)
        self.assertEqual(len(universidades), 2)

    def test_actualizar(self):
        universidad = nuevauniversidad()
        universidad.nombre = "Universidad Actualizada"
        universidad_actualizada = self.service.actualizar(universidad.id, universidad)
        self.assertEqual(universidad_actualizada.nombre, "Universidad Actualizada")

    def test_borrar(self):
        universidad = nuevauniversidad()
        borrado = self.service.borrar_por_id(universidad.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(universidad.id)
        self.assertIsNone(resultado)
