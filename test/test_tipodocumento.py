import unittest
import os
from flask import current_app
from app import create_app
from app.models.tipodocumento import TipoDocumento
from app.services import TipoDocumentoService
from test.instancias import nuevotipodocumento
from app import db
from test.base import BaseTestCase 

class TipoDocumentoTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service = TipoDocumentoService()

    def test_crear(self):
        tipodocumento = nuevotipodocumento()
        self.assertIsNotNone(tipodocumento)
        self.assertIsNotNone(tipodocumento.id)
        self.assertGreaterEqual(tipodocumento.id, 1)
        self.assertEqual(tipodocumento.dni, 46291002)

    def test_buscar_por_id(self):
        tipodocumento = nuevotipodocumento()
        r=self.service.buscar_por_id(tipodocumento.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.dni, 46291002)
        self.assertEqual(r.libreta_civica, "nacional")

    def test_buscar_todos(self):
        tipodocumento1 = nuevotipodocumento()
        tipodocumento2 = nuevotipodocumento(48291002, "23456789", "98765432", "CD123456")
        documentos = self.service.buscar_todos()
        self.assertIsNotNone(documentos)
        self.assertEqual(len(documentos), 2)

    def test_actualizar(self):
        tipodocumento = nuevotipodocumento()
        tipodocumento.dni = 89291002
        tipodocumento_actualizado = self.service.actualizar(tipodocumento.id, tipodocumento)
        self.assertEqual(tipodocumento_actualizado.dni, 89291002)
    
    def test_borrar(self):
        tipodocumento = nuevotipodocumento()
        borrado = self.service.borrar_por_id(tipodocumento.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(tipodocumento.id)
        self.assertIsNone(resultado)
