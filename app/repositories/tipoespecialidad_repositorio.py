from app.models import TipoEspecialidad
from .base_repositorios import BaseRepository

class TipoEspecialidadRepository(BaseRepository):
    
    def __init__(self):
        super().__init__(TipoEspecialidad)