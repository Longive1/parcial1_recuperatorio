from app.models import Autoridad
from app.repositories import AutoridadRepository, MateriaRepository,FacultadRepository
from .base_service import BaseService

class AutoridadService(BaseService):
    def __init__(self):
        super().__init__(AutoridadRepository())

        self.materia_repository = MateriaRepository()
        self.facultad_repository = FacultadRepository()


    def asociar_materia(self, autoridad_id: int, materia_id: int):
        autoridad = self.repository.buscar_por_id(autoridad_id)
        materia = self.materia_repository.buscar_por_id(materia_id) 
        if not autoridad or not materia:
            raise ValueError("Materia o autoridad no encontrada")
        # El método de asociación del Repositorio sigue siendo estático
        AutoridadRepository.asociar_materia(autoridad, materia)

    def desasociar_materia(self, autoridad_id: int, materia_id: int):
        autoridad = self.repository.buscar_por_id(autoridad_id)
        materia = self.materia_repository.buscar_por_id(materia_id)
        if not autoridad or not materia:
            raise ValueError("Materia o autoridad no encontrada")
        AutoridadRepository.desasociar_materia(autoridad, materia)
        
    def asociar_facultad(self, autoridad_id: int, facultad_id: int):
        autoridad = self.repository.buscar_por_id(autoridad_id)
        facultad = self.facultad_repository.buscar_por_id(facultad_id) 
        if not autoridad or not facultad:
            raise ValueError("Facultad o autoridad no encontrada")
        AutoridadRepository.asociar_facultad(autoridad, facultad)

    def desasociar_facultad(self, autoridad_id: int, facultad_id: int):
        autoridad = self.repository.buscar_por_id(autoridad_id)
        facultad = self.facultad_repository.buscar_por_id(facultad_id)
        if not autoridad or not facultad:
            raise ValueError("Facultad o autoridad no encontrada") 
        AutoridadRepository.desasociar_facultad(autoridad, facultad)