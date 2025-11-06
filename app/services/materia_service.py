from app.models import Materia
from app.repositories import MateriaRepository, AutoridadRepository
from .base_service import BaseService

class MateriaService(BaseService):

    def __init__(self):
        super().__init__(MateriaRepository())
        self.autoridad_repository = AutoridadRepository()

    def asociar_autoridad(self, materia_id: int, autoridad_id: int):
        materia = self.repository.buscar_por_id(materia_id)
        autoridad = self.autoridad_repository.buscar_por_id(autoridad_id)
        if not materia or not autoridad:
            raise ValueError("Materia o autoridad no encontrada")
        MateriaRepository.asociar_autoridad(materia, autoridad)

    def desasociar_autoridad(self, materia_id: int, autoridad_id: int):
        materia = self.repository.buscar_por_id(materia_id)
        autoridad = self.autoridad_repository.buscar_por_id(autoridad_id)
        if not materia or not autoridad:
            raise ValueError("Materia o autoridad no encontrada")
        MateriaRepository.desasociar_autoridad(materia, autoridad)
