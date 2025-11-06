import unittest
import os
from flask import current_app
from app import create_app
from app.models.grupo import Grupo
from app.services import GrupoService
from app import db
from test.instancias import nuevogrupo
from test.base import BaseTestCase 

class GrupoTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=GrupoService()
        
    def test_buscar_por_id(self):
        grupo = nuevogrupo()
        r=self.service.buscar_por_id(grupo.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Grupo A")
        
    def test_buscar_todos(self):
        grupo1 = nuevogrupo()
        grupo2 = nuevogrupo()
        grupos = self.service.buscar_todos()
        self.assertIsNotNone(grupos)
        self.assertEqual(len(grupos), 2)
        
    def test_actualizar(self):
        grupo = nuevogrupo()
        grupo.nombre = "Grupo B"
        grupo_actualizado = self.service.actualizar(grupo.id, grupo)
        self.assertEqual(grupo_actualizado.nombre, "Grupo B")

    def test_borrar(self):
        grupo = nuevogrupo()
        borrado = self.service.borrar_por_id(grupo.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(grupo.id)
        self.assertIsNone(resultado)
