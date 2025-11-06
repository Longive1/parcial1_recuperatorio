from app.models.universidad import Universidad
from app.repositories import UniversidadRepository
from .base_service import BaseService 

class UniversidadService(BaseService):
    
    def __init__(self):
        repository = UniversidadRepository()
        
        super().__init__(repository)
    