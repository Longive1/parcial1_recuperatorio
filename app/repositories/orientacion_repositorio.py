from app.models import Orientacion
from .base_repositorios import BaseRepository
 
class OrientacionRepository(BaseRepository):
   
   def __init__(self):
      super().__init__(Orientacion)