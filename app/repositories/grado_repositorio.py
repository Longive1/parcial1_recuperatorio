from app.models import Grado
from .base_repositorios import BaseRepository

class GradoRepository(BaseRepository):
    
  def __init__(self):
    super().__init__(Grado)