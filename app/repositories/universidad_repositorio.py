from app.models import Universidad
from .base_repositorios import BaseRepository

class UniversidadRepository(BaseRepository):
    """
    Repositorio para gestionar las universidades, hereda de BaseRepository.
    """
    def __init__(self):
        super().__init__(Universidad)