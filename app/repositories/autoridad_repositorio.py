from app import db
from app.models import Autoridad, Materia, Facultad
from .base_repositorios import BaseRepository

class AutoridadRepository(BaseRepository):
    def __init__(self):
        super().__init__(Autoridad)

    @staticmethod
    def asociar_materia(autoridad: Autoridad, materia: Materia):
        autoridad.asociar_materia(materia)
        db.session.commit()

    @staticmethod
    def desasociar_materia(autoridad: Autoridad, materia: Materia):
        autoridad.desasociar_materia(materia)
        db.session.commit()

    @staticmethod
    def asociar_facultad(autoridad: Autoridad, facultad:Facultad):
        autoridad.asociar_facultad(facultad)
        db.session.commit()

    @staticmethod
    def desasociar_facultad(autoridad: Autoridad, facultad: Facultad):
        autoridad.desasociar_facultad(facultad)
        db.session.commit()
