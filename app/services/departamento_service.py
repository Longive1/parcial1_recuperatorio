from app.models import Departamento
from app.repositories import DepartamentoRepository
from .base_service import BaseService

class DepartamentoService(BaseService):

    def __init__(self):
        repository = DepartamentoRepository()
        super().__init__(repository)
