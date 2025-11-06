from app.models import Area
from app.repositories import AreaRepository
from .base_service import BaseService

class AreaService(BaseService):

    def __init__(self):
        repository = AreaRepository()
        super().__init__(repository)

    def actualizar(self, id: int, data: Area) -> Area:
        return super().actualizar(id, data)
