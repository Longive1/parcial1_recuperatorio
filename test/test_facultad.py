import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.facultad import Facultad
from app.services.facultad_service import FacultadService
from test.instancias import nuevafacultad,nuevaautoridad
from test.base import BaseTestCase 

class FacultadTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=FacultadService()

    def test_crear(self):
        autoridad = nuevaautoridad()
        facultad = nuevafacultad(autoridades=[autoridad])
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertIsNotNone(facultad.universidad)
        self.assertEqual(facultad.universidad.nombre,"Universidad Nacional")
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias")
        self.assertIn(autoridad, facultad.autoridades)

    def test_buscar_por_id(self):
        autoridad = nuevaautoridad()
        facultad = nuevafacultad(autoridades=[autoridad])
        r=self.service.buscar_por_id(facultad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Facultad de Ciencias")
        self.assertEqual(r.autoridades[0].nombre, autoridad.nombre)

    def test_buscar_todos(self):
        facultad1 = nuevafacultad()
        facultad2 = nuevafacultad(nombre="Facultad de matematica")
        facultades = self.service.buscar_todos()
        self.assertIsNotNone(facultades)
        self.assertEqual(len(facultades), 2)
        nombres = [f.nombre for f in facultades]
        self.assertIn("Facultad de Ciencias", nombres)
        self.assertIn("Facultad de matematica", nombres)


    def test_actualizar(self):
        facultad= nuevafacultad()
        facultad.nombre = "Facultad de Ciencias Actualizada"
        facultad_actualizada = self.service.actualizar(facultad.id, facultad)
        self.assertEqual(facultad_actualizada.nombre, "Facultad de Ciencias Actualizada")

    def test_borrar(self):
        facultad = nuevafacultad()
        borrado = self.service.borrar_por_id(facultad.id)
        self.assertTrue(borrado)
        resultado = self.service.buscar_por_id(facultad.id)
        self.assertIsNone(resultado)
    
    def test_asociar_y_desasociar_autoridad(self):
        facultad = nuevafacultad()
        autoridad = nuevaautoridad()
        
        # Asociar autoridad
        self.service.asociar_autoridad(facultad.id, autoridad.id)
        facultad_actualizada = self.service.buscar_por_id(facultad.id)
        self.assertIn(autoridad, facultad_actualizada.autoridades)
        
        # Desasociar autoridad
        self.service.desasociar_autoridad(facultad.id, autoridad.id)
        facultad_actualizada = self.service.buscar_por_id(facultad.id)
        self.assertNotIn(autoridad, facultad_actualizada.autoridades)
