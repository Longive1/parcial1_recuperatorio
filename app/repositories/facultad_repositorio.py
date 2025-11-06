from app import db
from app.models import Facultad,Autoridad
from .base_repositorios import BaseRepository

class FacultadRepository(BaseRepository):
    
    def __init__(self):
        super().__init__(Facultad)

    @staticmethod
    def asociar_autoridad(facultad: Facultad, autoridad: Autoridad):
        facultad.asociar_autoridad(autoridad)
        db.session.commit()

    @staticmethod
    def desasociar_autoridad(facultad: Facultad, autoridad: Autoridad):
        facultad.desasociar_autoridad(autoridad)
        db.session.commit()
