from app.models import Especialidad
from .base_repositorios import BaseRepository

class EspecialidadRepository(BaseRepository):

    def __init__(self):
        super().__init__(Especialidad)