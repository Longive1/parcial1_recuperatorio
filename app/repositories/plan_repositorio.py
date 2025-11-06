from app.models import Plan
from .base_repositorios import BaseRepository

class PlanRepository(BaseRepository):
   
   def __init__(self):
      super().__init__(Plan)