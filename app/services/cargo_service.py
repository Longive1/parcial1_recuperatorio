from app.models import Cargo
from app.repositories import CargoRepository
from .base_service import BaseService

class CargoService(BaseService):

    def __init__(self):
        repository = CargoRepository()

        super().__init__(repository)

    def actualizar(self, id: int, data: Cargo) -> Cargo:
        existente = self.repository.buscar_por_id(id)
        if not existente:
            return None
        existente.nombre = data.nombre
        existente.puntos = data.puntos
        existente.categoria_cargo_id = data.categoria_cargo_id
        existente.tipo_dedicacion_id = data.tipo_dedicacion_id
        return self.repository.actualizar(existente)
