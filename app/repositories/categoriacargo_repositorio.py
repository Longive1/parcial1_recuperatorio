from app.models import CategoriaCargo
from .base_repositorios import BaseRepository

class CategoriaCargoRepository(BaseRepository):

    def __init__(self):
        super().__init__(CategoriaCargo)