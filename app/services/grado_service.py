from app.models import Grado
from app.repositories import GradoRepository
from .base_service import BaseService


class GradoService(BaseService):

    def __init__(self):
        repository = GradoRepository()

        super().__init__(repository)

    def actualizar(self, id: int, data: Grado) -> Grado:
        grado_existente = self.repository.buscar_por_id(id)
        if not grado_existente:
            return None
        grado_existente.nombre = data.nombre
        grado_existente.descripcion = data.descripcion
        return self.repository.actualizar(grado_existente)
