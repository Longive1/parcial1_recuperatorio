from app.models import TipoDedicacion
from app.repositories import TipoDedicacionRepository
from .base_service import BaseService

class TipoDedicacionService(BaseService):

    def __init__(self):
        repository = TipoDedicacionRepository()

        super().__init__(repository)

    def actualizar(self, id: int, data: TipoDedicacion) -> TipoDedicacion:
        existente = self.repository.buscar_por_id(id)
        if not existente:
            return None
        existente.nombre = data.nombre
        existente.observacion = data.observacion
        return self.repository.actualizar(existente)
