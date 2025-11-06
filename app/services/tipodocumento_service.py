from app.models import TipoDocumento
from app.repositories import TipoDocumentoRepository
from .base_service import BaseService

class TipoDocumentoService(BaseService):

    def __init__(self):
        repository = TipoDocumentoRepository()

        super().__init__(repository)
