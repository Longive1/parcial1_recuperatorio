import unittest
import os
from flask import current_app
from app import create_app
from app.models.categoriacargo import CategoriaCargo
from app.services import CategoriaCargoService
from test.instancias import nuevacategoriacargo
from app import db
from test.base import BaseTestCase

class CategoriaCargoTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=CategoriaCargoService()
        
    def test_crear(self):
        categoria = nuevacategoriacargo()
        self.assertIsNotNone(categoria)
        self.assertIsNotNone(categoria.id)
        self.assertGreaterEqual(categoria.id, 1)
        self.assertEqual(categoria.nombre, "Docente")

    def test_buscar_por_id(self):
        categoria = nuevacategoriacargo()
        r=self.service.buscar_por_id(categoria.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Docente")
        
    
    def test_buscar_todos(self):
        categoria1 = nuevacategoriacargo()
        categoria2 = nuevacategoriacargo()
        categorias = self.service.buscar_todos()
        self.assertIsNotNone(categorias)
        self.assertEqual(len(categorias), 2)

    def test_actualizar(self):
        categoria = nuevacategoriacargo()
        categoria.nombre = "Docente actualizado"
        categoria_actualizado = self.service.actualizar(categoria.id, categoria)
        self.assertEqual(categoria_actualizado.nombre, "Docente actualizado")

    def test_borrar(self):
        categoria = nuevacategoriacargo()
        borrado= self.service.borrar_por_id(categoria.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(categoria.id)
        self.assertIsNone(resultado)

    
        