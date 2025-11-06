from app.models import Area
from .base_repositorios import BaseRepository

class AreaRepository(BaseRepository):
    
    def __init__(self):
        super().__init__(Area)