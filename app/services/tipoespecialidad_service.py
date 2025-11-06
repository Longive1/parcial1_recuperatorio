from app.models import TipoEspecialidad
from app.repositories import TipoEspecialidadRepository
from .base_service import BaseService


class TipoEspecialidadService(BaseService):

    def __init__(self):
        repository = TipoEspecialidadRepository()

        super().__init__(repository)
