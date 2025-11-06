from app import db
from app.models import Materia, Autoridad
from .base_repositorios import BaseRepository

class MateriaRepository(BaseRepository):
    
    def __init__(self):
        super().__init__(Materia)


    @staticmethod
    def asociar_autoridad(materia: Materia, autoridad: Autoridad):
        materia.asociar_autoridad(autoridad)
        db.session.commit()

    @staticmethod
    def desasociar_autoridad(materia: Materia, autoridad: Autoridad):
        materia.desasociar_autoridad(autoridad)
        db.session.commit()