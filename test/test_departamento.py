import unittest
import os
from flask import current_app
from app import create_app
from app.models.departamento import Departamento
from app.services import DepartamentoService
from app import db
from test.instancias import nuevodepartamento
from test.base import BaseTestCase

class DepartamentoTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=DepartamentoService()


    def test_crear(self):
        departamento = nuevodepartamento()
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.id)
        self.assertGreaterEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, "Matematicas")

    def test_buscar_por_id(self):
        departamento = nuevodepartamento()
        r=self.service.buscar_por_id(departamento.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Matematicas")
        

    def test_buscar_todos(self):
        departamento1 = nuevodepartamento()
        departamento2 = nuevodepartamento("Fisica")
        departamentos = self.service.buscar_todos()
        self.assertIsNotNone(departamentos)
        self.assertEqual(len(departamentos), 2)

    def test_actualizar(self):
        departamento = nuevodepartamento()
        departamento.nombre = "Matematicas actualizado"
        departamento_actualizado = self.service.actualizar(departamento.id, departamento)
        self.assertEqual(departamento_actualizado.nombre, "Matematicas actualizado")
    
    def test_borrar(self):
        departamento = nuevodepartamento()
        borrado= self.service.borrar_por_id(departamento.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(departamento.id)
        self.assertIsNone(resultado)
        
    