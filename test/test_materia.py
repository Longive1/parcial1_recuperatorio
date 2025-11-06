import unittest
from app.models import Materia, Autoridad
from app.services import MateriaService, AutoridadService
from test.instancias import nuevamateria, nuevaautoridad
from test.base import BaseTestCase 

class MateriaTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=MateriaService()

    def test_crear(self):
        autoridad = nuevaautoridad(nombre="Autoridad 1")
        materia = nuevamateria(autoridades=[autoridad])
        self.assertIsNotNone(materia.id)
        self.assertEqual(materia.nombre, "Matematica")
        self.assertIn(autoridad, materia.autoridades)

    def test_buscar_por_id(self):
        materia = nuevamateria()
        encontrado = self.service.buscar_por_id(materia.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, materia.nombre)

    def test_buscar_todos(self):
        materia1 = nuevamateria(nombre="Matematica 1")
        materia2 = nuevamateria(nombre="Matematica 2")
        materias = self.service.buscar_todos()
        self.assertIsNotNone(materias)
        self.assertGreaterEqual(len(materias), 2)
        nombres = [m.nombre for m in materias]
        self.assertIn("Matematica 1", nombres)
        self.assertIn("Matematica 2", nombres)

    def test_actualizar(self):
        materia = nuevamateria()
        materia.nombre = "Nombre Actualizado"
        actualizado = self.service.actualizar(materia.id, materia)
        self.assertEqual(actualizado.nombre, "Nombre Actualizado")

    def test_borrar(self):
        materia = nuevamateria()
        borrado = self.service.borrar_por_id(materia.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(materia.id)
        self.assertIsNone(resultado)

    def test_asociar_y_desasociar_autoridad(self):
        materia = nuevamateria()
        autoridad = nuevaautoridad()
        
        # Asociar autoridad
        self.service.asociar_autoridad(materia.id, autoridad.id)
        materia_actualizada = self.service.buscar_por_id(materia.id)
        self.assertIn(autoridad, materia_actualizada.autoridades)
        
        # Desasociar autoridad
        self.service.desasociar_autoridad(materia.id, autoridad.id)
        materia_actualizada = self.service.buscar_por_id(materia.id)
        self.assertNotIn(autoridad, materia_actualizada.autoridades)
