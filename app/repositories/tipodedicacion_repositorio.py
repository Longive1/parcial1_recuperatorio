from app.models import TipoDedicacion
from .base_repositorios import BaseRepository

class TipoDedicacionRepository(BaseRepository):

    def __init__(self):
        super().__init__(TipoDedicacion)