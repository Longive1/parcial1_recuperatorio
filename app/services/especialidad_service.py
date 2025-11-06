from app.models import Especialidad
from app.repositories import EspecialidadRepository, AlumnoRepository
from .base_service import BaseService

class EspecialidadService(BaseService):

    def __init__(self):
        repository = EspecialidadRepository()
        super().__init__(repository)
        self.alumno_repository = AlumnoRepository()

    def actualizar(self, id: int, data: Especialidad) -> Especialidad:
        especialidad_existente = self.repository.buscar_por_id(id)
        if not especialidad_existente:
            return None
        especialidad_existente.nombre = data.nombre
        especialidad_existente.letra = data.letra
        especialidad_existente.observacion = data.observacion
        especialidad_existente.tipoespecialidad_id = data.tipoespecialidad_id
        especialidad_existente.facultad_id = data.facultad_id
        return self.repository.actualizar(especialidad_existente)

    def obtener_alumnos_y_facultad(self, especialidad_id: int) -> dict:
        especialidad = self.repository.buscar_por_id(especialidad_id)
        if not especialidad:
            return None 
        facultad = especialidad.facultad 
        alumnos = self.alumno_repository.buscar_por_especialidad(especialidad_id)
        return {
            "facultad": facultad,
            "alumnos": alumnos
        }