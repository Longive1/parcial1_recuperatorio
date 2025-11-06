import unittest
import os
from flask import current_app
from app import create_app
from app.models.area import Area
from app.services import AreaService
from test.instancias import nuevaarea
from app import db
from test.base import BaseTestCase

class AreaTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=AreaService()

    def test_crear(self):
        area = nuevaarea()
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.id)
        self.assertGreaterEqual(area.id, 1)
        self.assertEqual(area.nombre, "Matematica")

    def test_buscar_por_id(self):
        area = nuevaarea()
        r = self.service.buscar_por_id(area.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Matematica")

    def test_buscar_todos(self):
        area1 = nuevaarea("Matematica")
        area2 = nuevaarea("nombre2")
        areas = self.service.buscar_todos()
        self.assertIsNotNone(areas)
        self.assertEqual(len(areas), 2)

    def test_actualizar(self):
        area = nuevaarea()
        area.nombre = "nombre actualizado"
        area_actualizado = self.service.actualizar(area.id, area)
        self.assertEqual(area_actualizado.nombre, "nombre actualizado")

    def test_borrar(self):
        area = nuevaarea()
        borrado= self.service.borrar_por_id(area.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(area.id)
        self.assertIsNone(resultado)
