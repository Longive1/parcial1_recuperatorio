from app.models import Cargo
from .base_repositorios import BaseRepository

class CargoRepository(BaseRepository):

    def __init__(self):
        super().__init__(Cargo)