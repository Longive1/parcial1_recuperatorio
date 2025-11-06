import unittest
import os
from flask import current_app
from app import create_app
from app.models import TipoEspecialidad
from app.services import TipoEspecialidadService
from app import db
from test.instancias import nuevotipoespecialidad
from test.base import BaseTestCase 


class TipoEspecialidadTestCase(BaseTestCase):
    
    def setUp(self):
        super().setUp()
        self.service = TipoEspecialidadService()

    def test_crear(self):
        tipoespecialidad = nuevotipoespecialidad()
        self.assertIsNotNone(tipoespecialidad)
        self.assertIsNotNone(tipoespecialidad.id)
        self.assertGreaterEqual(tipoespecialidad.id, 1)    
        self.assertEqual(tipoespecialidad.nombre, "Cardiologia")
        self.assertEqual(tipoespecialidad.nivel, "Avanzado")

    def test_buscar_por_id(self):
        tipoespecialidad = nuevotipoespecialidad()
        r=self.service.buscar_por_id(tipoespecialidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, tipoespecialidad.nombre)
    
    def test_buscar_todos(self):
        tipoespecialidad1 = nuevotipoespecialidad()
        tipoespecialidad2 = nuevotipoespecialidad("pediatria", "Basico")
        tipoespecialidad = self.service.buscar_todos()
        self.assertIsNotNone(tipoespecialidad)
        self.assertGreaterEqual(len(tipoespecialidad), 2)

    def test_actualizar(self):
        tipoespecialidad = nuevotipoespecialidad()
        tipoespecialidad.nombre = "Neurología"
        tipoespecialidad.nivel = "Intermedio"
        tipoespecialidad_actualizado = self.service.actualizar(tipoespecialidad.id, tipoespecialidad)
        self.assertEqual(tipoespecialidad_actualizado.nombre, "Neurología")
        self.assertEqual(tipoespecialidad_actualizado.nivel, "Intermedio")

    def test_borrar(self):
        tipoespecialidad = nuevotipoespecialidad()
        borrado = self.service.borrar_por_id(tipoespecialidad.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(tipoespecialidad.id)
        self.assertIsNone(resultado)
    
