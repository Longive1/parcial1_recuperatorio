from app.models import Orientacion
from app.repositories import OrientacionRepository
from .base_service import BaseService

class OrientacionService(BaseService):

    def __init__(self):
        repository = OrientacionRepository()

        super().__init__(repository)

    def actualizar(self, id: int, data: Orientacion) -> Orientacion:
        existente = self.repository.buscar_por_id(id)
        if not existente:
            return None
        existente.nombre = data.nombre
        existente.especialidad_id = data.especialidad_id
        existente.plan_id = data.plan_id
        existente.materia_id = data.materia_id
        return self.repository.actualizar(existente)
