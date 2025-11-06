from app.models import TipoDocumento
from .base_repositorios import BaseRepository

class TipoDocumentoRepository(BaseRepository):

    def __init__(self):
        super().__init__(TipoDocumento)