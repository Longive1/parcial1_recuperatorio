import unittest
import os
from flask import current_app
from app import create_app
from app.models import Especialidad, TipoEspecialidad
from app.services import EspecialidadService, TipoEspecialidadService
from test.instancias import nuevaespecialidad, nuevotipoespecialidad
from app import db
from test.base import BaseTestCase

class EspecialidadTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=EspecialidadService()

    def test_crear(self):
        especialidad= nuevaespecialidad()
        self.assertIsNotNone(especialidad)
        self.assertIsNotNone(especialidad.id)
        self.assertGreaterEqual(especialidad.id,1)
        self.assertEqual(especialidad.nombre, "Matematicas")
        self.assertEqual(especialidad.tipoespecialidad.nombre, "Cardiologia")

    def test_buscar_por_id(self):
        especialidad = nuevaespecialidad()
        r=self.service.buscar_por_id(especialidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Matematicas")
        self.assertEqual(r.letra, "A")

    def test_buscar_todos(self):
        especialidad1 =nuevaespecialidad()
        especialidad2 =nuevaespecialidad()
        especialidades = self.service.buscar_todos()
        self.assertIsNotNone(especialidades)
        self.assertEqual(len(especialidades),2)

    def test_actualizar(self):
        especialidad = nuevaespecialidad()
        especialidad.nombre = "matematica actualizada"
        especialidad_actualizada = self.service.actualizar(especialidad.id, especialidad)
        self.assertEqual(especialidad_actualizada.nombre, "matematica actualizada")

    def test_borrar(self):
        especialidad = nuevaespecialidad()
        borrado = self.service.borrar_por_id(especialidad.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(especialidad.id)
        self.assertIsNone(resultado)

    