from app.models import Grupo
from app.repositories import GrupoRepository
from .base_service import BaseService

class GrupoService(BaseService):

    def __init__(self):
        repository = GrupoRepository()

        super().__init__(repository)

    def actualizar(self, id: int, data: Grupo) -> Grupo:
        existente = self.repository.buscar_por_id(id)
        if not existente:
            return None
        existente.nombre = data.nombre
        return self.repository.actualizar(existente)
