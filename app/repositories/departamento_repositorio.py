from app.models import Departamento
from .base_repositorios import BaseRepository

class DepartamentoRepository(BaseRepository):

   def __init__(self):
      super().__init__(Departamento)