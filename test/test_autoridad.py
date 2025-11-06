import unittest
from app import create_app, db
from app.models import Autoridad, Materia
from app.services import AutoridadService
from test.instancias import nuevaautoridad, nuevamateria, nuevafacultad
from test.base import BaseTestCase

class AutoridadTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=AutoridadService()

    def test_crear(self):
        facultad = nuevafacultad()
        materia = nuevamateria()
        autoridad = nuevaautoridad(materias=[materia], facultades=[facultad])
        self.assertIsNotNone(autoridad.id)
        self.assertEqual(autoridad.nombre, "Pelo")
        self.assertIn(materia, autoridad.materias)
        self.assertIn(facultad, autoridad.facultades)
        

    def test_buscar_por_id(self):
        autoridad = nuevaautoridad()
        encontrado = self.service.buscar_por_id(autoridad.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, autoridad.nombre)

    def test_buscar_todos(self):
        autoridad1 = nuevaautoridad(nombre="Pelo1")
        autoridad2 = nuevaautoridad(nombre="Pelo2")
        autoridades = self.service.buscar_todos()
        self.assertIsNotNone(autoridades)
        self.assertGreaterEqual(len(autoridades), 2)
        nombres = [a.nombre for a in autoridades]
        self.assertIn("Pelo1", nombres)
        self.assertIn("Pelo2", nombres)

    def test_actualizar(self):
        autoridad = nuevaautoridad()
        autoridad.nombre = "Nombre Actualizado"
        actualizado = self.service.actualizar(autoridad.id, autoridad)
        self.assertEqual(actualizado.nombre, "Nombre Actualizado")

    def test_borrar(self):
        autoridad = nuevaautoridad()
        borrado = self.service.borrar_por_id(autoridad.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(autoridad.id)
        self.assertIsNone(resultado)

    def test_relacion_materias(self):
        autoridad = nuevaautoridad()
        materia1 = nuevamateria(nombre="Matematica")
        materia2 = nuevamateria(nombre="Fisica")

        # Asociar materias desde autoridad.materias 
        autoridad.materias.append(materia1)
        autoridad.materias.append(materia2)
        db.session.commit()

        self.assertIn(materia1, autoridad.materias)
        self.assertIn(materia2, autoridad.materias)
        self.assertIn(autoridad, materia1.autoridades)
        self.assertIn(autoridad, materia2.autoridades)

        # Desasociar una materia
        autoridad.materias.remove(materia1)
        db.session.commit()
        self.assertNotIn(materia1, autoridad.materias)
        self.assertNotIn(autoridad, materia1.autoridades)

    def test_asociar_y_desasociar_materia(self):
        autoridad = nuevaautoridad()
        materia = nuevamateria()

        # Asociar materia
        self.service.asociar_materia(autoridad.id, materia.id)
        autoridad_actualizada = self.service.buscar_por_id(autoridad.id)
        self.assertIn(materia, autoridad_actualizada.materias)

        # Desasociar materia
        self.service.desasociar_materia(autoridad.id, materia.id)
        autoridad_actualizada = self.service.buscar_por_id(autoridad.id)
        self.assertNotIn(materia, autoridad_actualizada.materias)

    def test_asociar_y_desasociar_facultad(self):
        facultad = nuevafacultad()
        autoridad = nuevaautoridad()

        # Asociar facultad
        self.service.asociar_facultad(autoridad.id, facultad.id)
        autoridad_actualizada = self.service.buscar_por_id(autoridad.id)
        self.assertIn(facultad, autoridad_actualizada.facultades)

        # Desasociar facultad
        self.service.desasociar_facultad(autoridad.id, facultad.id)
        autoridad_actualizada = self.service.buscar_por_id(autoridad.id)
        self.assertNotIn(facultad, autoridad_actualizada.facultades)
