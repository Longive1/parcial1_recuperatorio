import unittest
import os
from flask import current_app, jsonify
from app import create_app
from app.models import Especialidad, TipoEspecialidad
from app.services import EspecialidadService, TipoEspecialidadService
from test.instancias import nuevaespecialidad, nuevotipoespecialidad, nuevoalumno, nuevafacultad
from app import db
from test.base import BaseTestCase

class EspecialidadTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.service=EspecialidadService()
        self.client = self.app.test_client()

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

    def test_get_alumnos_por_especialidad(self):
     
        facultad1 = nuevafacultad(nombre="Facultad de Ingeniería")
        especialidad1 = nuevaespecialidad(nombre="Sistemas", facultad=facultad1)
        
        alumno1 = nuevoalumno(nombre="Juan", apellido="Perez", especialidad=especialidad1)
        alumno2 = nuevoalumno(nombre="Ana", apellido="Gomez", especialidad=especialidad1)

        facultad2 = nuevafacultad(nombre="Facultad de Humanidades")
        especialidad2 = nuevaespecialidad(nombre="Letras", facultad=facultad2)
        alumno_otro = nuevoalumno(nombre="Luis", apellido="Lopez", especialidad=especialidad2)

        response = self.client.get(f'/api/v1/especialidad/{especialidad1.hashid}/alumnos')
        
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        
        self.assertIn('facultad', data)
        self.assertEqual(data['facultad']['nombre'], "Facultad de Ingeniería")
        self.assertEqual(data['facultad']['hashid'], facultad1.hashid)

        self.assertIn('alumnos', data)
        self.assertEqual(len(data['alumnos']), 2)
        
        nombres_alumnos_respuesta = {a['nombre'] for a in data['alumnos']}
        self.assertIn("Juan", nombres_alumnos_respuesta)
        self.assertIn("Ana", nombres_alumnos_respuesta)
        self.assertNotIn("Luis", nombres_alumnos_respuesta)

    def test_get_alumnos_por_especialidad_not_found(self):

        response = self.client.get('/api/v1/especialidad/hashid_invalido/alumnos')

        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['message'], "Especialidad no encontrada")