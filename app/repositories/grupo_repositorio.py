from app.models import Grupo
from .base_repositorios import BaseRepository

class GrupoRepository(BaseRepository):
    
    def __init__(self):
        super().__init__(Grupo)