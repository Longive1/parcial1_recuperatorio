from app.models import CategoriaCargo
from app.repositories import CategoriaCargoRepository
from .base_service import BaseService

class CategoriaCargoService(BaseService):

    def __init__(self):
        repository = CategoriaCargoRepository()

        super().__init__(repository)

    def actualizar(self, id: int, data: CategoriaCargo) -> CategoriaCargo:
        return super().actualizar(id, data)
