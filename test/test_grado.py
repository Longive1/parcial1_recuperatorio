import unittest
import os
from flask import current_app
from app import create_app
from app.models import Grado
from app.services import GradoService
from app import db
from test.instancias import nuevogrado
from test.base import BaseTestCase 


class GradoTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=GradoService()

    def test_crear(self):
        grado = nuevogrado()
        self.assertIsNotNone(grado)
        self.assertIsNotNone(grado.id)
        self.assertGreaterEqual(grado.id, 1)
        self.assertEqual(grado.nombre, "Primero")

    def test_buscar_por_id(self):
        grado = nuevogrado()
        r=self.service.buscar_por_id(grado.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Primero")
        self.assertEqual(r.descripcion, "Descripcion del primer grado")

    
    def test_buscar_todos(self):
        grado1 = nuevogrado()
        grado2 = nuevogrado()
        grados = self.service.buscar_todos()
        self.assertIsNotNone(grados)
        self.assertGreaterEqual(len(grados), 2)

    def test_actualizar(self):
        grado= nuevogrado()
        grado.nombre = "Segundo"
        grado.descripcion = "Descripción del segundo grado"
        grado_actualizado = self.service.actualizar(grado.id, grado)
        self.assertEqual(grado_actualizado.nombre, "Segundo")
        self.assertEqual(grado_actualizado.descripcion, "Descripción del segundo grado")

    def test_borrar(self):
        universidad = nuevogrado()
        borrado = self.service.borrar_por_id(universidad.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(universidad.id)
        self.assertIsNone(resultado)